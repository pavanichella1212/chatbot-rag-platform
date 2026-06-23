from src.main import get_status, get_welcome_message


def test_get_welcome_message() -> None:
    assert get_welcome_message() == "Chatbot RAG Platform is running"


def test_get_status_returns_ok() -> None:
    assert get_status() == "ok"
