import matplotlib.pyplot as plt
import numpy as np

# Data
traits = ["Fungible", "Non Consumable", "Portability", "High Durable", "Highly Divisible", "Secure (counterfeiting)", "Easily Translatable"]
gold_scores = [3, 2, 2, 3, 2, 2, 1]
paper_money_scores = [3, 3, 3, 2, 2, 2, 3]
crypto_scores = [3, 3, 3, 3, 3, 3, 3]

# Bar Chart
x = np.arange(len(traits))
width = 0.25

plt.bar(x - width, gold_scores, width, label='Gold', color='gold')
plt.bar(x, paper_money_scores, width, label='Paper Money', color='gray')
plt.bar(x + width, crypto_scores, width, label='Crypto', color='blue')

plt.xticks(x, traits, rotation=45, ha='right', fontsize=10)
plt.title("Bar Chart of Traits", fontsize=14)
plt.ylabel("Scores", fontsize=12)
plt.legend(fontsize=10)
plt.tight_layout()

# Change the window title
fig = plt.gcf()  # Get current figure
fig.canvas.manager.set_window_title("Money Traits Analysis - Bar Chart")

plt.show()
