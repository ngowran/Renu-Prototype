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
i = 0

while True:
  
  # Setting our values
  humidty, temperature = Adafruit_DHT.read_retry(sensor, pin)
  sensor_data = ('Temp={0:0.1f}*C Humidty={1:0.1f}%'.format(temperature, humidty))
  
  # Prints in terminal
  print(sensor_data)
  
  # Setting the current time to a variable.
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  
  # Updating data to main branch.
  data = {f"Key {i}": f"{sensor_data} Time= {current_time}"}
  database.child("Renu").update(data)
  
  # Setting latest data to individual branch - to be displayed on web/mobile applications.
  set_data = {"Key 1": f"{sensor_data} Time= {current_time}"}
  database.child("sensor").set(set_data)
  
  time.sleep(10)
  i += 1

  # Program runs indefinitely until you stop it manually.
  # Sends data every 10 seconds.
