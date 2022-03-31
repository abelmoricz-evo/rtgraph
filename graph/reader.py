import json
import requests
import websocket

ws = websocket.WebSocket()

import random, time

ws.connect('ws://localhost:8000/ws/graph/')

def read_force1():
    while True:
        time.sleep(.4)
        force1 = open('force1_output.txt', 'r')
        force1_value = force1.readline()
        force1.close()
        ws.send(json.dumps({'type':'data','value':{'sensor_data':force1_value,'unit':'lbs', 'sensor':'force1'}}))

if __name__=='__main__':
    read_force1()
