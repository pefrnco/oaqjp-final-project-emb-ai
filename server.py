"""Flask server for emotion detection web app."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """Analyze input text and return emotion analysis."""
    # GET (do front): /emotionDetector?textToAnalyze=...
    text_to_analyze = request.args.get("textToAnalyze")

    # POST (opcional)
    if text_to_analyze is None:
        text_to_analyze = request.form.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)