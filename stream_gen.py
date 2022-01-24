import numpy
from gnss_tec import rnx
import datetime
from time import localtime
from Data import Data
import numpy as np
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")

path_to_file = "data/ugts3110.21o"
#generated_file = open("generated/generated_data_" + str(datetime.date.today()) + '_' + str(localtime().tm_hour)+ "_" + str(localtime().tm_min)+ "_" + str(localtime().tm_sec), 'w+')
array = []



#glo_freq_nums = collect_freq_nums(path_to_file)

with open(path_to_file) as obs_file:
    reader = rnx(obs_file)
    for tec in reader:
        data = Data(tec.timestamp, tec.satellite, tec.phase_tec, tec.p_range_tec)
        array.append(data)


#for i in array:
    #print(i.to_str())
    #generated_file.write(i.to_str() + "\n")

counter = 0
for i in array:
    print("Sending request %s …" % i.to_str())
    socket.send(i.to_str().encode('utf-8'))

    #  Get the reply.
    message = socket.recv()
    #print("Received reply %s [ %s ]" % (request, message))
    counter += 1
