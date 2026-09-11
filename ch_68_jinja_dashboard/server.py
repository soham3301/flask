
from flask import Flask, render_template, abort

app = Flask(__name__)

users = {
    "soham3301": {
        "id": "soham3301",
        "role": "manager",
        "email": "splint3r777@gmail.com",
        "account_status": "active",
        "task_done": 67,
        "salary": 78000,
    },
    "tanu007": {
        "id": "tanu007",
        "role": "manager",
        "email": "amitabh678@gmail.com",
        "account_status": "active",
        "task_done": 9,
        "salary": 34000,
    },
    "rajesh123": {
        "id": "rajesh123",
        "role": "employee",
        "email": "das.rajesh44@gmail.com",
        "account_status": "active",
        "task_done": 32,
        "salary": 53000,
    },
    "akash1991": {
        "id": "akash1991",
        "role": "employee",
        "email": "saha.akash33@gmail.com",
        "account_status": "active",
        "task_done": 110,
        "salary": 48000,
    }
}

tasks = [{"ac_repair":"done"}, {"call_customer":"pending"}, {"send_report_to_ceo":"done"}, {"need_to_hire_hr":"pending"}, {"apply_for_fund":"pending"}]

projects = {
    "travel_website": {
        "name": "travel_website",
        "manager": "soham3301",
        "employee": ["akash1991"],
        "status": "complete"
    },
    "medical_app": {
        "name": "medical_app",
        "manager": "tanu007",
        "employee": ["rajesh123", "akash1991"],
        "status": "pending"
    },
    "weather_alert": {
        "name": "weather_alert",
        "manager": "tanu007",
        "employee": ["rajesh123"],
        "status": "complete"
    }
}


@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/projects")
def project_page():
    return render_template('projects.html', projects=projects, users=users)

@app.route("/users")
def users_page():
    return render_template('users.html', users=users)

@app.route("/tasks")
def tasks_page():
    return render_template('tasks.html', tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)