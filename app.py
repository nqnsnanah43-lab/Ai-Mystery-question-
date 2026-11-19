import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from dotenv import load_dotenv
from database import init_db, save_game, get_history
from game_logic import CASE, PUZZLES, get_hint, check_answer, get_suspect_response
from ai_assistant import ask_detective

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-development-key")
init_db()

@app.route("/")
def index():
    return render_template("index.html", case=CASE, puzzles=PUZZLES)

@app.route("/api/hint", methods=["POST"])
def hint():
    data = request.get_json(silent=True) or {}
    puzzle_id = int(data.get("puzzle_id", 1))
    level = int(data.get("level", 1))
    return jsonify({"hint": get_hint(puzzle_id, level)})

@app.route("/api/answer", methods=["POST"])
def answer():
    data = request.get_json(silent=True) or {}
    puzzle_id = int(data.get("puzzle_id", 1))
    user_answer = str(data.get("answer", "")).strip()
    correct, message = check_answer(puzzle_id, user_answer)
    return jsonify({"correct": correct, "message": message, "points": 20 if correct else 0})

@app.route("/api/interview", methods=["POST"])
def interview():
    data = request.get_json(silent=True) or {}
    suspect = str(data.get("suspect", ""))
    question = str(data.get("question", "")).strip()
    if not question:
        return jsonify({"reply": "Please enter a question first."})
    return jsonify({"reply": get_suspect_response(suspect, question)})

@app.route("/api/detective", methods=["POST"])
def detective():
    data = request.get_json(silent=True) or {}
    question = str(data.get("question", "")).strip()
    context = str(data.get("context", ""))[:3000]
    if not question:
        return jsonify({"reply": "Ask me something about the case."})
    reply, mode = ask_detective(question, context)
    return jsonify({"reply": reply, "mode": mode})

@app.route("/api/complete", methods=["POST"])
def complete():
    data = request.get_json(silent=True) or {}
    player = str(data.get("player", "Detective")).strip()[:60] or "Detective"
    score = max(0, min(int(data.get("score", 0)), 10000))
    theory = str(data.get("theory", ""))[:1000]
    save_game(player, score, theory)
    return jsonify({"ok": True, "message": "Case result saved."})

@app.route("/history")
def history():
    return render_template("history.html", games=get_history())

if __name__ == "__main__":
    app.run(debug=True)
