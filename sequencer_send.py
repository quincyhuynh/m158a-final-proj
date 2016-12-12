from base import *
import csv, sys, numpy as np
import serial, pdb

ser = serial.Serial('COM4', 9600, timeout=10)
class SequenceSource(DataSource):
    @property
    def data(self):
        return [int(i) for i in ser.readline().split('-')]

    def zero_hold(self, data, hold):
        new_data = []
        len_data = len(data)
        i = 0
        while len(new_data) < len_data * hold and i < len_data:
            for _ in range(hold):
                new_data.append(data[i])
            i += 1

        i = 0
        while len(new_data) < self.num_datapoints and i < len_data:
            for _ in range(hold):
                new_data.append(data[i])
            i += 1
        return new_data

if __name__ == '__main__':
    # if len(sys.argv) != 1:
    #     print('Usage: python tab_source.py <length>')
    length = 100
    seq = SequenceSource(length, '')
    while True:
        pm = PacketManager(length)
        pm.add_data_source(seq)
        pm.send_to_max()
    ser.close()
