from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

class PublicConsultation:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.kmeans = KMeans(n_clusters=5)
    
    def summarize_feedbacks(self, documents: list) -> dict:
        X = self.vectorizer.fit_transform(documents)
        self.kmeans.fit(X)
        clustered_texts = {}
        for doc, cluster in zip(documents, self.kmeans.labels_):
            if cluster not in clustered_texts:
                clustered_texts[cluster] = []
            clustered_texts[cluster].append(doc)
        return clustered_texts
