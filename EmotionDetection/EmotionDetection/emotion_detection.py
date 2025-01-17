import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    if not response:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None}

    emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
    #Looking for the dominant emotion
    max_value = max(emotion_dict.values())
    dominant_emotion = None
    for key, value in emotion_dict.items():
        if value == max_value:
            dominant_emotion = key
            break
    #Getting the return dictionary
    emotion_dict['dominant_emotion'] = dominant_emotion

    return emotion_dict