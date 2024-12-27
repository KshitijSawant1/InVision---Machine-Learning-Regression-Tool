import matplotlib.pyplot as plt
import numpy as np

# Data
traits = ["Fungible", "Non Consumable", "Portability", "High Durable", "Highly Divisible", "Secure (counterfeiting)", "Easily Translatable"]
gold_scores = [3, 2, 2, 3, 2, 2, 1]
paper_money_scores = [3, 3, 3, 2, 2, 2, 3]
crypto_scores = [3, 3, 3, 3, 3, 3, 3]

# Line Chart
x = np.arange(len(traits))

plt.plot(x, gold_scores, marker="o", label="Gold", color="gold")
plt.plot(x, paper_money_scores, marker="o", label="Paper Money", color="gray")
plt.plot(x, crypto_scores, marker="o", label="Crypto", color="blue")

plt.xticks(x, traits, rotation=45, ha='right', fontsize=10)
plt.title("Line Chart of Traits", fontsize=14)
plt.ylabel("Scores", fontsize=12)
plt.legend(fontsize=10)
plt.tight_layout()
fig = plt.gcf()  # Get current figure
fig.canvas.manager.set_window_title("Money Traits Analysis - Line Chart")

plt.show()
