import matplotlib.pyplot as plt

# Data
labels = ['Delhi', 'Mumbai', 'Ahemdabad', 'Chennai']
sales = [12000, 15000, 9000, 8000]  # Example values

# Colors (similar to your image)
colors = ['#9C7BD8', '#35C0C7', '#8FD14F', '#F7C600']

# Create figure
plt.figure(figsize=(6, 5), facecolor='white')

# Create donut chart
wedges, texts = plt.pie(
    sales,
    labels=labels,
    colors=colors,
    startangle=90,
    wedgeprops={'width': 0.4}  # Makes it donut
)

# Title
plt.title("Sales in Cities", color='black', fontsize=14)

# Set background color
plt.gca().set_facecolor('white')

# Make text white
for text in texts:
    text.set_color('black')

plt.show()