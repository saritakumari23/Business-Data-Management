import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Rajput_travels_dataset.csv")

# Compute descriptive statistics
desc_stats = df.describe()

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(desc_stats, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Descriptive Statistics Heatmap")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()
