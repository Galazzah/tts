from flask import Flask, render_template, request
app = Flask(__name__)

from helper import *

@app.route('/')
def my_form():
	return render_template("my-form.html")
	
@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	wav = get_raw_wav(text)
	return render_template(
		'index.html',
		title = 'New Phrase',
		wavfile = wav
	)

# @app.route('/')
# def home():
# 	return render_template(
# 		'index.html', 
# 		title = 'home', 
# 		wavfile = 
# 	)
	
@app.route('/cool')
def cool():
	return 'hello'


if __name__ == "__main__":
    app.run(debug=True)
	
	

