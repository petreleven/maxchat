from flask import Flask
from flask import render_template


# create our server
app = Flask(__name__)


@app.route("/chatpage")
def chatPage():
    return render_template("index.html")


app.run()
