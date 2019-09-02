import numpy as np
import matplotlib.pyplot as plt

meanA = [10,20]
covA  = [[1,0], [0,1]]

meanB = [30,10]
covB  = [[10,0], [0,1]]

xA, yA = np.random.multivariate_normal(meanA, covA, 100).T
plt.plot(xA, yA, '*r')

xB, yB = np.random.multivariate_normal(meanB, covB, 100).T
plt.plot(xB, yB, '*b')

plt.axis('equal')
plt.show()
