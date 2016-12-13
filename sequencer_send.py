from base import *
import csv, sys, numpy as np
import serial, pdb

ser = serial.Serial('COM4', 9600, timeout=10)
class SequenceSource:
    def __init__(self):
        self.stored = ([0 for _ in range(6)],[0 for _ in range(6)])

    @property
    def notes(self):
        return [int(i) for i in ser.readline().split('+')[1].split('-')], [int(i) for i in ser.readline().split('+')[0].split('-')]

    @property
    def buffer(self):
        pedal = int(ser.readline().split('+')[-1])
        if pedal:
            self.stored = self.notes
        return self.stored

if __name__ == '__main__':
    length = 100
    seq = SequenceSource()
    while True:
        pm = PacketManager(length)
        pm.add_data_source(seq)
        pm.send_to_max()
    ser.close()
