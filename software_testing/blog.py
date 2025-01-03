import json


class Post:
    def __init__(self, title, author, content):
        self._title = title
        self._author = author
        self._content = content

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    def json(self) -> dict:
        return {
            'title': self.title,
            'author': self.author,
            'content': self.content
        }
