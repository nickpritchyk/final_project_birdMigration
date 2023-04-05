import matplotlib;import matplotlib.pyplot as plt
import math
import numpy as np
import random
import pylab

class Region:
    def __init__(self, name, zone, temperature):
        self.name = name
        self.zone = zone
        self.temp = temperature
class Bird:
    def __init__(self, name, probability):
        self.name = name
        self.prob = probability
    def update_prob(self, prob):
        self.prob = prob

time_steps = 100000
temperature = []
greenhouse_gases_ranges = []
location = []
species = ["Pied Wheatear", "Northern Wheatear", "Pectoral Sandpiper", "Bar-tailed Godwit", "Short-tailed Shearwater"]


def calculateMigrationLikeness():
    print("Calculating birds likeliness to migrate")

def migrate():
    print('Starting Migration...')
    sandpiper = Bird("sandpiper", 20)
    print(sandpiper)

    


migrate()