import matplotlib;import matplotlib.pyplot as plt
import math
import numpy as np
import random
import pylab


Alaska = [0.057,-0.118,0.335,-0.299,-0.867,-0.152,-0.452,0.476,-0.003,0.426,-0.023,-1.796,0.306,-0.846,0.225,0.083,1.079,-0.605,-0.214,0.917,1.562,-0.673,0.488,0.337,-0.311,0.011,1.34,1.204,0.017,0.078,0.336,0.1,0.342,0.467,0.938,-0.125,0.426,2.47,1.694,1.291,1.421,0.54,1.24,0.485,1.282,2.343,1.333,0.851,0.539,2.915,1.438,2.144,1.182,0.288,1.231,2.373,1.48,0.477,1.311,1.128,2.515,1.268]
EastAsia = [0.668,0.125,-0.053,0.266,-0.519,0.019,0.034,-0.498,-0.049,-0.381,-0.334,0.227,0.325,-0.488,0.041,-0.506,-0.154,0.232,0.458,-0.206,-0.631,-0.041,0.107,-0.605,0.13,-0.686,0.326,-0.154,0.556,1.132,0.726,0.333,0.012,0.965,0.348,-0.127,0.454,1.199,0.948,0.636,0.418,0.63,0.326,1.116,0.737,0.39,1.004,0.671,0.801,0.922,0.596,0.395,0.628,0.56,0.833,1.323,0.796,0.926,1.272,1.437,1.27,1.335]
UK = [0.264,-0.688,-0.773,0.158,-0.554,-0.033,-0.009,0.072,-0.265,0.06,0.342,-0.268,0.362,-0.211,0.701,0.561,-0.279,0.257,-0.687,-0.057,0.377,0.154,0.408,0.336,-0.439,-0.726,-0.143,0.246,1.054,0.829,0.199,0.446,0.064,0.282,1.198,-0.006,0.977,0.937,1.077,0.577,0.551,0.83,1.024,0.9,1.175,1.159,1.345,0.836,0.804,-0.104,0.559,0.705,0.568,1.357,0.449,1.04,1.264,0.783,1.201,1.075,1.019,1.764]
Oceania = [-0.282,0.581,-0.356,-0.455,-0.451,-0.233,-0.184,-0.086,-0.374,0.596,0.684,0.119,0.196,0.363,0.588,-0.51,-0.388,0.387,0.316,0.007,0.427,-0.062,-0.294,0.174,0.398,0.382,0.397,0.488,0.736,0.572,-0.028,-0.716,-0.38,-0.077,0.108,0.244,-0.128,0.981,1.009,0.265,0.572,0.42,0.238,0.033,0.443,0.391,0.237,0.564,0.059,0.598,0.673,0.125,0.999,0.544,0.568,1.214,0.627,1.173,1.118,0.912,0.982,1.319]
SouthAmerica = [0.122,-0.046,0.162,-0.343,0.09,-0.163,0,0.472,0.292,0.438,-0.26,-0.008,-0.139,-0.106,-0.021,-0.321,0.432,0.362,0.266,0.373,0.378,0.359,0.046,-0.1,0.308,0.46,0.446,-0.192,0.611,0.436,0.261,-0.261,0.086,0.487,0.259,0.512,0.759,0.351,0.16,-0.186,0.425,0.278,0.635,0.47,0.281,0.596,-0.169,0.601,0.857,0.135,0.386,0.798,0.442,0.951,0.957,0.488,1.095,0.878,0.76,1.123,1.031,0.643]
TropicalAfrica = [0.251,0.215,0.185,-0.072,-0.025,0.246,-0.073,-0.376,0.287,0.365,-0.153,0.106,0.35,-0.245,-0.132,-0.504,0.171,0.059,0.317,0.237,-0.328,0.212,0.707,0.535,0.663,0.463,0.743,0.338,-0.034,0.324,0.367,0.807,0.836,0.208,0.633,-0.15,0.219,0.825,1.096,0.271,0.516,0.453,0.791,0.874,1.031,0.361,0.721,0.575,0.662,1.083,0.446,0.508,0.655,0.838,1.3,1.562,1.103,1.016,1.811,0.89,0.809,1.094]

class Region:
    def __init__(self, name, zone, temperature, initialTemp):
        self.name = name
        self.zone = zone
        self.temp = temperature
        self.initialTemp = initialTemp
class Bird:
    def __init__(self, name, probability):
        self.name = name
        self.prob = probability
    def update_prob(self, prob):
        self.prob = prob

time_steps = 100
temperature = []
greenhouse_gases_ranges = []
location = []
species = ["Pied Wheatear", "Northern Wheatear", "Pectoral Sandpiper", "Bar-tailed Godwit", "Short-tailed Shearwater"]


def calculateMigrationSuccess(self):
    successProb = random.randrange(9, 17) + 2
    print("successProb: ", successProb)

def calculateNewPath(self): # maybe call newPath before calcMigrationSuccess to decide if the bird even migrates in the first place
    if(abs(self.temperature-self.initialTemp) > 1.8): # if the new temperature this year is too hot, the agent will migrate earlier
        



def migrate():
    PiedWheatearArr = []
    NorthernWheatearArr = []
    PectoralSandpiperArr = []
    BartailedGodwitArr = []
    ShorttailedShearwaterArr = []


    for i in range(0, time_steps)
        for y in range(0, len(species)): # loop for each species
            for x in range(0, 43): # 43 years (1980-2023)
                for z in range(0, 50): # 50 birds for each species
                    match y:    # switch case for each of the 5 birds
                        case 0:
                            if(calculateMigrationSuccess()):    # if migration probability returns true(migration is a success) add to bird array
                                count += 1
                                PiedWheatearArr.append(1)
                        case 1:
                            if(calculateMigrationSuccess()):
                                count += 1
                                NorthernWheatearArr.append(1)
                        case 2:
                            if(calculateMigrationSuccess()):
                                count += 1
                                PectoralSandpiperArr.append(1)
                        case 3:
                            if(calculateMigrationSuccess()):
                                count += 1
                                BartailedGodwitArr.append(1)
                        case 4:
                            if(calculateMigrationSuccess()):
                                count += 1
                                ShorttailedShearwaterArr.append(1) 




migrate()
