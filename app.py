import os
import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def my_form():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text))))['compound']
    if(score > 0):
        label = 'This sentence is positive'
        col = 'text-success'
    elif(score == 0):
        label = 'This sentence is neutral'
        col = 'text-primary'
    else:
        label = 'This sentence is negative'
        col = 'text-danger'
    return(render_template('index.html', variable=label , color = col))
if __name__ == "__main__":
    app.run(port='8088', threaded=False, debug=True)