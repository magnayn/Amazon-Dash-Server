"""
This is a very simple TCP server that does not use SSL. It simply completes
the 3-way handshake and closes the connection.
"""
import SocketServer, SimpleHTTPServer
import time
import paho.mqtt.client as mqtt

last = 0

class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        global last

	print 'incoming ', self.client_address[0]
	self.request.close()
	# run your custom code
        thistime = time.time()
        if last + 5 < thistime:
            print 'PUBLISH'
            broker_address="192.168.0.16" 
#broker_address="iot.eclipse.org" #use external broker
            client = mqtt.Client("P1") #create new instance
            client.connect(broker_address) #connect to broker
            client.publish("/amazon/dash","PRESS")#publish
	    last = thistime

if __name__ == "__main__":
    # Create the server, binding to localhost on port 443
    server = SocketServer.TCPServer(("", 443), MyTCPHandler)
    server.serve_forever()
