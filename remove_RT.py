#################################################################
# This python file takes a 1 column csv of tweet text and removes
# all tweets that start with "RT ". This removes most retweets from
# our corpus of tweets from the @realdonaldtrump twitter account.
# We do this because retweets do not capture the gramatical structure
# and vocabulary used by the account. Including them would muddle 
# our data.   
################################################################

import csv

tweets_minus_rt = []
rt = []
count = 0
with open("tweet_text.csv", encoding='utf8') as tweets:
    reader = csv.reader(tweets)
    for row in reader:
        count = count + 1
        if row[0][:3] == "RT ":
            rt.append(row[0])
        else:
            tweets_minus_rt.append(row[0])

print(f'Total tweets: {count}') #Print of the total number of tweets
print(f'Tweets minus retweets: {len(tweets_minus_rt)}') #Print of the number of tweets minus retweets
print(f'Retweets: {len(rt)}') #Print of the number of rts in the corpus

print('Removing writing tweets (not retweets) to tweet_text_minus_rt.csv')

with open("tweet_text_minus_rt.csv", encoding="utf8", mode='w', newline='') as new_csv:
    writer = csv.writer(new_csv)
    for tweet in tweets_minus_rt:
        writer.writerow([tweet])

print("Done!")