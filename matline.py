import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Januar-23", "February-23", "March-23", "April-23","May-23","June-23","July-23","August-23","September-23","October-23","November-23","December-23","January-24", "February-24", "March-24", "April-24","May-24","June-24","July-24","August-24","September-24","October-24","November-24","December-24"])
y = np.array([30000, 80000, 70000, 70000, 20000, 40000, 60000, 70000, 80000, 90000,75000,72000,56000, 58000, 70000, 90000, 80000, 80000, 45000, 40700, 41000, 31000,42000,82000])

plt.bar(x,y)
plt.title("FY 2023-24 Monthly Sales(Units sold)")

plt.xticks(rotation=90)
plt.show()