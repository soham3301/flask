
import json
from flask import Flask, render_template, abort


app = Flask(__name__)

class User:
    def __init__(self, name, age, occupation, favourite_language):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.favourite_language = favourite_language

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "occupation": self.occupation,
            "favourite_language": self.favourite_language
        }

users = {}

with open("userdata.json") as userdata_file:
    data = json.load(userdata_file)
    for username in data:
        new_user = User(data[username]["name"], data[username]["age"], data[username]["occupation"], data[username]["favourite_language"])
        users[new_user.name] = new_user

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/user/<received_username>")
def result_page(received_username):
    if received_username in users:
        return render_template('result.html', user_data = users[received_username])
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)


# for _ in range(10):
#     u_name = input("Enter User Name: ")
#     u_age = int(input("Enter User Age: "))
#     u_occu = input("Enter User Occupation: ")
#     u_lang = input("Enter User Favourite Language: ")
#     an_user = User(u_name, u_age, u_occu, u_lang)
#     users[an_user.name] = an_user
#     print("User Added")


# with open("userdata.json", mode="w") as userdata_file:
#     formatted_dict = {}
#     for username in users:
#         formatted_dict[username] = users[username].to_dict()
#     json.dump(formatted_dict, userdata_file, indent=4)
