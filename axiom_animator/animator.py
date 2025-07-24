import matplotlib.pyplot as plt
import matplotlib.animation as animation
from typing import Union, Any, List
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.patches import Rectangle
from matplotlib.text import Text 
import matplotlib.patches as mpatches 
import matplotlib. text as mtext
from matplotlib.animation import FuncAnimation


Number = Union[int, float]

def animate_commutativity(a: Number, b: Number) -> None:
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=(6, 2)) #setting the figure size to 600px wide to 200px tall
    ax.set_xlim(0, max(a + b + 2, 10)) #configure the x axis limits
    ax.set_ylim(0,2) #configure the y axis limits
    ax.axis('off') #turns off axis ticks, labels, and grid lines for a clean visual

    #Bar1 = a, #Bar2 = b
    bar1: Rectangle = plt.Rectangle((0, 0.5), 0, 0.5, color="skyblue") #arg1 (x, y) coordinates; arg#2 width, arg#3 height, arg#4 color 
    bar2: Rectangle = plt.Rectangle((0, 0.5), 0, 0.5, color="orange") #same as above but for second arugment/number

    #these two lines add the rectangle (bars) to the Axes object so that they will be drwan when the plot is rendered 
    ax.add_patch(bar1)
    ax.add_patch(bar2) 

    text: Text = ax.text(0, 1.2, "", fontsize=12) #adds the text label above the bars, the label dymically updating

    def update(frame: int) -> List[mpatches.Patch | mtext.Text]:
        if frame < 10:
            # Show a + b
            bar1.set_width(a) #sets the bar's width
            bar1.set_xy((1, 0.5)) # moves the bar via (x, y)
            bar2.set_width(b) #sets the bar's width
            bar2.set_xy((1 + a, 0.5)) #moves the bar via (x, y)
            text.set_text(f"{a} + {b} = {b + a}")
        else:
            # Show b + a
            bar1.set_width(b)
            bar1.set_xy((1, 0.5))
            bar2.set_width(a)
            bar2.set_xy((1 + b, 0.5))
            text.set_text(f"{b} + {a} = {b + a}")
        
        return [bar1, bar2, text]
    
    ani: FuncAnimation = animation.FuncAnimation (
        fig, 
        update,
        frames=range(20),
        interval=500,
        blit=True,
        repeat=True,
    )

    plt.show()

if __name__ == "__main__":
        animate_commutativity(3, 5)







