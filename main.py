import network
import time
import dht
from machine import Pin

SSID = "Wokwi-GUEST"
PASSWORD = ""
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
print("Connecting to WiFi...", end="")
while not wlan.isconnected():
    time.sleep(0.5)
print("Connected!\nIP Address:", wlan.ifconfig()[0])

sensor = dht.DHT22(Pin(7))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature:{:.1f}°C)Humidity: {:.1F}%".format(temp,hum))
    except OSError as e:
        print("Sensor reading failed:",e)
        time.sleep(2)#wait
