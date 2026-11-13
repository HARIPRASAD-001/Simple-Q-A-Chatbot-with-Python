
"""
Django management command for starting the chatbot.

Usage:
    python manage.py chat
"""

from django.core.management.base import BaseCommand

from chatbot.terminal import run_chat


class Command(BaseCommand):

    help = "Start the Simple Q&A Chatbot terminal application."

    def handle(self, *args, **options):

        self.stdout.write(
            self.style.SUCCESS(
                "Starting the Simple Q&A Chatbot..."
            )
        )

        run_chat()

