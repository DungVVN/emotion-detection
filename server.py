"""Serve the Emotion Detection application using Flask."""
import requests
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze text and display emotion scores."""
    text = request.args.get("textToAnalyze", "")
    if not text.strip():
        return "Invalid text! Please try again!"

    try:
        result = emotion_detector(text)
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return "Emotion detection service is unavailable. Please try again.", 503

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/")
def index():
    """Render the application interface."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
