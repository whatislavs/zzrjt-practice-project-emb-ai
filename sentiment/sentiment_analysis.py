'''
Sentiment analysis module
'''
import json
import requests


def sentiment_analyzer(text_to_analyse):
    '''
    Sentiment analysis function
    '''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    if response.status_code == 200:
        response_json_text = json.loads(response.text)
        label = response_json_text['documentSentiment']['label']
        score = response_json_text['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}
