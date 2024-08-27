import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    bio = Column(String(250))
    profile_picture = Column(String(250))
    stories = relationship("Story")
    followers = relationship("Follower", foreign_keys='Follower.user_from_id')
    followings = relationship("Follower", foreign_keys='Follower.user_to_id')
    reels = relationship("Reel")
    messages_sent = relationship("Message", foreign_keys='Message.sender_id')
    messages_received = relationship("Message", foreign_keys='Message.receiver_id')
    posts = relationship("Post")
    comments = relationship("Comment")
    likes = relationship("Like")

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(String(250))
    video_url = Column(String(250))
    image_url = Column(String(250))
    user = relationship("User")

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_from = relationship("User")
    user_to = relationship("User")

class Reel(Base):
    __tablename__ = 'reel'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    video_url = Column(String(250))
    caption = Column(String(250))
    user = relationship("User")

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('user.id'))
    receiver_id = Column(Integer, ForeignKey('user.id'))
    content = Column(String(250))
    sender = relationship("User")
    receiver = relationship("User")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    video_url = Column(String(250))
    image_url = Column(String(250))
    caption = Column(String(250))
    user = relationship("User")
    comments = relationship("Comment")
    likes = relationship("Like")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(String(250))
    post = relationship("Post")
    user = relationship("User")

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    post = relationship("Post")
    user = relationship("User")


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
