
# reddit post table

# app/models/post.py

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.database import Base
from datetime import datetime, timezone
from sqlalchemy import Text

class Post(Base):
    __tablename__ = 'reddit_posts'

    id = Column(String(100), primary_key=True, index=True)
    title = Column(String(300))
    author = Column(String(100))
    subreddit = Column(String(100))
    score = Column(Integer)
    num_comments = Column(Integer)
    url = Column(String(500))
    is_self = Column(Boolean)  # True = text post, False = link
    content = Column(Text)  # full text of the post
    created_utc = Column(DateTime, default=lambda: datetime.now(timezone.utc))
