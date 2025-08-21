# fetch data from Reddit and save to database
# app/scripts/fetch_posts.py

from app.reddit_connector import get_reddit_instance
print("get_reddit_instance:", get_reddit_instance)

from app.database import SessionLocal
from app.models.post import Post
from datetime import datetime, timezone

subreddits = [
    'nigeria', 'technology', 'datascience', 'machinelearning',
    'programming', 'worldnews', 'AskReddit', 'finance', 'Futurology'
]

def fetch_and_save(subreddit_name, limit=50):
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)

    db = SessionLocal()

    for submission in subreddit.hot(limit=limit):
        if db.query(Post).filter(Post.id == submission.id).first():
            continue  # avoid duplicates

        post = Post(
            id=submission.id,
            title=submission.title,
            author=str(submission.author),
            score=submission.score,
            num_comments=submission.num_comments,
            subreddit=subreddit_name,
            url=submission.url,
            is_self=submission.is_self,
            content=submission.selftext if submission.is_self else None,
            created_utc=datetime.fromtimestamp(submission.created_utc, timezone.utc)
        )

        db.add(post)
        db.commit()

    db.close()

def fetch_and_save_all():
    for sub in subreddits:
        print(f"Fetching posts from r/{sub}...")
        fetch_and_save(subreddit_name=sub, limit=50)
    print("Done fetching posts from all subreddits.")

if __name__ == '__main__':
    fetch_and_save_all()
