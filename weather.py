import random

# Create lists of weather conditions, temperatures, wind speeds, and wind directions
conditions = ['Sunny', 'Partly cloudy', 'Mostly cloudy', 'Scattered thunderstorms', 'Isolated showers']
temperatures = range(25, 32) # Temperature range in Celsius
wind_speeds = range(5, 15) # Wind speed range in knots
wind_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

# Generate a random weather condition, temperature, wind speed, and wind direction
condition = random.choice(conditions)
temperature = random.choice(temperatures)
wind_speed = random.choice(wind_speeds)
wind_direction = random.choice(wind_directions)

# Print out the results
print(f"The weather today is {condition} with a temperature of {temperature} degrees Celsius and a wind speed of {wind_speed} knots from the {wind_direction}.")