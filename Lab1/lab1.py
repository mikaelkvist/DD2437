import numpy as np
import matplotlib.pyplot as plt

# sets seed for same results each time
np.random.seed(0)

# switches for plotting
plot_permutation = 0
plot_classes = 0

# number of data points in each class
N = 10;
# mean of classes, (x, y)
mA = [1.0, 1.0]
mB = [-1.0, -1.0]

# standard deviation for the classes
sigmaA = 0.5
sigmaB = 0.5

# covariance matrices
covA = [ [sigmaA**2, 0], [0, sigmaA**2] ]
covB = [ [sigmaB**2, 0], [0, sigmaB**2] ]

# classes of data points, column 1 is x, column 2 is y
classA = np.random.multivariate_normal(mA, covA, N)
classB = np.random.multivariate_normal(mB, covB, N)

# array with all data and labels
# 2 (for two classes), times N for number of data points and 3 for (x,y,label)
data = np.zeros( (2*N, 3) )
data[:N,:2] = classA
data[:N,2]  = 0                  # label for class A
data[N:,:2] = classB
data[N:,2]  = 1                  # label for class B

# permutes data for better learning in sequential mode
data = np.random.permutation(data)

# plot data in order if you are uncertain about the permutation
if plot_permutation:
    f = plt.figure(1)
    for row in data:
        marker = '*r' if row[2] == 0 else '*b'
        plt.plot(row[0], row[1], marker)
        plt.pause(0.001)
    f.show()

if plot_classes:
    ff = plt.figure(2)
    plt.plot(classA[:,0], classA[:,1], '*m')
    plt.plot(classB[:,0], classB[:,1], '*g')
    ff.show()

# to keep figures alive
if plot_permutation or plot_classes:
    input()


# Tasks...
