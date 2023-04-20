from flask import Flask, request
import socket
app = Flask(__name__)

@app.route("/home", methods=["POST"])
def mainTask():
    print("hey")
    return {"data": "hey"}, 200


if __name__ == "__main__":
    app.run()