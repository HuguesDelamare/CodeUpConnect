from .base import TimeStampedModel
from sqlalchemy import Column, Integer, String


class User(TimeStampedModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), nullable=False, unique=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.username} {self.email}"