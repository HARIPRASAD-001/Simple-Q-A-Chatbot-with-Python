
"""
Main chatbot engine.

This module:
1. Initializes ChatterBot.
2. Configures SQLite storage.
3. Trains the bot using sample conversations.
4. Provides a function for generating responses.
"""

from pathlib import Path

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Determine the project directory.
BASE_DIR = Path(__file__).resolve().parent.parent

# Store chatbot knowledge in a persistent SQLite database.
CHATBOT_DATABASE = BASE_DIR / "chatbot.sqlite3"


# Sample conversations used to train the chatbot.
TRAINING_CONVERSATIONS = [

    [
        "Hello",
        "Hello! How can I help you today?",
        "I would like to know more about you.",
        "I am a simple Python chatbot designed to answer questions.",
        "Thank you.",
        "You are welcome!"
    ],

    [
        "Good morning!",
        "Good morning! How are you doing?",
        "I am doing very well, thank you for asking.",
        "You're welcome.",
        "Do you like hats?",
        "Yes, hats can be interesting fashion accessories."
    ],

    [
        "How are you?",
        "I am doing very well, thank you for asking.",
        "That is good to hear.",
        "Thank you! How can I assist you today?"
    ],

    [
        "What is your name?",
        "My name is ChatBot. I am your virtual assistant.",
        "Who created you?",
        "I was created using Python and the ChatterBot library."
    ],

    [
        "What is Python?",
        "Python is a high-level programming language known for its simplicity and readability.",
        "What is Django?",
        "Django is a Python web framework used for building web applications."
    ],

    [
        "What is artificial intelligence?",
        "Artificial intelligence is the ability of computer systems to perform tasks that normally require human intelligence.",
        "Can you learn?",
        "Yes. ChatterBot can learn from conversational examples and interactions."
    ],

    [
        "What can you do?",
        "I can respond to questions and participate in simple conversations.",
        "Can you help me with programming?",
        "Yes. I can answer some basic programming questions."
    ],

    [
        "Thank you",
        "You are most welcome!",
        "Goodbye",
        "Goodbye! Have a wonderful day."
    ],

    [
        "How old are you?",
        "I am a computer program, so I do not have a human age.",
        "Where do you live?",
        "I exist as a Python application running on your computer."
    ],

    [
        "What is machine learning?",
        "Machine learning is a branch of artificial intelligence that enables computers to learn patterns from data.",
        "What is a chatbot?",
        "A chatbot is a software application designed to communicate with users through conversation."
    ]
]


def create_chatbot():
    """
    Create and initialize the ChatterBot instance.

    Training is performed only when the chatbot database
    does not contain previously stored statements.
    """

    bot = ChatBot(
        name="Simple Q&A Assistant",

        storage_adapter=(
            "chatterbot.storage.SQLStorageAdapter"
        ),

        database_uri=(
            f"sqlite:///{CHATBOT_DATABASE.as_posix()}"
        ),

        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch"
            }
        ],

        read_only=False
    )

    # Avoid adding the same training conversations every time
    # the application starts.
    if bot.storage.count() == 0:

        print("\nInitializing chatbot knowledge...")

        trainer = ListTrainer(bot)

        for conversation in TRAINING_CONVERSATIONS:

            trainer.train(conversation)

        print("Chatbot training completed successfully.")

    return bot


def get_response(bot, user_message):
    """
    Generate a response to a user message.

    Args:
        bot: Initialized ChatterBot instance.
        user_message: Text entered by the user.

    Returns:
        String containing the chatbot response.
    """

    response = bot.get_response(user_message)

    return str(response)

