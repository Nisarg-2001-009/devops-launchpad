import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "1.0.0"


@app.route("/")
def home():
    return "<h1>DevOps Portfolio Launchpad</h1><p>Flask app is running.</p>"


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "devops-launchpad"})


@app.route("/info")
def info():
    return jsonify({
        "version": APP_VERSION,
        "environment": os.getenv("FLASK_ENV", "development"),
        "python_path": os.getenv("PYTHONPATH", ""),
    })


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV", "development") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
