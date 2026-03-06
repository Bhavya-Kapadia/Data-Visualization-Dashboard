import matplotlib.pyplot as plt
import numpy as np

y = np.array([2000,2500,3000,2500])
l = ["Football","Cricket Kit","Cricket Bat","Basket Ball"]

plt.title("Product Distribution FY 2024-25")
plt.pie(y,labels=l,startangle=90,autopct='%1.1f%%')
plt.gca().set_facecolor('#1F6A73')
plt.show()
