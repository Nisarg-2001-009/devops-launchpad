# DevOps Portfolio Launchpad

A minimal Python Flask web application serving as the foundation for a DevOps portfolio project. It demonstrates a production-ready app structure suitable for containerization, CI/CD pipelines, and cloud deployment.

## Routes

| Route | Description |
|-------|-------------|
| `GET /` | Home page |
| `GET /health` | JSON health check — suitable for load balancer probes |
| `GET /info` | App version and runtime environment details |

## Getting Started

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app runs on `http://localhost:5000` by default.

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `5000` | Port the server listens on |
| `FLASK_ENV` | `development` | Set to `production` to disable debug mode |

## Project Structure

```
devops-launchpad/
├── app.py            # Flask application
├── requirements.txt  # Python dependencies
├── .gitignore        # Git ignore rules
└── README.md         # This file
```
