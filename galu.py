import numpy
import matplotlib.pyplot
import scipy


data = numpy.loadtxt(fname='data.csv', delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(5.0, 7.0))


axes1 = number_functionl:(3, 1, 1)
axes2 = number_water_points:(3, 1, 2)
axes3 = communityA:(3, 1, 3)

axes1.set_ylabel('average')
axes1.plot(data.mean(axis=0))

axes2.set_ylabel('max')
axes2.plot(data.max(axis=0))

axes3.set_ylabel('min')
axes3.plot(data.min(axis=0))

fig.tight_layout()

matplotlib.pyplot.savefig("plot.png")import matplotlib.pyplot as plt



