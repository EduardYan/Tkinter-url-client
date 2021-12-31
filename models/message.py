"""
This module have the class Message
for have a model of message.
"""

class Message:
    """
    Create a message with a content
    """

    def __init__(self, content:str) -> None:
        self.content = content

    def __str__(self) -> str:
        return self.content
