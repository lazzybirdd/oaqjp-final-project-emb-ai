import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    print(f"Status code is: {response.status_code}")

    if (response.status_code == 400):
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = json.loads(response.text)

    dominant_emotion_score = 0
    dominant_emotion = None

    node = formatted_response["emotionPredictions"][0]["emotion"]
    for emotion in node:
        #print(emotion)
        score = node[emotion]
        if score > dominant_emotion_score:
            dominant_emotion_score = score
            dominant_emotion = emotion

    result = node
    result["dominant_emotion"] = dominant_emotion

    return result

#r = emotion_detector("I love this new technology")
#print(r)