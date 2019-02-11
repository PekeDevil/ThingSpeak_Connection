#FIRST STEPS
#libraries and variables
import Adafruit_DHT #https://github.com/adafruit/Adafruit_Python_DHT
import time
import httplib
import urllib
import json
USER_API_KEY = 'xxxxxxxxxx'
hum01=0
hum02=0
temp01=0
temp02=0

primerflag = 0

#sensor setup
sensor = Adafruit_DHT.DHT11
pin= 23 #connected to PIN to GPIO23
timeout = 9
#END FIRST STEPS


# TCP CONNECTION
server = 'api.thingspeak.com'
connTCP = httplib.HTTPSConnection(server)
print("Starting connections...."),
connTCP.connect() #stablishing the connection
print("TCP connection made. Ready to go!")
# END TCP CONNECTIONP


# CREATING CHANNEL 01
#https://es.mathworks.com/help/thingspeak/createchannel.html

#HTTP ask and answer 
print("Creating channel 01..."),
method = "POST"
uri = "/channels.json"
headers_01= {'Host': server,
           'Content-Type': 'application/x-www-form-urlencoded'}
payload_01= {'api_key': USER_API_KEY,
             'public_flag':'true',
            'name' : 'Channel 01',
           'field1' : 'Humidity [%RH]',
            'field2' : 'Temperature [ºC]'}
payload_01_encoded = urllib.urlencode(payload_01) #HTTP petition codified
headers_01['Content-Length'] = len(payload_01_encoded) #lenght added to the headers
print("\t Asking to create channel 01...")
connTCP.request(method, uri, body=payload_01_encoded, headers=headers_01)
#print("Waiting for HTTP answer..."),
respuesta_01= connTCP.getresponse()
status_01 = respuesta_01.status
print ("\t Petition for channel 01: " + str(status_01))

#Channel data is needed for later
contenido_01= respuesta_01.read()
# we save contenido with json format
contenido_01_json = json.loads(contenido_01)
CHANNEL_ID_01 = contenido_01_json['id'] 
WRITE_API_KEY_01 = contenido_01_json['api_keys'][0]['api_key']

# END CREATING CHANNEL 01


# CREATING CHANNEL 02
#HTTP ask and answer 
print("Creating channel 02..."),
method = "POST"
uri = "/channels.json"
headers_02 = {'Host': server,
           'Content-Type': 'application/x-www-form-urlencoded'}
payload_02 = {'api_key': USER_API_KEY,
              'public_flag':'true',
           'name' : 'Channel 02',
           'field1' : 'Humidity [%RH]',
            'field2' : 'Temperature [ºC]'}
payload_02_encoded = urllib.urlencode(payload_02) #HTTP petition codified
headers_02['Content-Length'] = len(payload_02_encoded) #lenght added to the headers
print("\t Asking to create channel 02...")
connTCP.request(method, uri, body=payload_02_encoded, headers=headers_02)
#print("Waiting for HTTP answer..."),
respuesta_02= connTCP.getresponse()
status_02 = respuesta_02.status
print ("\t Petition for channel 02: " + str(status_02))

#Channel data is needed for later
contenido_02 = respuesta_02.read()
# we save contenido with json format
contenido_02_json = json.loads(contenido_02)
CHANNEL_ID_02= contenido_02_json['id'] 
WRITE_API_KEY_02 = contenido_02_json['api_keys'][0]['api_key']
# END CREATING CHANNEL 02


try:
    while (True):
      # SENSOR READING
      # Try to grab a sensor reading.  Use the read_retry method which will retry up
      # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
      if primerflag == 0:
          hum, temp = Adafruit_DHT.read_retry(sensor, pin) #reintentamos hasta tener dato
          if hum is not None and temp is not None:
              print('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, hum))
              hum01 = hum
              temp01 = temp
              primerflag = 1 #we already have the first data
      else:
          # we don't want to lose time with retries
          # Temp y Hum change slowly, so an error margin is accepted
          # The maximum difference between a real data and a repeated one would be 10 seconds
          hum, temp = Adafruit_DHT.read(sensor, pin)
          if hum is not None and temp is not None:
              print('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, hum))
              hum01 = hum
              temp01 = temp
          else:
              hum01 = hum02
              temp01 = temp02
      # END SENSOR READING


      # UPLOADING DATA TO CHANNEL 01
      method = "POST"
      relativ_uri = "/update.json"
      headers = {'Host' : server,
                'Content-Type' : 'application/x-www-form-urlencoded'}
      payload = {'api_key' : WRITE_API_KEY_01,  
                'field1' : hum01,                 
                 'field2' : temp01}                    
      payload_encoded = urllib.urlencode(payload)
      headers['Content-Length'] = len(payload_encoded)

      print("Asking to upload to channel 01...")
      connTCP.request(method, relativ_uri, body=payload_encoded, headers=headers)

      print("Waiting for HTTP answer...")
      respuesta = connTCP.getresponse()
      respuesta.read()
      status = respuesta.status
      print (str(status))
      SubidaCanal01=time.time() #200 means data has just been uploaded
      # END UPLOADING DATA TO CHANNEL 01


      # WAIT
      Medida02 = time.time()
      DeltaTiempo = Medida02 - SubidaCanal01
      while (DeltaTiempo <timeout):
          Medida02 = time.time() #10 seconds loop
          DeltaTiempo = Medida02 - SubidaCanal01
      # END WAIT
      

      # SENSOR READ
      hum, temp = Adafruit_DHT.read_retry(sensor, pin)
      if hum is not None and temp is not None:
          print('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, hum))
          hum02 = hum
          temp02 = temp
      else:
          hum02 =hum01
          temp02 = temp01          
      # END SENSOR READ        
      
      
      # UPLOADING DATA TO CHANNEL 02
      method = "POST"
      relativ_uri = "/update.json"
      headers = {'Host': server,
               'Content-Type': 'application/x-www-form-urlencoded'}
      payload = {'api_key': WRITE_API_KEY_02, 
                'field1' : hum02,                 
                 'field2' : temp02} 
      payload_encoded = urllib.urlencode(payload)
      headers['Content-Length'] = len(payload_encoded)

      print("Asking to upload to channel 02...")
      connTCP.request(method, relativ_uri, body=payload_encoded, headers=headers)

      print("Waiting for HTTP answer...")
      respuesta = connTCP.getresponse()
      respuesta.read()
      status = respuesta.status
      print (str(status))
      SubidaCanal02=time.time() #200 means data has just been uploaded
      # END UPLOADING DATA TO CHANNEL 02
      
      
      # WAIT
      Medida01 = time.time()
      DeltaTiempo2 = Medida01 - SubidaCanal02
      while (DeltaTiempo2 <timeout):
          Medida01 = time.time() #10 seconds loop
          DeltaTiempo2 = Medida01 - SubidaCanal02
      # END WAIT
      
      
except KeyboardInterrupt:

    # TCP CONNECTION IS CLOSED
    connTCP.close()
    print("Se ha pulsado Ctrl+C. Saliendo del programa...")
