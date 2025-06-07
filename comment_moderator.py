# Prediction function for future use
import joblib
def classify_comments(comments):
    model = joblib.load("Toxicity_classifier.pkl")
    predictions = model.predict(comments)
    return predictions