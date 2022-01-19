import numpy
from gnss_tec import rnx
import datetime
from time import localtime
from gnss_tec.glo import collect_freq_nums
import numpy as np

path_to_file = "data/ugts3110.21o"
generated_file = open("generated/generated_data_" + str(datetime.date.today()) + '_' + str(localtime().tm_hour)+ "_" + str(localtime().tm_min)+ "_" + str(localtime().tm_sec), 'w+')
array = []

class Data:
    timestamp = None
    satellite = None
    phase_tec = None
    p_range_tec = None

    def __init__(self, timestamp, satellite, phase_tec, p_range_tec):
        self.timestamp = timestamp
        self.satellite = satellite
        self.phase_tec = phase_tec
        self.p_range_tec = p_range_tec

    def to_str(self):
        return '{} {}: {} {}'.format(
            self.timestamp,
            self.satellite,
            self.phase_tec,
            self.p_range_tec,
        )

#glo_freq_nums = collect_freq_nums(path_to_file)

with open(path_to_file) as obs_file:
    reader = rnx(obs_file)
    for tec in reader:
        data = Data(tec.timestamp, tec.satellite, tec.phase_tec, tec.p_range_tec)
        array.append(data)


for i in array:
    #print(i.to_str())
    generated_file.write(i.to_str() + "\n")


