# web_server.py
from flask import Flask, request, jsonify
from database import init_db
from app_server import process_number

app = Flask(__name__)

init_db()

@app.route("/rvs_web_app", methods=["POST"])
def handle_request():
    data = request.get_json()

    number = int(data["number"])

    result, code = process_number(number)

    return jsonify(result), code
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
