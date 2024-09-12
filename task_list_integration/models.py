from peewee import *
from database import db

class BaseModel(Model):
    class Meta:
        database = db

class Message(BaseModel):
    action = CharField()
    number = CharField()
    message = TextField()
    status = CharField()

    class Meta:
        table_name = 'messages'