from transformers import pipeline

class Chatbot:
    def __init__(self):
        self.model = pipeline("conversational", model="microsoft/DialoGPT-medium")
    
    def get_response(self, user_input: str) -> str:
        return self.model([user_input])[0]['generated_text']
