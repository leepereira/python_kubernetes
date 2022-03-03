from flask import Flask, jsonify, render_template
import time, random

app = Flask(__name__)

# list of cat images

images = [
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg",
    "https://thumbs.dreamstime.com/z/i-love-coffee-13785741.jpg"
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template('index.html',url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
