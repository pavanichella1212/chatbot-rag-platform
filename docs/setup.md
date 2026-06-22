# Setup Guide

Get the project running locally in under 15 minutes.

## Prerequisites

- Python 3.11 or newer (`python3 --version`)
- Git

## 1. Clone the repo

```bash
git clone https://github.com/pavanichella1212/chatbot-rag-platform.git
cd chatbot-rag-platform
```

## 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements-dev.txt
```

This installs runtime dependencies (FastAPI, Uvicorn) plus dev tools (pytest, ruff, httpx).
If you only need to run the app (no testing/linting), `pip install -r requirements.txt` is enough.

## 4. Configure environment variables

```bash
cp config/example.env .env
```

The defaults work out of the box for local development — no values need to be filled in yet.

## 5. Run the app

```bash
uvicorn src.main:app --reload
```

Visit http://localhost:8000/health — you should see:

```json
{"status": "ok"}
```

## 6. Run lint and tests

```bash
ruff check .
pytest
```

Both should pass with no errors. This is exactly what CI runs on every pull request.

## Troubleshooting

- **`command not found: python3`** — install Python 3.11+ from [python.org](https://www.python.org/downloads/).
- **Port 8000 already in use** — run `uvicorn src.main:app --reload --port 8001` instead.
- **Import errors when running pytest** — make sure your virtual environment is activated and you ran `pip install -r requirements-dev.txt` from the project root.
