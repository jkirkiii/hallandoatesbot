import tweepy
import logging
from config import create_client
from fileReader import get_lines
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    client = create_client()
    lines = get_lines()
    for line in lines:
        logger.info('Sending tweet')
        client.create_tweet(text=f'{line}')
        time.sleep(60)
    
if __name__ == "__main__":
    main()