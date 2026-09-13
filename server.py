from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        message = "Invalid text! Please try again!"

    else:
        message = f"""
        For the given statement, the system response is
        'anger': {response['anger']}, 'disgust': {response['disgust']},
        'fear': {response['fear']}, 'joy': {response['joy']}, and
        'sadness: {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.
        """

    return message

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)