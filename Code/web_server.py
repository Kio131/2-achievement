import asyncio
from flask import Flask, request, jsonify
from database import init_db
from app_server import process_number

app = Flask(__name__)

# Инициализируем БД (однократно)
asyncio.run(init_db())

@app.route("/rvs_web_app", methods=["POST"])
def handle_request():
    data = request.get_json()

    number = int(data["number"])

    result = process_number(number)

    return jsonify(result[0]), result[1]
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
