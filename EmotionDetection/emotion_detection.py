
import requests


def emotion_detector(text_to_analyze):
    """Analyze text using the Watson NLP emotion service."""

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30
        )

        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        if response.status_code != 200:
            return None

        result = response.json()
        emotions = result["emotionPredictions"][0]["emotion"]

        formatted_emotions = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"]
        }

        formatted_emotions["dominant_emotion"] = max(
            formatted_emotions,
            key=formatted_emotions.get
        )

        return formatted_emotions

    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None
