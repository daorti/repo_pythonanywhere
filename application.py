from flask import Flask, jsonify, request
from datos_dummy import books

application = Flask(__name__)

@application.route('/', methods = ['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@application.route('/api/v1/resources/books/all', methods = ['GET'])
def get_all():
    return jsonify(books)


if __name__ == "__main__":

    application.debug = True
    application.run()