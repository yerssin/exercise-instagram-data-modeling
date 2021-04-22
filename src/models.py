import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table posts.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class History(Base):
    __tablename__ = 'history'
    # Here we define columns for the table history
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table media
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('posts.id'))


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table comment
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    autor_id = Column(Integer, ForeignKey('user.id'))
    user_id = Column(Integer, ForeignKey('posts.id'))
    comment_text = Column(String(250))

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
