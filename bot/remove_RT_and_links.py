#################################################################
# This python file takes a 1 column csv of tweet text and removes
# all tweets that start with "RT ". This removes most retweets from
# our corpus of tweets from the @realdonaldtrump twitter account.
# We do this because retweets do not capture the gramatical structure
# and vocabulary used by the account. Including them would muddle 
# our data.   
#
# Retweets come into the data in two forms. Either the tweet starts 
# with "RT " or it comes as "@handle: ". This script removes both.
################################################################

#################################################################
# This file also removes outbound links from the tweets. When 
# testing a few finetuned models, links were coming through.
# While it would be cool for this bot to include links the 
# @realdonaldtrump account used, most of the links were broken. 
# Adding working links to the bot could be a fun next step in the
# future. 
#################################################################

import csv

tweets_minus_rt = []
rt = []
count = 0
with open("tweet_text.csv", encoding='utf8') as tweets:
    reader = csv.reader(tweets)
    for row in reader:
        count = count + 1
        stripped_string = row[0].strip() #some of the tweets come in with an errant space in the front of the csv row. This removes that
        tokens = stripped_string.split(" ")  #tokenizes the string for more efficient removal of retweets and links
        if tokens[0] == "RT": #
            rt.append(stripped_string)
        elif tokens[0][0] == "@" and tokens[0][-1] == ":":
            rt.append(stripped_string)
        else:
            for index,token in enumerate(tokens):
                if token[:12] == "https://t.co" or token[:11] == "http://t.co":
                    tokens.pop(index)
            recomb = " ".join(tokens)
            tweets_minus_rt.append(recomb)
print(f'Total tweets: {count}') #Print of the total number of tweets
print(f'Tweets minus retweets: {len(tweets_minus_rt)}') #Print of the number of tweets minus retweets
print(f'Retweets: {len(rt)}') #Print of the number of rts in the corpus

print('Writing tweets (not retweets) to tweet_text_minus_rt.csv')

with open("tweet_text_minus_rt.csv", encoding="utf8", mode='w', newline='') as new_csv:
    writer = csv.writer(new_csv)
    for tweet in tweets_minus_rt:
        if tweet != "":
            writer.writerow([tweet])

print("Done!")


