import tweepy 
from keys import set_keys


def create_api():
    keys = set_keys()

    auth = tweepy.OAuthHandler(keys['api_key'],keys['api_secret_key'])
    auth.set_access_token(keys['access_token'],keys['access_token_secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        print("Error creating API")
        raise e
    print("API created")

    return api