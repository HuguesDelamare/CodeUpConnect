from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime


from SQLAlchemy_main import session

from datetime import datetime


Model = declarative_base()
Model.query = session.query_property()


class TimeStampedModel(Model):
    __abstract__ = True

    creaeted_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())
