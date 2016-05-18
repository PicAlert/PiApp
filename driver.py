import RPi.GPIO as GPIO
import time
import json, urllib2
from picamera import PiCamera

# GPIO Setup
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

# Camera Setup
camera = PiCamera()

# Settings Setup
config = {}
execfile('settings.conf', config)

# API Data Setup
alert_data = {
    'title': 'Alarm Trip',                  # Type of event
    'alert_message': config['alert_msg'],   # Text content of alerts (may change)
    'device_id': config['device_id'],       # Comes with device
    'secret_key': config['secret_key'],     # Retrieved on registration (unused for demo)
    'api_password': config['api_password'], # Protect api from garbage calls
}

alert_url = "http://" + config['heroku_app'] + ".herokuapp.com/alert"

# TODO: listening logic