import tweepy
from config import create_api
from gpt2 import start_gpt2_sess,gpt_predict,tf_version
import time
from datetime import datetime


def run_model(prompt_text,api,mention):
    
    while True:
        try:
            text = gpt_predict(prompt_text.strip(), sess)
            break
        except:
            print("error generating text, Trying again")

    print(text)
    api.update_status(
                    status=text,
                    in_reply_to_status_id=mention._json['id'], 
                    auto_populate_reply_metadata=True,
                )
    
    
    
    return None

# def random_tweet(prompt_text,api):

#     return 

def answer_mentions(api, old_since_id):
    mentions = tweepy.Cursor(api.mentions_timeline, since_id=old_since_id).items() #returns tweet objects for all mentions since a certain id
    new_since_id = old_since_id

    for mention in mentions:
        if mention._json['id'] > new_since_id:
            new_since_id = mention._json['id']
        tweet_text = mention._json['text']
        prompt_text = tweet_text[12:]
        print(prompt_text)

        #Reply if the prompt is not in the right format
        if tweet_text[:11] != "@RoboTrump3": 
            api.update_status(
                    status="Sorry, I don't know how to handle that input. Please mention me in the front of the tweet. Tweet '@ tweetForThat1 help' for more help",
                    in_reply_to_status_id=mention._json['id'], 
                    auto_populate_reply_metadata=True,
            )

            continue
        
        ## If the user is prompting a support 
        if prompt_text.lower() == "help":
            api.update_status(
                    status="""To use me, send me a tweet with the phrase you'd like my tweet to start with.\n\nEx: '@ tweetForThat1 Great rally today!'""",
                    in_reply_to_status_id=mention._json['id'], 
                    auto_populate_reply_metadata=True,
                )
            continue
        
        #A proper prompt, this is where we run gpt-2
        else:
            run_model(prompt_text,api,mention) ##api.update_status is handled in this method
    


    
    return new_since_id



def main():
    api = create_api()

    old_since_id = 1201634058788384769 #tweet id to start from
    while True:
        print("Checking mentions ...")
        checking_tweets = tweepy.Cursor(api.mentions_timeline, since_id=old_since_id).items(1) #checks to see if the bot has recieved any new mentions
        tweet = list(checking_tweets)
        
        if len(tweet) == 0: #check if there is anything new tweet
            print("Nothing new")
        else:
            print("Some new tweets! Let's answer them.")
            old_since_id = answer_mentions(api, old_since_id) #the answer methods returns the id of the last mention answered so we can know where to start from in the next loop
            

        print("sleeping")
        time.sleep(15)
  
   

if __name__ == "__main__":
    print(tf_version())
    sess = start_gpt2_sess("trump_tune_small")
    last_tweet_time = datetime.now()
    main()
   