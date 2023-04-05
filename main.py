import matplotlib;import matplotlib.pyplot as plt
import math
import numpy as np
import random
import pylab

time_steps = 100000
temperature = []
greenhouse_gases_ranges = []
location = []
species = ["Pied Wheatear", "Northern Wheater", "Pectoral Sandpiper", "Bar-tailed Godwit", "Short-tailed Shearwater"]


def migrate():
    print('Starting Migration...')

    for i in range(0, location.length()):

        for i in range(0, time_steps):
            for j in range(0, species.length()):
                if(i == location[0]):
                    print("First Migration Path")
                if(i == location[1]):
                    print("Second Migration Path")
                if(i == location[2]):
                    print("Third Migration Path")


migrate()