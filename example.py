import tweepy
import keys
import os

# V1 Twitter API Authentication
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 Twitter API Authentication
client = tweepy.Client(
    keys.bearer_token,
    keys.api_key,
    keys.api_secret,
    keys.access_token,
    keys.access_token_secret,
    wait_on_rate_limit=True,
)

# Get the full path of the image file
image_path = os.path.join(os.path.dirname(__file__), 'regular_weather.png')

# Upload image to Twitter (without tweeting)
media_id = api.media_upload(filename=image_path).media_id_string
print(media_id)

# Text to be tweeted
message = 'Hello World!'

# Post the tweet with text and image media ID
client.create_tweet(text=message, media_ids=[media_id])
print('Tweeted!')
