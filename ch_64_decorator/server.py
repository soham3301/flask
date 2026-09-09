
from flask import Flask, render_template, abort
from functools import wraps

app = Flask(__name__)

user_data = {
    "soham3301": {
        "name": "soham",
        "age": 35,
        "email": "splint3r777@gmail.com",
        "username": "soham3301",
        "logged_in": True,
    },
    "tanu001": {
        "name": "amitabh",
        "age": 34,
        "email": "amitabhdeb@gmail.com",
        "username": "tanu001",
        "logged_in": True,
    },
    "akash007": {
        "name": "akash",
        "age": 35,
        "email": "sahaakash190@gmail.com",
        "username": "akash007",
        "logged_in": False,
    }
}

class User:
    def __init__(self, name, age, email, username, logged_in):
        self.name = name
        self.age = age
        self.email = email
        self.username = username
        self.logged_in = logged_in

users = {}

for username in user_data:
    new_user = User(user_data[username]["name"], user_data[username]["age"], user_data[username]["email"], user_data[username]["username"], user_data[username]["logged_in"])
    users[new_user.username] = new_user


@app.route("/")
def homepage():
    return render_template('index.html', all_users = users)

log_data = {}

def visited_page_logger(func):
    @wraps(func)
    def log_wrapper(*args, **kwargs):
        the_username = kwargs.get('username')
        if the_username in users:
            the_user = users[the_username]
            #? Note:- key of log_data should be a timestamp, not username
            log_data[the_user.username] = f"{the_user.name}'s details was checked"
        return func(*args, **kwargs)
    return log_wrapper

def authenticator(func):
    @wraps(func)
    def auth_wrapper(*args, **kwargs):
        the_username = kwargs.get('username')
        if the_username in users:
            the_user = users[the_username]
            if the_user.logged_in:
                return func(*args, **kwargs)
        abort(404)
    return auth_wrapper

@app.route("/user/<username>")
@authenticator
@visited_page_logger
def user_details(username):
    if username in users:
        return render_template('display_user_details.html', single_user = users[username])
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)