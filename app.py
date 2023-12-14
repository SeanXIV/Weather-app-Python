import requests

def get_weather_data(api_key, user_input):
    # Construct the URL for OpenWeatherMap API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
    
    # Make a request to the API and return the JSON response
    return requests.get(url).json()

def display_weather_info(user_input, weather_data):
    # Check if the city is not found
    if weather_data['cod'] == '404':
        print("No City Found")
    else:
        # Extract weather and temperature information from the JSON response
        weather = weather_data['weather'][0]['main']
        temp = round(weather_data['main']['temp'])

        # Display the weather information
        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}ºF")

def main():
    # OpenWeatherMap API key
    api_key = '30d4741c779ba94c470ca1f63045390a'
    
    # Get user input for the city
    user_input = input("Enter city: ")

    # Get weather data for the specified city
    weather_data = get_weather_data(api_key, user_input)
    
    # Display weather information
    display_weather_info(user_input, weather_data)

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
