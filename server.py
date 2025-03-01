from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send
from botdev import bot

# create our server
app = Flask(__name__)
socket = SocketIO(app)

users = {
    ""
}


@app.route("/chatpage")
def chatPage():
    return render_template("index.html")


@socket.on("connect")
def connect():
    print("someone is trying to connect")


@socket.on("message")
def message(clientMessage):
    print("I have received:", clientMessage)
    response = bot(clientMessage)
    send(response)


@socket.on("disconnect")
def disconnect():
    print("Someone left")


socket.run(app)
