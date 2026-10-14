# Emotion Detector

A Python web application that analyzes text using the IBM Watson NLP
emotion detection service.

## Features

- Detects anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Provides a Flask web interface.
- Handles blank input and service errors.

## Technologies

- Python
- Requests
- Flask
- IBM Watson NLP
- Pylint
- unittest

## Run the application

Install dependencies:

    python3 -m pip install requests flask pylint

Start the server:

    python3 server.py

## Run tests

    python3 -m unittest -v test_emotion_detection.py