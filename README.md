# Simple Q&A Chatbot Using Python, Django, and ChatterBot

## 1. Project Overview

This project implements a simple Question-and-Answer (Q&A) chatbot using Python, Django, and the ChatterBot library. The application allows users to interact with a chatbot through a terminal interface by submitting questions and receiving responses based on previously trained conversational data.

ChatterBot handles conversational training, response matching, and storage, while Django provides the project structure and a custom management command for launching the chatbot.

The chatbot is trained using predefined conversational sequences covering greetings, general conversations, and basic programming concepts, including Python and Django.

## 2. Project Objectives

The main objectives of this project are to:

- Develop a functional question-and-answer chatbot using Python.
- Integrate the ChatterBot library for conversational processing.
- Train the chatbot using predefined conversational datasets.
- Use SQLite for persistent conversational storage.
- Organize the application using Django.
- Implement a terminal interface for user interaction.
- Provide commands for help and conversation termination.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Project organization and management commands |
| ChatterBot | Chatbot functionality and response matching |
| SQLite | Persistent conversational storage |
| ListTrainer | Training the chatbot using conversational sequences |
| BestMatch | Matching user input with stored conversational knowledge |

## 4. Project Structure

The project is organized as follows:

```text
simple_qa_chatbot/
│
├── manage.py
├── requirements.txt
│
├── chatbot_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── chatbot/
    ├── __init__.py
    ├── apps.py
    ├── bot.py
    ├── terminal.py
    │
    └── management/
        ├── __init__.py
        │
        └── commands/
            ├── __init__.py
            └── chat.py
```

### Main Files and Their Responsibilities

**manage.py:** Provides the Django command-line interface used to execute the chatbot.

**requirements.txt:** Contains the Python dependencies required to run the project.

**chatbot_project/settings.py:** Contains Django project configuration, including installed applications and database settings.

**chatbot_project/urls.py:** Defines the Django URL configuration.

**chatbot/apps.py:** Configures the chatbot Django application.

**chatbot/bot.py:** Initializes the ChatterBot instance, configures storage and response matching, and trains the chatbot using predefined conversations.

**chatbot/terminal.py:** Handles terminal interaction, user input, chatbot responses, and conversation termination.

**chatbot/management/commands/chat.py:** Defines the custom Django management command used to launch the chatbot.

**SQLite database:** Stores the chatbot's conversational information. Its exact filename and location depend on the database URI configured in `bot.py`.

## 5. Requirements

Before running the project, ensure that the following are installed:

- Python 3.10 or later, subject to the compatibility requirements of the installed ChatterBot release.
- pip (Python package installer).
- Django.
- ChatterBot.

The project dependencies are defined in `requirements.txt`:

```text
Django
chatterbot
```

## 6. Installation and Setup

### Step 1: Clone or Download the Project

Download the project files and navigate to the project directory.

```bash
cd simple_qa_chatbot
```

### Step 2: Create a Virtual Environment

It is recommended to use a virtual environment to isolate project dependencies.

```bash
python3 -m venv venv
```

Activate the environment on Linux:

```bash
source venv/bin/activate
```

### Step 3: Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Step 4: Install Dependencies

Install the required packages using:

```bash
pip install -r requirements.txt
```

Verify the installations:

```bash
python -m django --version
```

```bash
python -m pip show chatterbot
```

## 7. Running the Application

After installing the dependencies, navigate to the directory containing `manage.py`.

Start the chatbot using:

```bash
python manage.py chat
```

The application initializes the chatbot and checks whether conversational training data already exists in its storage.

If the database is empty, the chatbot processes the predefined training conversations. After training is completed, the terminal displays a welcome message and waits for user input.

**Example startup command:**

```bash
python manage.py chat
```

## 8. Using the Chatbot

Once the chatbot starts, users can enter questions or conversational statements in the terminal.

### Example Conversation

```text
============================================================
              SIMPLE Q&A CHATBOT
============================================================

Chatbot: Hello! How can I help you today?

You: Good morning! How are you doing?

Chatbot: I am doing very well, thank you for asking.

You: What is Python?

Chatbot: Python is a high-level programming language
known for its simplicity and readability.

You: What is Django?

Chatbot: Django is a Python web framework used for
building web applications.

You: exit

Chatbot: Goodbye! Thank you for chatting with me.
```

