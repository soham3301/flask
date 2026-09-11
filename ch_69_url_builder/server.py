from flask import Flask, render_template

app = Flask(__name__)

users = {
    "soham3301": {
        "username": "soham3301",
        "name": "Soham",
        "posts": {
            "01": "Good Morning",
            "02": "Good Afternoon",
            "03": "How are you?"
        }
    },
    "tanu007": {
        "username": "tanu007",
        "name": "Tanu",
        "posts": {
            "01": "The sky is blue today",
            "02": "Whats up",
            "03": "Lets walk"
        }
    },
    "akash123": {
        "username": "akash123",
        "name": "Akash",
        "posts": {
            "01": "I love cats",
            "02": "Its raining today",
            "03": "Good Night"
        }
    }
}

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/users")
def users_page():
    return render_template('users.html', users = users)

@app.route("/user/<user_id>")
def user_page(user_id):
    if user_id in users:
        return render_template('user.html', the_user = users[user_id])
    else:
        return render_template('user_not_found.html')

@app.route("/user/<username>/posts")
def posts_page(username):
    if username in users:
        return render_template('posts.html', the_user = users[username], all_posts = users[username]["posts"])
    else:
        return render_template('user_not_found.html')

if __name__ == "__main__":
    app.run(debug=True)