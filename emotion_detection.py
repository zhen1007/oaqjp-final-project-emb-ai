import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define headers for the request
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }

    # Define input JSON for the request
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        # Make a POST request to the Emotion Detection service
        response = requests.post(url, headers=headers, json=input_json)
        return response.text

    except Exception as e:
        print(f"Error: An exception occurred in case you experience connection error - {e}")
        return None