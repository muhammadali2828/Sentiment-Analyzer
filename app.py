from flask import Flask, render_template, request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()
chat_history = []  

def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >=  0.05:
        return "🟢 Positive Sentiment"
    elif sentiment_score['compound'] <= -0.05:
        return "🔴 Negative Sentiment"
    else:
        return "🟡 Neutral Sentiment"

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history
    if request.method == "POST":
        user_text = request.form["text"]
        sentiment = analyze_sentiment(user_text)
        chat_history.append({"You": user_text, "Chatbot": sentiment}) 
    return render_template("index.html",chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
