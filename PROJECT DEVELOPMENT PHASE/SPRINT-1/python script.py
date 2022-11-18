import time
import random
import sys
import requests 
import json
import ibmiotf.application
import ibmiotf.device


# watson device details

organization = "fd7fvs"
devicType =  "Smart_Management"
deviceId = "113355"
authMethod= "token"
authToken= "1122334455"

#generate random values for random variables (Distance and load)



def myCommandCallback(cmd):
    global a
    print("command recieved:%s" %cmd.data['command'])
    control=cmd.data['command']
    print(control)

try:
        deviceOptions={"org": organization, "type": devicType,"id": deviceId,"auth-method":authMethod,"auth-token":authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
        print("caught exception connecting device %s" %str(e))
        sys.exit()

#connect and send a datapoint "Distance" with value integer value into the cloud as a type of event for every 10 seconds
deviceCli.connect()

while True:
    lat=10.9368
    lon=78.1366
    bin_level= random.randint(1,75)
    bin_weight= random.randint(0,20)
    data= {'Bin_level':bin_level,'Bin_Weight':bin_weight,'latitude':lat,'longitude':lon}
    warn={"Msg":"Bin is Free"}
    if bin_weight<5 and bin_weight>0:
        weight="20"
    elif bin_weight<10 and bin_weight>5:
        weight="40" 
    elif bin_weight<15 and bin_weight>10:
        weight="60"
    elif bin_weight<18 and bin_weight>15:
        weight="80"
    elif bin_weight<20 and bin_weight>18:
        weight="90"
    else:
        weight="100"
            
    if bin_level<7 and bin_level>1:
        level="90%"
    elif bin_level<15 and bin_level>7:
        level="80%"
    elif bin_level<30 and bin_level>15:
        level="60%"
    elif bin_level<45 and bin_level>30:
        level="40%"
    elif bin_level<60 and bin_level>45:
        level="20%"
    elif bin_level<75 and bin_level>60:
        level="10%"
    else:
        level="0%"
        
    if(level=="90%" or weight=="90%"):
        warn={'Alert':'Dustbin is almost filled'}
        
    def myOnPublishCallback(latitude=10.9368,longitude=78.1366):
        print("published Level of bin = %s " %level,"weight= %s " %weight, "Latitude = %s " %latitude,"Longitude = %s " %longitude)
        print("Bin_Weight",weight)
        print("Bin_Level",level)
        print(warn)
        
    time.sleep(10)
   
   
    success=deviceCli.publishEvent ("IoTSensor","json",warn,qos=0,on_publish= myOnPublishCallback)
   
    success=deviceCli.publishEvent ("IoTSensor","json",data,qos=0,on_publish= myOnPublishCallback)
   
    

    if not success:
        print("not connected to ibmiot")
    time.sleep(20)
   
           
   

    deviceCli.commandCallback=myCommandCallback
#disconnect the device
deviceCli.disconnect()
