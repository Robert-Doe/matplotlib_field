import numpy as np
import matplotlib.pyplot as plt

x=np.arange(20) +1
print(x)
y=2*x
print(y)
plt.scatter(x,y)
plt.show()
plt.bar(x,y)
plt.show()
plt.boxplot(x,y)
plt.show()