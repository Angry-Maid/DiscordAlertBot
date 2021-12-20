from datetime import datetime
from contextlib import contextmanager

import yaml
from sqlalchemy import (
    create_engine, Column, Integer,
    String, DateTime
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


__all__ = [
    'session_scope'
    'Base',
    'Record',
]


with open('config.yaml') as cfile:
    config = yaml.load(cfile, Loader=yaml.CLoader)


Base = declarative_base()


class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    username = Column(String(512))
    command = Column(String(256))
    message = Column(String(4096))
    created_at = Column(DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Message(id={}, username={}, command={})>'.format(
            self.id, self.username, self.command
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'command': self.command,
            'message': self.message,
            'created_at': self.created_at.strftime('%d %b %Y %H:%M:%S')
        }


engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(
    config['PG_USER'], config['PG_PASSWORD'],
    config['PG_URL'], config['PG_DB']
))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
