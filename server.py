
"""Flask web server for the Emotion Detector application."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Display the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze submitted text and display the result."""
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return render_template(
            "index.html",
            error="Invalid text! Please enter a sentence."
        ), 400

    result = emotion_detector(text_to_analyze)

    if result is None:
        return render_template(
            "index.html",
            error="Emotion detection failed. Please try again."
        ), 502

    if result["dominant_emotion"] is None:
        return render_template(
            "index.html",
            error="Unable to analyze the supplied text."
        ), 400

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
