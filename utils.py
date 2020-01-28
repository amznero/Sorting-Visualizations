import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def generate_data(rows=100, cols=300):
    data = np.random.randn(rows, cols)
    return data

def visulization(data):
    sns.heatmap(data, cmap=sns.color_palette("Blues"))
    plt.show()

