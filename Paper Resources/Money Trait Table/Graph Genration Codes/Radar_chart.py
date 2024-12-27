import matplotlib.pyplot as plt
import numpy as np

# Data
traits = ["Fungible", "Non Consumable", "Portability", "High Durable", "Highly Divisible", "Secure (counterfeiting)", "Easily Translatable"]
gold_scores = [3, 2, 2, 3, 2, 2, 1]
paper_money_scores = [3, 3, 3, 2, 2, 2, 3]
crypto_scores = [3, 3, 3, 3, 3, 3, 3]

# Radar Chart
def radar_chart(data, labels, title):
    categories = traits
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    for i, d in enumerate(data):
        d += d[:1]
        ax.plot(angles, d, label=labels[i], linewidth=2, linestyle='solid')
        ax.fill(angles, d, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["Low", "Moderate", "High"], fontsize=10)
    ax.set_ylim(0, 3)
    ax.set_title(title, fontsize=14)
    ax.legend(fontsize=10, loc='upper right')
    fig.canvas.manager.set_window_title("Money Traits Analysis - Radar Chart")
    plt.show()

radar_chart([gold_scores, paper_money_scores, crypto_scores], ["Gold", "Paper Money", "Crypto"], "Radar Chart of Traits")
