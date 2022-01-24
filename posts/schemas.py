from datetime import datetime
from ninja import Schema


class PostInSchema(Schema):
    title: str
    content: str


class PostOutSchema(Schema):
    title: str
    content: str
    date_created: datetime


class Message(Schema):
    message: str
