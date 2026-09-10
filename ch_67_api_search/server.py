
from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/<received_word>")
def result_page(received_word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{received_word}"
    response = requests.get(url=api_url)
    if response.ok:
        result = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
        #? NOTE:- The successfull response is formatted like that (as far as I know). However, if the response json format changes I have to change the code.
        return render_template('result.html', answer = result)
    else:
        return render_template('failure.html')

if __name__ == "__main__":
    app.run(debug=True)