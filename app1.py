
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ['GET'])
def home():
    return "<h1>APP clase 28_04_2021</h1><p>Papa, mi primera aplicacion desde GitHub</p>"


if __name__ == '__main__':
    app.run()
