import os 

###########################################################
# In order for this file to work, you
# need to set the four credential variables in your
# shell environment
# 
# "set [variable_name]=[variable_value]" in command prompt
###########################################################

# os.environ.get('[env_variable_name]')

def set_keys():
    api_key = os.environ.get('trump_bot_api_key')
    api_secret_key = os.environ.get('trump_bot_api_secret_key')

    access_token = os.environ.get('trump_bot_access_token')
    access_token_secret = os.environ.get('trump_bot_access_token_secret')

    print(f"api_key: {api_key}")
    print(f"api_secret_key: {api_secret_key}")
    print(f"access_token: {access_token}")
    print(f"access_token_secret: {access_token_secret}")

    keys = {
        "api_key": api_key,
        "api_secret_key": api_secret_key,
        "access_token": access_token,
        "access_token_secret": access_token_secret
    }

    return keys