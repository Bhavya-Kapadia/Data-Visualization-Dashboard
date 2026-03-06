import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Football", "Cricket Bat", "Basket Ball", "Cricket Kit"])
y = np.array([5000, 8000, 2500, 3000])
plt.title("FY 2024-25 Sales(Units)")

plt.bar(x,y)
plt.show()