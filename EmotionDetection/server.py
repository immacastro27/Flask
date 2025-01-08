from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response_dict = emotion_detector(text_to_analyze)
    if response_dict['joy'] is None:
        return 'Error! Envalid text. Please try again'
    else:
        dominant_emotion = response_dict['dominant_emotion']
        response_dict.pop('dominant_emotion')
        response = f'For the given statement, the system response is ${response_dict}. The dominant emotion is ${dominant_emotion}.'
        response = response.replace('$', '')
        response = response.replace('{', '')
        response = response.replace('}', '')
        return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
