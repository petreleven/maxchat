from flask import Flask
from flask import render_template

from flask_socketio import SocketIO, send

# create our server
app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/chatpage")
def chatPage():
    return render_template("index.html")


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on("message")
def handle_message(msg):
    print("Messsage :", msg)
    send(msg, broadcast=True)


socketio.run(app, debug=True)
