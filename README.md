# Chatbot RAG Platform

A platform for building a retrieval-augmented generation (RAG) chatbot. This repo currently
contains the project scaffolding — dev environment, CI, and a minimal runnable script — with
the RAG pipeline itself landing in upcoming work.

## Quick start

See [docs/setup.md](docs/setup.md) for full instructions. Short version:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
cp config/example.env .env
python3 src/main.py
```

## Project structure

```
src/      application code
tests/    automated tests (pytest)
docs/     setup and project documentation
config/   environment variable templates
```

## Development

- Lint: `ruff check .`
- Tests: `pytest`

Both run automatically via GitHub Actions on every pull request to `main`.
