import tweepy
import logging
from secrets import secrets

logger = logging.getLogger()

def create_client():
    try:
        client = tweepy.Client(
        consumer_key = secrets.get('API_KEY'),
        consumer_secret = secrets.get('API_SECRET'),
        access_token = secrets.get('ACCESS_TOKEN'),
        access_token_secret = secrets.get('ACCESS_TOKEN_SECRET')
        )
    except Exception as e:
        logger.error("Error creating API client", exc_info=True)
        raise e
    logger.info("API client created")
    return client