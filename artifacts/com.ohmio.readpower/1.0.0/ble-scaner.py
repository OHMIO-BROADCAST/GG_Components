import requests
import json
import sys
from bluepy import btle
from bluepy.btle import Scanner
import math
#url = 'http://192.168.1.8:3001/users/Waipo'


try:
    # based on http://ianharvey.github.io/bluepy-doc/scanner.html#sample-code
 
    scanner = Scanner(0) 
    devices = scanner.scan(1)
 
    devices_m = []

    for dev in devices:
         
        name = ""
        power = ""
        for (adtype, desc, value) in dev.getScanData():
            if (desc == "Complete Local Name"):
                name = str(value)
            elif (desc == "Tx Power"):
                power = str(value)
        if (name != "Waipo"):
        
            #CALCULO DE DISTANCIA EN METROS:
            meters = math.pow(10,((-67.5-((dev.rssi)))/(10.0*2.85)))
            meters = str(meters)

            #AGREGAR AL OBJETO DE DISPOSITIVO ACTUAL
            devices_m.append({'addr': dev.addr, 'addType': dev.addrType, 'rssi': dev.rssi, 'power': power, 'meters':meters})
            json_devices = json.dumps(devices_m)

            #PARA PETICIÓN HTTP
            #requests.put(url, json = json_devices)
            #requests.put(url, data = {'addr': dev.addr, 'addType': dev.addrType, 'rssi': meters, 'power': power})
            
            #SE IMPRIME
            print(json_devices)
 
except Exception as ex:
    print ( "Unexpected error in BLE Scanner BLUEPY: %s" % ex )