*Note: The example illustrates the expected interaction based on the project's tested responses.*

### Available Commands

| Command | Description |
|---|---|
| `help` | Displays available chatbot commands |
| `exit` | Terminates the conversation |
| `quit` | Terminates the conversation |
| `bye` | Ends the conversation, if supported by the terminal handler |

Users can also enter ordinary questions to receive responses from the chatbot.

## 9. Chatbot Training

The chatbot uses ChatterBot's `ListTrainer` to learn from predefined conversational sequences.

Training data is maintained in `chatbot/bot.py`. The conversations include greetings, general questions, and programming-related information.

For example, a training sequence may contain:

```python
conversation = [
    "What is Python?",
    "Python is a high-level programming language known for its simplicity and readability."
]
```

The ListTrainer processes conversational statements and stores the learned information in the configured SQLite database.

The project checks the existing storage before training. This prevents the same initial training process from being repeated unnecessarily whenever the chatbot starts.

To expand the chatbot's knowledge, additional conversational sequences can be added to the training data in `bot.py`.

## 10. Database and Storage

The application uses SQLite through ChatterBot's `SQLStorageAdapter` to maintain conversational information.

The database provides persistent storage, allowing previously trained information to remain available between application sessions.

The database is managed by ChatterBot independently of Django's default ORM database configuration.

If the chatbot is not returning expected responses after changes to the training data, inspect the configured SQLite database and training initialization logic. Resetting the database may require retraining the chatbot, but existing conversational records will be lost.

## 11. Testing the Application

The following tests can be performed to verify the chatbot's functionality:

| Test Case | Input | Expected Result |
|---|---|---|
| Greeting | `Good morning! How are you doing?` | Returns a greeting response |
| Python question | `What is Python?` | Provides a description of Python |
| Django question | `What is Django?` | Provides a description of Django |
| Help command | `help` | Displays available commands |
| Exit command | `exit` | Displays goodbye message and terminates the session |

### Observed Test Results

The implementation was successfully executed using:

```bash
python manage.py chat
```

The application initialized successfully, processed ten predefined conversational sequences during its initial training, and generated the expected responses to the tested greeting, Python, and Django questions.

The exit command also worked correctly, allowing the user to terminate the conversation.

These results demonstrate successful basic functionality but do not represent a formal chatbot accuracy evaluation.

## 12. Troubleshooting

### Issue 1: ModuleNotFoundError

If Python reports that a module cannot be found, install the project dependencies:

```bash
pip install -r requirements.txt
```

Also confirm that the correct virtual environment is activated.

### Issue 2: Django Command Not Found

If Django does not recognize the `chat` command, confirm that the custom management command exists at:

```text
chatbot/management/commands/chat.py
```

Ensure that the `chatbot` application is included in `INSTALLED_APPS` in `settings.py`.

### Issue 3: Database or Storage Errors

If the application reports SQLite storage errors, verify that the configured database path is valid and that the application has permission to write to its parent directory.

### Issue 4: Unexpected Chatbot Responses

The chatbot's responses depend on its stored conversational information. Add more training sequences to `bot.py` to improve its coverage of different questions.

### Issue 5: Dependency Compatibility

If dependency installation fails, check the installed Python version and the compatibility requirements of Django and ChatterBot. Use a supported Python version and install the dependencies in a clean virtual environment.

## 13. Limitations

This project is a basic conversational chatbot intended for educational purposes. Its responses are limited by the conversational information supplied during training. It does not have unrestricted internet access or the broad general knowledge of advanced large language models.

The terminal interface also limits the application to command-line interaction. The current implementation does not provide a graphical user interface, user authentication, or multi-user conversation management.

## 14. Future Improvements

The project can be extended in several ways. Additional training data could be introduced to support a wider range of questions and conversational topics. A Django web interface could also be developed to allow users to interact with the chatbot through a browser.

Other possible improvements include implementing better input normalization, adding conversation history, introducing user-specific sessions, and evaluating response quality using a larger test dataset.

