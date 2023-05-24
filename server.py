from flask import Flask, jsonify, request 
from scrape import search
app = Flask(__name__)

@app.route("/search", methods=['GET'])
def hello_world():
    args = request.args
    results = search(args['query'])
    return results

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')