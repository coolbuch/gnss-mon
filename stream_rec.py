from Data import Data
import time
import zmq

ip = "192.168.56.246"
port = "5555"
protocol = "tcp"

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(protocol + "://" + ip + ":" + port)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    #time.sleep(1)

    #  Send reply back to client
    socket.send(b"ok")
