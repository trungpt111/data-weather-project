import requests
api_key = "584e7c012a209851f6c79e289ae6b5ad"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=Ha Noi"

def fetch_data():
    print("Fetching weather data from weather stack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received succesfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        raise
# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Ha Noi, Vietnam', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Ha Noi', 'country': 'Vietnam', 'region': '', 'lat': '21.033', 'lon': '105.850', 'timezone_id': 'Asia/Bangkok', 'localtime': '2026-09-27 13:36', 'localtime_epoch': 1790516160, 'utc_offset': '7.0'}, 'current': {'observation_time': '06:36 AM', 'temperature': 33, 'weather_code': 119, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0003_white_cloud.png'], 'weather_descriptions': ['Cloudy '], 'astro': {'sunrise': '05:47 AM', 'sunset': '05:49 PM', 'moonrise': '06:04 PM', 'moonset': '06:03 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 100}, 'air_quality': {'co': '364', 'no2': '5', 'o3': '205', 'so2': '25', 'pm2_5': '33.3', 'pm10': '33.8', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 9, 'wind_degree': 181, 'wind_dir': 'S', 'pressure': 1006, 'precip': 0, 'humidity': 56, 'cloudcover': 70, 'feelslike': 38, 'uv_index': 5, 'visibility': 10, 'is_day': 'yes'}}
