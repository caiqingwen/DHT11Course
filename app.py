from flask import Flask, render_template
import dht11
import RPi.GPIO as GPIO
import datetime

app = Flask(__name__)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

@app.route("/")
def index():
    instance = dht11.DHT11(pin=14)
    result = instance.read()
    Temperature = str(result.temperature)
    Humidity = str(result.humidity)
    return 'Temperature: ' + Temperature + '      ' + 'Humidity:' + Humidity 

if __name__ == '__main__':
    app.run(host="10.254.24.50",port=80,debug=True)