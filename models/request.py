"""
This module have the model
for the request.
"""

from requests import get, post, put, delete

class Request:
    """
    Create a request object.
    """

    def __init__(self, url:str, method:str = 'get') -> None:
        self.url = url
        self.method = method

    def make(self, data:dict) -> str:
        """
        Make the request according
        to the method passed in the constructor.
        """

        # validating the method for make
        if self.method == 'get':
            request = get(self.url)
            try:
                return request.content.decode()
            except UnicodeDecodeError:
                return request.content

        elif self.method == 'post':
            request = post(self.url, data)

            try:
                return request.content

            except:
                # in case some problem with the response
                return request.content.decode()

        elif self.method == 'put':
            request = put(self.url, data)

            try:
                return request.content
            except:
                return request.content.decode()

        elif self.method == 'delete':
            del data
            request = delete(self.url)

            try:
                return request.content

            except:
                return request.content.decode()
