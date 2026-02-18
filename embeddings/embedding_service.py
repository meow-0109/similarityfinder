from sklearn.feature_extraction.text import TfidfVectorizer

class EmbeddingService:
    def __init__(self, messages):
        self.vectorizer = TfidfVectorizer()
        self.message_vectors = self.vectorizer.fit_transform(messages)

    def embed(self, text):
        return self.vectorizer.transform([text])
