import tweepy 


def create_api():

    auth = tweepy.OAuthHandler(api_key,api_secret_key)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        print("Error creating API")
        raise e
    print("API created")

    return api