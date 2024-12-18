from sentiment_analysis.nlp_model import SentimentAnalysis
from chatbot.chatbot import Chatbot
from analytics_dashboard.analytics import AnalyticsDashboard
from public_consultation.consultation import PublicConsultation

def main():
    # Example usage of each component
    sentiment = SentimentAnalysis()
    chat_bot = Chatbot()
    analytics = AnalyticsDashboard()
    consultation = PublicConsultation()

    feedback = "The new healthcare policies are extremely helpful."
    print("Sentiment:", sentiment.analyze_sentiment(feedback))
    print("Category:", sentiment.categorize_feedback(feedback, ['healthcare', 'infrastructure', 'education']))
    
    user_query = "How can I access healthcare benefits?"
    print("Chatbot response:", chat_bot.get_response(user_query))
    
    analytics.add_data('Healthcare', 75)
    analytics.add_data('Education', 50)
    analytics.visualize_data()
    
    feedbacks = [
        "I am worried about the education budget cuts.",
        "The public transport system needs improvement.",
        "Healthcare has become better with recent updates."
    ]
    summary = consultation.summarize_feedbacks(feedbacks)
    for cluster, texts in summary.items():
        print(f"Cluster {cluster}:\n", "\n".join(texts), "\\n")

if __name__ == "__main__":
    main()
