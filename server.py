''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def get_emotion_detector():
    ''' This is a handler of incoming GET request "/emotionDetector"
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    #if (text_to_analyze is None) or (len(text_to_analyze.strip()) == 0):
    #    return "No input supplied!"

    response = emotion_detector(text_to_analyze)
    #if response is None:
    #    return "Invalid input ! Try again."
    print(response)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    #formatted_response = dumps(response, indent = 4)
    #formatted_response.replace("\n", "<br/>")

    return f"For the given statement, the system response is {response}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
