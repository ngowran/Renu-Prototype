import pyrebase
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

pin = 4

config = {
  # Include here the config information of your Firebase database.
  # I have removed this for security purposes.
};

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()
database = firebase.database()

while True:
  humidty, temperature = Adafruit_DHT.read_retry(sensor, pin)
  sensor_data = ('Temp={0:0.1f}*C Humidty={1:0.1f}%'.format(temperature, humidty))
  print(sensor_data)
  database.child("Renu")
  data = {"Key1": sensor_data}
  database.set(data)
  time.sleep(10)

  # Program runs indefinitely until you stop it manually.
  # Sends data every 10 seconds.
