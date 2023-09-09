from flask import Flask
app = Flask(__name__)

@app.route("/")
def message():
    return {"message": "Hello World"}
