import tweepy
import requests
import time
import os
import keys
import random

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

# Set different locations
LOCATIONS = {
    "AUSTRIA": ["Vienna, AT", "Graz, AT"],
    "BELGIUM": ["Brussels, BE", "Antwerp, BE"],
    "BULGARIA": ["Sofia, BG", "Plovdiv, BG"],
    "CROATIA": ["Zagreb, HR", "Split, HR"],
    "CYPRUS": ["Nicosia, CY", "Limassol, CY"],
    "CZECH REPUBLIC": ["Prague, CZ", "Brno, CZ"],
    "DENMARK": ["Copenhagen, DK", "Aarhus, DK"],
    "ESTONIA": ["Tallinn, EE", "Tartu, EE"],
    "FINLAND": ["Helsinki, FI", "Espoo, FI"],
    "FRANCE": ["Paris, FR", "Marseille, FR"],
    "GERMANY": ["Berlin, DE", "Hamburg, DE"],
    "GREECE": ["Athens, GR", "Thessaloniki, GR"],
    "HUNGARY": ["Budapest, HU", "Debrecen, HU"],
    "IRELAND": ["Dublin, IE", "Cork, IE"],
    "ITALY": ["Rome, IT", "Milan, IT"],
    "LATVIA": ["Riga, LV", "Daugavpils, LV"],
    "LITHUANIA": ["Vilnius, LT", "Kaunas, LT"],
    "LUXEMBOURG": ["Luxembourg, LU"],
    "MALTA": ["Valletta, MT"],
    "NETHERLANDS": ["Amsterdam, NL", "Rotterdam, NL"],
    "POLAND": ["Warsaw, PL", "Krakow, PL"],
    "PORTUGAL": ["Lisbon, PT", "Porto, PT"],
    "ROMANIA": ["Bucharest, RO", "Cluj-Napoca, RO"],
    "SLOVAKIA": ["Bratislava, SK", "Košice, SK"],
    "SLOVENIA": ["Ljubljana, SI", "Maribor, SI"],
    "SPAIN": ["Madrid, ES", "Barcelona, ES"],
    "SWEDEN": ["Stockholm, SE", "Gothenburg, SE"]
}

# Set different images
IMAGES = ['cold_weather.png', 'regular_weather.png', 'hot_weather.png']

# Define the global variable through where images are going to be uploaded
media_ids = []

# Function that uploads the different images
def upload_images(api: tweepy.Client) -> None and str:
    # Get the full path of the image file and upload image to Twitter (without tweeting)
        global media_ids  # Create an empty list to store media IDs
        for image in IMAGES:
            image_path = os.path.join(os.path.dirname(__file__), image)
            media_upload = api.media_upload(filename=image_path)
            media_id = media_upload.media_id_string
            media_ids.append(media_id)  # Append each media ID to the list
        return media_id

# Function that gets the data and tweets
def get_weather_and_tweet(city: str) -> None and str:
    try:
        # Get data from OpenWeatherMap
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={keys.api_key_openweather}&units=metric'
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']

        # Text prompt for the tweet
        message = f"Today's weather in {city[:-4]}: {weather}. Temperature: {temperature:.2f}°C"

        # Post the tweet with text and image media ID 
        if temperature < 19:
            media_id = media_ids[0]  # Cold weather image
        elif 19 <= temperature < 26.5:
            media_id = media_ids[1]  # Regular weather image
        else:
            media_id = media_ids[2]  # Hot weather image           
        
        client.create_tweet(text=message, media_ids=[media_id])
        print(f"Tweeted successfully for {city}! :D")
    
    # Exception and error handling
    except (requests.RequestException, tweepy.TweepyException) as e:
        print(f"An error occurred for {city}: {str(e)}")
    except (KeyError, IndexError):
        print(f"Error processing weather data for {city}")
    except Exception as e:
        print(f"An unexpected error occurred for {city}: {str(e)}")

if __name__ == '__main__':
    country_selected = random.choice(list(LOCATIONS.items()))
    client.create_tweet(text=f'Country selected for the day: {country_selected[0]}!')
    print(f'Country selected for the day: {country_selected[0]}!')
    
    if len(country_selected[1]) == 1:
        upload_images(api)
        get_weather_and_tweet(country_selected[1][0])
    else:
        upload_images(api)
        get_weather_and_tweet(country_selected[1][0])
        time.sleep(20)
        get_weather_and_tweet(country_selected[1][1])
        