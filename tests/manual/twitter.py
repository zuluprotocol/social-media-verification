#!/usr/bin/env python3
import os

from services.twitter import TwitterClient

TWITTER_ACCOUNT_NAME = "[PUT TWITTER ACCOUNT NAME WITHOUT @]"
TWITTER_CONSUMER_KEY = "[PUT TWITTER APP KEY/CONSUMER KEY]"
TWITTER_CONSUMER_SECRET = "[PUT TWITTER APP SECRET/CONSUMER SECRET]"
TWITTER_ACCESS_TOKEN = "[PUT TWITTER USER ACCESS TOKEN"
TWITTER_ACCESS_SECRET = "[PUT TWITTER USER ACCESS SECRET]"

TWITTER_SEARCH_TEXT = f"I'm taking a ride with @{TWITTER_ACCOUNT_NAME}"

os.environ[
    "TWITTER_SECRET"
] = f"""{{
    "ACCOUNT_NAME": "{TWITTER_ACCOUNT_NAME}",
    "CONSUMER_KEY": "{TWITTER_CONSUMER_KEY}",
    "CONSUMER_SECRET": "{TWITTER_CONSUMER_SECRET}",
    "ACCESS_TOKEN": "{TWITTER_ACCESS_TOKEN}",
    "ACCESS_SECRET": "{TWITTER_ACCESS_SECRET}"
}}"""

twclient = TwitterClient(
    gcp_secret_name="TWITTER_SECRET",
)

if __name__ == "__main__":
    i = 0
    for tweet in reversed(list(twclient.search(TWITTER_SEARCH_TEXT))):
        i += 1
        print(f" ------ {i} {tweet}")
