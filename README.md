# ThingSpeak_Connection
This respository will be used to storage all the code made for a IoT project assigned by one of my teachers at university.

## WiFi Connection
On this folder you will find the interfaces and the wpa_supplicant.config files necessary to set up the Raspberry Pi wifi connection. Note than if your Raspbian version is new, you won't need the interfaces file.

## TempHum.py
This python file creates two channel in the [ThingSpeak Website](https://thingspeak.com), in order to upload data every 10 seconds. Data comes from a DHT11 humidity/temperature sensor.

Channels are created automatically and data is uploaded to them as long as the program is left running.

## LineCharts.html
This file downloads data from the ThingSpeak Channels and uses html, JavaScript and [Google Charts](https://developers.google.com/chart/) to plot it.

Since data was uploaded to both channels it also reconstructs it before plotting.
