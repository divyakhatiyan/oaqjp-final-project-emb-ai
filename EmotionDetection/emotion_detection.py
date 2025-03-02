import requests
import json

def emotion_detector(text_to_analyse):
    emotions = {}
    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    
    # If the response status code is 200, extract the emotions
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        maxvalue = max(emotions, key = emotions.get)
        emotions["dominant_emotion"] = maxvalue
    # If the response status code is 500, set emotions  to None

    elif response.status_code == 400:
        emotions['anger'] = "None"
        emotions['disgust'] = "None"
        emotions['fear'] = "None"
        emotions['joy'] = "None"
        emotions['sadness'] = "None"
        emotions['dominant_emotion'] = "None"
    elif response.status_code == 500:
        emotions['anger'] = "None"
        emotions['disgust'] = "None"
        emotions['fear'] = "None"
        emotions['joy'] = "None"
        emotions['sadness'] = "None"
        emotions['dominant_emotion'] = "None"

    # Return the emotions
    return emotions