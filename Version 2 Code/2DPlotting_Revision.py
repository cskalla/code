#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:35:04 2021

@author: carolineskalla
"""

#General imports
import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint
import math
import statistics
import sys
from mpl_toolkits import mplot3d
#import seaborn as sns
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy.interpolate import griddata


#from ATAFDSimulation_Revisions import simulation
import ATAFDSimulation_Revisions

def graph2D():
    #user sets foxhedge ratios she's interested in using foxhedgeArray])
    foxhedgeArray = ([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    foxhedgeArraySize = len(foxhedgeArray)
    masterScoreList = []
  
    #generate as many lists as there are foxhedge ratios
    i = 0
    while(i < foxhedgeArraySize):
        temp = []
        masterScoreList.append(temp)
        i += 1

    #fill in sublists of masterScoreList. Each contains scores from one foxhedge ratio
    numRuns = 10
    numTrials = numRuns
    while(numRuns > 0):
        index = 0
        for ratio in foxhedgeArray:
            #timeFactor = 2, 10 agents, 15 tasks, ratio
            #timeFactor = 2
            numAgents = 100
            #numTasks = 15
            foxhedge = ratio
            taskRate = 10
            time = 2000
            #penalty = 0.1 
            #scorecoeff = 0.1
            score = ATAFDSimulation_Revisions.simulation(numAgents, foxhedge, taskRate, time)
            masterScoreList[index].append(score)
            index += 1
        numRuns -= 1
    
    #comment the following code in or out to generate the desired plots
    #meanScoreVsFoxhedge(timeFactor, numAgents, numTasks, foxhedge, penalty, scorecoeff, numTrials, foxhedgeArray, masterScoreList)
    medianScoreVsFoxhedge( numAgents, foxhedge, taskRate, time, numTrials, foxhedgeArray, masterScoreList)
    #allScoreVsFoxhedge(timeFactor, numAgents, numTasks, foxhedge, penalty, scorecoeff, numTrials, foxhedgeArray, masterScoreList)


#numAgents, foxhedge, taskRate, time


def medianScoreVsFoxhedge(numAgents,  foxhedge, taskRate, time, numTrials, foxhedgeArray, masterScoreList):
    sys.stdout=open("2Dmedian.txt","w")

    medianScores = []

    #find the median of each sublist
    j = 0
    while(j < len(masterScoreList)):
        medianScores.append(statistics.median(masterScoreList[j]))
        j += 1
    
    #Median score  vs fox ratio (for multiple runs)
    plt.figure(2)
    x = np.array(foxhedgeArray)
    plt.scatter(x, medianScores)
    m, b = np.polyfit(x, medianScores, 1)
    plt.plot(x, m*x + b)
   # plt.plot(foxhedgeArray, np.poly1d(np.polyfit(foxhedgeArray, medianScores, 1)*foxhedgeArray)
    plt.title('Median Scores vs. Proportion of Generalists')
    plt.xlabel("Proportion of Generalists")
    plt.ylabel("Median Scores")
    plt.figtext(.5, 0, "time = " + str(time) + ", numAgents = " + str(numAgents) + ", taskRate = " + str(taskRate) + ", numRuns = " + str(numTrials), ha="center", fontsize=9) 
    plt.subplots_adjust(bottom=0.15)
    plt.show()

    sys.stdout.close()
    
graph2D()
    

    