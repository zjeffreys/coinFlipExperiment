# importing the required module
import matplotlib.pyplot as plt
import random


# corresponding y axis values
numTosses = [] #average number of tosses before observing 3 heads
experiments = [] #experiments conducted 1-1000 times

def singleExperiment():
    HEAD = 3
    successes = 0
    tosses = 0
    while(successes < HEAD):
        tosses += 1
        if random.random() <= 0.5:
            successes += 1
    return tosses
               
def nExperiments(n):
    i = 0
    while i < n:
        i = i+1
        numTosses.append(singleExperiment())
        experiments.append(i)

def plot_graphs(x, y):
    # plotting the points
    plt.plot(x, y)  

    # naming the x axis
    plt.xlabel('Experiments')
    # naming the y axis
    plt.ylabel('Tosses Until 3 Heads')

    # giving a title to my graph
    plt.title('Coin Toss Experiment')

    # function to show the plot
    plt.show()

nExperiments(1000)
plot_graphs(experiments, numTosses)
