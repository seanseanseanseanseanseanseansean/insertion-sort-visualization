import gradio as gr
import matplotlib.pyplot as plt
import time
import random
from matplotlib.patches import Patch


#generate random array for sorting later
def rand_array(n):
    arr = []
    for i in range(n):
        arr += [random.randint(1,100)]
    return arr


#define function to display the values of an array as a bar chart

def show_bars(arr, green = 0, blue = 0, state="Insertion Sort Visualization"):

    fig, ax = plt.subplots() #initialize plot

    #define positions of bars
    x = []
    for i in range(len(arr)):
        x += [i * 1.6]
        
    #define widths of bars
    widths = [0.8] * len(arr)


    #define colors of bars
    #start by setting all to "red"
    colors = ["red"] * len(arr)

    #if green isn't set to zero, we must set sorted bars to "green"
    if green:
        for i in range(green):
            colors[i] = "green"

    #if blue isn't zero, we must set the blue bar to "blue"
    if blue:
        colors[blue - 1] = "blue"

    #define legend
    legend_items = [
    Patch(facecolor='red', label='Unsorted'),
    Patch(facecolor='blue', label='Checking'),
    Patch(facecolor='green', label='Sorted'),
    ]
    ax.legend(handles=legend_items, loc="upper left")

    #place values from array above corresponding bar
    for i, val in enumerate(arr):
        ax.text(i * 1.6, val + 2, str(val), ha="center", fontsize=8)
    
    # hide axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    #set title to current state of algorithm
    ax.set_title(state)

    #draw the bar plot
    ax.bar(x, arr, widths, color = colors)

    return fig


#define the insertion sort function with each step rendering a new figure for the visualization
def insertion_sort(n, speed):

    #make sure input is valid
    try:
        size = int(n)
        if size <= 0:
            raise gr.Error("Please enter a positive integer.")
    except:
        raise gr.Error("Please enter a positive integer.")

    #set animation speed
    sleep = 1 - float(speed)

    #generate random array for sorting
    arr = rand_array(int(n))

    yield show_bars(arr, state="Starting")
    time.sleep(sleep)

    #insertion sort with each step yielding current state of graph
    for i in range(len(arr)):
        a = i
        time.sleep(sleep)
        yield show_bars(arr, i + 1, a + 1, state="Checking")
        while a != 0 and arr[a - 1] > arr[a]:
            arr[a], arr[a - 1] = arr[a - 1], arr[a]
            a = a - 1
            time.sleep(sleep)
            yield show_bars(arr, i + 1, a + 1, state="Swapping")
        time.sleep(sleep)
        yield show_bars(arr, i + 1, state="Inserted")
        time.sleep(sleep)
    yield show_bars(arr, len(arr), state="Sorted")

#generate gradio block to display the visualization
with gr.Blocks(title="Insertion Sort Visualization") as visualization:
    gr.Markdown("# Insertion Sort Visualization")
    arr_size = gr.Textbox(label="Number of Values", placeholder="Please enter the number of values for the visualization")
    speed = gr.Slider(0.01, 1.0, value=0.5, label="Animation Speed")
    btn = gr.Button("run")
    out = gr.Plot()
    btn.click(inputs=[arr_size, speed], outputs=out, fn = insertion_sort)

visualization.launch()

