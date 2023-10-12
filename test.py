import requests
import time
import keys

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

for country, cities_list in LOCATIONS.items():
        for city in cities_list:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={keys.api_key_openweather}&units=metric'
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            print(weather, city)
            time.sleep(10)

#url = f'https://api.openweathermap.org/data/2.5/weather?q={"Luxembourg, LU"}&appid={keys.api_key_openweather}&units=metric'
#response = requests.get(url)
#response.raise_for_status()  # Raise an exception for HTTP errors
#data = response.json()
#weather = data['weather'][0]['description']
#temperature = data['main']['temp']
#print(weather)

# Full spam
#for country, cities_list in LOCATIONS.items():
#        for city in cities_list:
#            try:   
#                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={keys.api_key_openweather}&units=metric'
#                response = requests.get(url)
#                response.raise_for_status()  # Raise an exception for HTTP errors
#                data = response.json()
#                weather = data['weather'][0]['description']
#                temperature = data['main']['temp']
#
#                message = f"Today's weather in {city[:-4]}: {weather}. Temperature: {temperature:.2f}°C"
#                    
#                client.create_tweet(text=message)
#                print(f"Tweeted successfully for {city}! :D")
#                time.sleep(10)
#            
#            except (requests.RequestException, tweepy.TweepyException) as e:
#                print(f"An error occurred for {city}: {str(e)}")
#            except (KeyError, IndexError):
#                print(f"Error processing weather data for {city}")
#            except Exception as e:
#                print(f"An unexpected error occurred for {city}: {str(e)}")