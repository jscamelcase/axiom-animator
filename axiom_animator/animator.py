import matplotlib.pyplot as plt
import matplotlib.animation as animation
from typing import Union 
from matplotlib.figure import Figure
from matplotlib.axes import Axes


Number = Union[int, float]

def animate_cummtativity(a: Number, b: Number) -> None:
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=(6, 2)) #setting the figure size to 600px wide to 200px tall
    ax.set_xlim(0, max(a + b + 2, 10)) #configure the x axis limits
    ax.set_ylim(0,2) #configure the y axis limits
    ax.axis('off') #turns off axis ticks, labels, and grid lines for a clean visual

    #Bar1 = a, Bar2 = b
    bar1 = plt.Rectangle((0, 0.5), 0, 0.5, color="skyblue") #
    bar2 = plt.Rectangle((0, 0.5), 0, 0.5, color="orange")
