"""
Terminal interface for the Simple Q&A Chatbot.
Users can interact with the chatbot directly
from the Ubuntu terminal.
"""

from chatbot.bot import create_chatbot, get_response
def display_banner():
    """Display the chatbot application banner."""
    print("\n" + "=" * 75)

    print(
        "                 SIMPLE Q&A CHATBOT"
    )

    print(
        "                 PYTHON + CHATTERBOT"
    )

    print("=" * 75)

    print("\nWelcome! I am your virtual assistant.")

    print("\nAvailable commands:")

    print("  exit   - End the conversation")
    print("  quit   - Close the chatbot")
    print("  help   - Display usage instructions")

    print("\n" + "-" * 75)


def run_chat():
    """Start and manage the chatbot conversation."""
    display_banner()
    # Initialize the chatbot engine.
    bot = create_chatbot()
    print("\nBot: Hello! How can I help you today?")
    while True:
        try:
            # Read input from the user.
            user_message = input("\nUser: ").strip()
            # Prevent empty messages.
            if not user_message:
                print(
                    "Bot: Please enter a message before continuing."
                )
                continue
            # Handle exit commands.
            if user_message.lower() in ["exit", "quit", "bye"]:
                print(
                    "\nBot: Goodbye! Thank you for chatting with me."
                )
                break
            # Display instructions.
            if user_message.lower() == "help":

                print("\nBot: You can ask me simple questions.")

                print("Type 'exit' or 'quit' to end the conversation.")

                continue

            # Generate the chatbot response.
            response = get_response(
                bot,
                user_message
            )

            print(f"\nBot: {response}")

        except KeyboardInterrupt:

            print(
                "\n\nBot: Chat interrupted. Goodbye!"
            )

            break

        except EOFError:

            print(
                "\n\nBot: Input stream closed. Goodbye!"
            )

            break

        except Exception as error:

            # Display a friendly message instead of crashing.
            print(
                "\nBot: Sorry, I encountered an error."
            )

            print(
                f"Technical details: {error}"
            )


if __name__ == "__main__":

    run_chat()

