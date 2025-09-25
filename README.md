# 🌦️ European Weather Twitter / 𝕏 Bot

An automated Python bot that tweeted daily weather updates for a **random European country**.  
It posted **2 to 3 tweets per day** (depending if the country selected had one or 2 cities in the dictionary):
1. A tweet announcing the **country of the day**.
2. One or two tweets with **live weather data** for the **largest cities** in that country.

You can check out its past posts [here](https://x.com/___WeatherBot__)!

---

## 🚀 Features

- 🌍 **Random country selection**: Picks a new European country each run.
- ☁️ **Real-time weather data**: Fetches current weather from the [OpenWeatherMap API](https://openweathermap.org/api).
- 📸 **Dynamic media**: Attaches themed weather images (cold, regular, or hot) to each weather tweet.
- 🤖 **Automated posting**: Publishes tweets using the [Twitter / 𝕏 API](https://developer.twitter.com/en/docs/twitter-api).

---

## 🛠️ How It Works

1. The script randomly selects a European country from a predefined list.
2. It tweets the selected country as the **"Country of the Day"**.
3. It then retrieves current weather data for one or two major cities in that country.
4. Depending on the temperature, it attaches a **cold**, **regular**, or **hot** weather image and tweets the forecast.

Example tweet:
> Today's weather in Berlin: clear sky. Temperature: 22.45°C
>> Correct .png file attached to the post depending on the fetched temperature (in this case the regular weather png).

---

## 📁 Project Structure

├── main_TWB.py # Main bot script \
├── cold_weather.png # Weather image for cold days \
├── regular_weather.png # Weather image for moderate days \
├── hot_weather.png # Weather image for hot days \
└── keys.py (private) # API keys (not included)

---

## 🔧 Requirements

- Python 3.8+
- [tweepy](https://www.tweepy.org/) - Twitter / 𝕏 API client
- [requests](https://docs.python-requests.org/) - For fetching weather data

Install dependencies:
```bash
pip install tweepy 
pip install requests
```

---

## 🔑 Setup

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/european-weather-bot.git
cd european-weather-bot
```

2. **Create a keys.py file in the project root with your API credentials:**
```python
api_key = "YOUR_TWITTER/𝕏_API_KEY"
api_secret = "YOUR_TWITTER/𝕏_API_SECRET"
access_token = "YOUR_TWITTER/𝕏_ACCESS_TOKEN"
access_token_secret = "YOUR_TWITTER/𝕏_ACCESS_TOKEN_SECRET"
bearer_token = "YOUR_TWITTER/𝕏_BEARER_TOKEN"
api_key_openweather = "YOUR_OPENWEATHERMAP_API_KEY"
```

3. **Add weather images:**
Make sure cold_weather.png, regular_weather.png, and hot_weather.png are present in the same directory as main_TWB.py.

---

## ▶️ Usage

Run the bot manually:
```bash
python main_TWB.py
```
Or automate it to run daily using a third-party scheduler such as [PythonAnywhere](https://www.pythonanywhere.com/).

---

## 📜 License
This project is licensed under the MIT License - feel free to use and modify it.
