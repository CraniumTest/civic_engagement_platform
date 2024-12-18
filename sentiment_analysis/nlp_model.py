from transformers import pipeline

class SentimentAnalysis:
    def __init__(self):
        self.nlp = pipeline("sentiment-analysis")
        self.category_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    
    def analyze_sentiment(self, text: str) -> str:
        sentiment = self.nlp(text)[0]
        return sentiment['label']
    
    def categorize_feedback(self, text: str, categories: list) -> str:
        categories = self.category_model(text, candidate_labels=categories)
        return categories['labels'][0]
