import math
import numpy
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,15,3,6,17,8,16,8,3,10,12,16,12,9]

print(numpy.min(x))
print(numpy.max(x))
print(numpy.std(x))
print(numpy.mean(x))
print(numpy.median(x))

x = [1,2,15,3,6,17,8,16,8,3,10,12,16,12,9]

plt.boxplot(x)
plt.show()