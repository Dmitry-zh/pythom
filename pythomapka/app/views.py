from app import app

@app.route("/")
def index():
    return "Hello Vladiks ty petuh"
