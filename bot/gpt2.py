import gpt_2_simple as gpt2
import tensorflow as tf
import random

def tf_version(): #checks the version of tensorflow
    print("We need to use a tensorflow version <2.0")
    return tf.__version__


def start_gpt2_sess(run_name): #Starts the session. Needs a run stored in the checkpoint folder. This is our "trump_tune_small" folder
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name=run_name)
    return sess

def shorten_output(text):
  #distribution = [1,1,1,1,1,1,1,1,1,1,1,2,2,2,3] #73 percent chance of selecting a tweet thread of length 1. 20 percent of length 2. ~7 percent for 3
  distribution = [1] #torching the tweet threading for now 
  max_tweet_length = int(280*random.choice(distribution)) #Sets the max length our generated text can be given a determined number of tweets in the thread
  random_length_generator = random.randrange(70) #We don't want our tweets to always fill all 280 characters so we add a little more randomness to the length

  return text[:max_tweet_length-random_length_generator] 

def remove_outbound_links_and_blank_tokens(text):
  token_list = text.split(" ")

  for index,token in enumerate(token_list):  
    if token[:12] == "https://t.co" or token[:11] == "http://t.co":
      token_list.pop(index) #removes outbound links
    elif token == "":
      token_list.pop(index) #removes blank tokens
    elif token == "&amp;": #output not recognizing ampersand
      token_list[index] = "&"

  return token_list

def remove_hanging_clause(token_list): #Makes sure the tweet ends in a full sentence
  latest_terminator_index = 0
  #print(token_list)
  for index,token in enumerate(token_list): 
    if token[-1] == "." or token[-1] == "!": #checks to see if a word ends in a terminator, used to keep the tweet to full sentences
      latest_terminator_index = index

  #print(latest_terminator_index)
  shorten_tokens = token_list[:latest_terminator_index+1]
  return " ".join(shorten_tokens)

def gpt_predict(prompt,sess):

  gen_text = gpt2.generate(sess, length=200, temperature=0.7, prefix=prompt, run_name='trump_tune_small', return_as_list=True)[0]

  text_minus_tags = str(gen_text).replace("<|endoftext|>","").replace("<|startoftext|>", "") #remove text artifacts from gpt-2 output

  short_tweet_text = shorten_output(text_minus_tags) #shorten output of GPT-2 into a useable tweet length 
  short_tweet_tokens = remove_outbound_links_and_blank_tokens(short_tweet_text) #remove any outbound links
  short_tweet_text_no_clause = remove_hanging_clause(short_tweet_tokens) #remove text at the end that does not form a whole sentence


  return short_tweet_text_no_clause
