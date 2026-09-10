
from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

def get_quote():
    URL = "https://dummyjson.com/quotes/random"
    response = requests.get(url=URL)
    result = response.json()
    print(result)
    return result

@app.route("/")
def homepage():
    quote_dict = get_quote()
    return render_template('index.html', quote_data = quote_dict)

if __name__ == "__main__":
    app.run(debug=True)