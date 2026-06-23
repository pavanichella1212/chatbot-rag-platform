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

This installs dev tools (pytest, ruff). There are no runtime dependencies yet —
`src/main.py` is plain Python with nothing to install to run it.

## 4. Configure environment variables

```bash
cp config/example.env .env
```

Nothing reads this yet — it's a placeholder for settings future features will need.

## 5. Run the app

```bash
python3 src/main.py
```

You should see:

```
Chatbot RAG Platform is running
status: ok
```

## 6. Run lint and tests

```bash
ruff check .
pytest
```

Both should pass with no errors. This is exactly what CI runs on every pull request.

## Troubleshooting

- **`command not found: python3`** — install Python 3.11+ from [python.org](https://www.python.org/downloads/).
- **Import errors when running pytest** — make sure your virtual environment is activated and you ran `pip install -r requirements-dev.txt` from the project root.
