from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("links.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return render_template("index.html", data=data)
    except Exception as e:
        return f"Виникла помилка: {e}"

@app.route('/participants')
def participants():
    return render_template('participants.html')

@app.route('/evgen')
def evgen():
    return render_template('evgen.html')

if __name__ == "__main__":
    app.run(debug=True)
