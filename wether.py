from pyowm import OWM


owm = OWM('5b83253acadd70af6293bf3f749c90cf')

manager = owm.weather_manager()


place = input("enter yout city name:  ")

obs = manager.weather_at_place(place)

w = obs.weather

temp= obs.weather.temperature("celsius")["temp"]
wind = w.wind()["speed"]
humidity = w.humidity


print("temparature is {temp}°C".format(temp=temp))
print("Wind speed is {} m/s".format(wind))
print("Humidity is {} %".format(humidity))


# Geo location


geo_manager = owm.geocoding_manager()

location = geo_manager.geocode(place)


place_name = location[0].name

latitude = location[0].lat

longitude = location[0].lon


print(f"place : {place} => latitude: {latitude} longitude: {longitude}")