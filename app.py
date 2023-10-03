from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"name": "Sandrine", "Score": 100},
    {"name": "Gergelay", "Score": 87},
    {"name": "Frieda", "Score": 92},
    {"name": "Fritz", "Score": 40},
    {"name": "Sirius", "Score": 75},
]

@app.route("/")
def index():
    return render_template("index.html", students=students)