from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send
from botdev import bot
from flask import session, redirect, url_for
import os
from urllib import request

# create our server
app = Flask(__name__)
socket = SocketIO(app)
app.secret_key = os.urandom(24)

counsellors = {"admin": 1234}


@app.route("/login")
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username in counsellors and counsellors[username] == password:
        session['username'] = username
        return redirect(url_for('chatPage'))
    return render_template("login.html")


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
