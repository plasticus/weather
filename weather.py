from flask import Flask, render_template
from PIL import Image
import random
import math

app = Flask(__name__)

# Create lists of weather conditions, temperatures, wind speeds, and wind directions
conditions = ['Sunny', 'Partly sunny', 'Partly cloudy', 'Light showers', 'Showers', 'Thunderstorms']
temperatures = range(70, 85) # Temperature range in Fahrenheit
wind_speeds = range(5, 30) # Wind speed range in knots


# Define the path where the weather condition images are stored
IMAGE_PATH = 'static/images/'

@app.route('/')
def weather():
    # Generate a random weather condition, temperature, and wind speed
    condition = random.choice(conditions)
    temperature = random.choice(temperatures)
    wind_speed = random.choice(wind_speeds)
    wind_speed_mph = int(math.ceil(wind_speed * 1.15078))

    # Open the corresponding image for the weather condition
    image_file = IMAGE_PATH + condition.lower().replace(' ', '_') + '.png'
    image = Image.open(image_file)

    # Determine if the weather will change in the evening
    change_weather = random.choice([True, False])

    if change_weather:
        # Generate a new random weather condition, temperature, and wind speed
        new_condition = random.choice(conditions)
        new_temperature = random.choice(temperatures)
        new_wind_speed = random.choice(wind_speeds)
        new_wind_speed_mph = int(math.ceil(new_wind_speed * 1.15078))
        change_message = f"The weather is expected to change to {new_condition} with a temperature of {new_temperature}F and wind speed of {new_wind_speed} knots ({new_wind_speed_mph} mph) in the evening."
    else:
        # Use the current weather conditions for the evening
        new_condition = condition
        new_temperature = temperature
        new_wind_speed = wind_speed
        new_wind_speed_mph = wind_speed_mph
        change_message = "The weather is expected to remain the same in the evening."

    # Render the HTML template with the weather information and image
    return render_template('weather.html', condition=condition, temperature=temperature, wind_speed=wind_speed, wind_speed_mph=wind_speed_mph,
                           new_condition=new_condition, new_temperature=new_temperature, new_wind_speed=new_wind_speed, new_wind_speed_mph=new_wind_speed_mph,
                           change_message=change_message, image=image_file)

if __name__ == '__main__':
    app.run(debug=True)
