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

        # Check the response
        if response.status_code == 200:
            # Parse the response JSON and extract emotion scores
            formatted_response = json.loads(response.text)
            emotion_predictions = formatted_response.get('emotionPredictions', [])
            
            # Extract required emotions and their scores
            emotions = emotion_predictions[0].get('emotion', {})
            # Find the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)
            
            # Add the dominant emotion to emotions
            formatted_emotion = {**emotions, 'dominant_emotion': dominant_emotion}
            return formatted_emotion
            
        elif response.status_code == 400:
            # Handle blank entry error
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            print(f"Error: Emotion Detection request failed with status code {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error: An exception occurred in case you experience connection error - {e}")
        return None