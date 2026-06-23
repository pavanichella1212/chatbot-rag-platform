def get_welcome_message() -> str:
    # Just returns a plain piece of text — no web, no network, nothing fancy
    return "Chatbot RAG Platform is running"


def get_status() -> str:
    # Stands in for "is everything okay" — for now it's always "ok"
    return "ok"


def main() -> None:
    # Calls the two functions above and prints their results to the screen
    print(get_welcome_message())
    print(f"status: {get_status()}")


if __name__ == "__main__":
    # Only runs main() if this exact file is executed directly (python3 src/main.py)
    # Does NOT run when this file is just imported elsewhere (e.g., by our tests)
    main()
