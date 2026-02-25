import json
import requests

def emotion_detector(text_to_analyze):
    """Analyze emotions and return scores + dominant emotion."""
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=payload, headers=headers, timeout=30)

    data = json.loads(response.text)

    # Estrutura típica do retorno: você vai navegar até o bloco de emoções
    emotions = data["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    dominant_emotion = max(
        {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness},
        key=lambda k: {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness}[k]
    )

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }