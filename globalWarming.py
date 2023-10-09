import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-3.14, 3.14, 360)
y = np.linspace(-3.14, 3.14, 360)

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot')
plt.show()