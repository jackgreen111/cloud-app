import os
import socket
import time
from datetime import datetime

from flask import Flask, jsonify, render_template

app = Flask(__name__)

TITLE = "Cloud Technologies"
VERSION = os.getenv("APP_VERSION", "1.0.0")
GIT_SHA = os.getenv("GIT_SHA", "local")
STARTED_AT = datetime.now()
START_TS = time.time()

LABS = [
    {"n": 1, "title": "Введение в облачные технологии", "hours": 2, "done": True},
    {"n": 2, "title": "Виртуальные машины", "hours": 4, "done": True},
    {"n": 3, "title": "Linux и командная строка", "hours": 3, "done": True},
    {"n": 4, "title": "Сети и безопасность", "hours": 4, "done": True},
    {"n": 5, "title": "Хранилища данных", "hours": 3, "done": True},
    {"n": 6, "title": "Облачное приложение", "hours": 6, "done": True},
    {"n": 7, "title": "Контейнеры Docker", "hours": 5, "done": True},
    {"n": 8, "title": "Docker Compose", "hours": 4, "done": True},
    {"n": 9, "title": "Мониторинг и логи", "hours": 3, "done": True},
    {"n": 10, "title": "Масштабирование", "hours": 4, "done": True},
    {"n": 11, "title": "CI/CD для облачного приложения", "hours": 6, "done": False},
]

PIPELINE = [
    "Git Push", "Checkout", "Install dependencies", "Run tests",
    "Build Docker image", "Push image", "Deploy",
]

TECH = ["Git", "GitHub Actions", "Docker", "Flask", "pytest", "Ubuntu"]


def get_status():
    return {
        "status": "ok",
        "title": TITLE,
        "version": VERSION,
        "commit": GIT_SHA,
        "hostname": socket.gethostname(),
        "started_at": STARTED_AT.strftime("%d.%m.%Y %H:%M:%S"),
        "uptime_seconds": int(time.time() - START_TS),
    }


@app.route("/")
def index():
    done = sum(1 for lab in LABS if lab["done"])
    total = len(LABS)
    percent = round(done * 100 / total)
    circumference = 326.73
    max_hours = max(lab["hours"] for lab in LABS)
    return render_template(
        "index.html",
        title=TITLE,
        status=get_status(),
        labs=LABS,
        pipeline=PIPELINE,
        tech=TECH,
        done=done,
        total=total,
        percent=percent,
        dash=round(circumference * percent / 100, 1),
        circumference=circumference,
        max_hours=max_hours,
        total_hours=sum(lab["hours"] for lab in LABS),
    )


@app.route("/api/status")
def api_status():
    return jsonify(get_status())


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
