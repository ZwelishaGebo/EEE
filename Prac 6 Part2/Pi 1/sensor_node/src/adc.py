import socket
import sys
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

################TCP SEND SETUP###########################

#TODO Add code to setup the tcp connection with the correct IP and same port as the tcp_server on the other pi
    #Test this locally before trying to deploy via balena using test messages instead of ADC values
    #Use localmode when deploying to balena and use the advertised local address (using public IPs is possible but more complicated to configure due to the security measures BalenaOS imposes by default.  These are a good thing for real world deployment but over complicate the prac for the immediate purposes





TCP_IP = '192.168.115.241'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = bytes("Hello, World!",'utf-8')

print("ADC has started")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)





##################ADC Setup##############################

#TODO using the adafruit circuit python SPI and MCP libraries setup the ADC interface
#Google will supply easy to follow instructions 


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
temp = AnalogIn(mcp, MCP.P1)
print("Runtime Temp Reading Temp Light Reading");
a=0;



#########################################################

f = open("demofile2.txt", "a")
print("Sensor Node it awake\n")     #Print statements to see what's happening in balena logs
f.write("Sensor Node it awake\n")   #Write to file statements to see what's happening if you ssh into the device and open the file locally using nano
f.flush()
#s.send(b'Sensor Node it awake\n')   #send to transmit an obvious message to show up in the balena logs of the server pi

while(True):
   



    #TODO add code to read the ADC values and print them, write them, and send them

	#print(a,"s",temp.value,""+str(round(lmt86_v2t(temp.voltage*1000),3))+"C ",chan.value);
	#a=a+5;
	print("Zwe")
	time.sleep(5);
