from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home_route():
    return jsonify({"message": "n word"})

if __name__ == '__main__':
    app.run()