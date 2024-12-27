import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap

# Data
traits = ["Fungible", "Non Consumable", "Portability", "High Durable", "Highly Divisible", "Secure (counterfeiting)", "Easily Translatable"]
gold_scores = [3, 2, 2, 3, 2, 2, 1]
paper_money_scores = [3, 3, 3, 2, 2, 2, 3]
crypto_scores = [3, 3, 3, 3, 3, 3, 3]

# Heatmap
data = np.array([gold_scores, paper_money_scores, crypto_scores])
cmap = ListedColormap(["lightyellow", "lightblue", "lightgreen"])

plt.figure(figsize=(8, 6))
sns.heatmap(data, cmap=cmap, annot=True, fmt="d", xticklabels=traits, yticklabels=["Gold", "Paper Money", "Crypto"])
plt.title("Heatmap of Traits", fontsize=14)
plt.tight_layout()
fig = plt.gcf() 
fig.canvas.manager.set_window_title("Money Traits Analysis - Heat Map")

plt.show()
