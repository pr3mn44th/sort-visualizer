from tkinter import *
from tkinter import ttk
import numpy as np
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort


# Initialising Tkinter
root = Tk()
root.title('Sort Visualizer')
root.maxsize(700, 600)
root.config(bg='lightblue')


# Variables
selected_alg = StringVar()
data = []


# Functions
# Given the data list and correspoding color list, plots bar graph on canvas
def plot_data(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()


# Based on the user values for min, max and size; creates a list of random values
def generate():
    global data
    minVal = int(min_scale.get())
    maxVal = int(max_scale.get())
    size = int(size_scale.get())
    if(minVal > maxVal):
        minVal, maxVal = maxVal, minVal
    data = list(np.random.randint(minVal, maxVal, size))
    plot_data(data, ['salmon' for x in range(len(data))])


def start_sort():
    global data
    if not data:
        return
    s = menu.get()
    if s == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, plot_data, speed_scale.get())
    elif s == 'Bubble Sort':
        bubble_sort(data, plot_data, speed_scale.get())
    elif s == 'Merge Sort':
        merge_sort(data, plot_data, speed_scale.get())
    plot_data(data, ['green' for x in range(len(data))])


# Base Layout
interface = Frame(
    root,
    width=600,
    height=200,
    bg='lightblue'
)
interface.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(
    root,
    width=600,
    height=380,
    bg='lightblue'
)
canvas.grid(row=1, column=0, padx=10, pady=10)

# Algorithm Selection Label
Label(
    interface,
    text="Select Algorithm: ",
    bg='lightblue'
).grid(row=0, column=0, padx=5, pady=5, sticky=W)


# Algorithm Selection Dropdown
menu = ttk.Combobox(
    interface,
    textvariable=selected_alg,
    values=[
        'Bubble Sort',
        'Merge Sort',
        'Quick Sort'
    ]
)
# Sets the default value to the first Dropdown value
menu.current(0)
menu.grid(row=0, column=1, padx=5, pady=5)


# Dataset Size Scaler
size_scale = Scale(
    interface,
    from_=3,
    to=10,
    resolution=1,
    orient=HORIZONTAL,
    label="Dataset Size",
    bg='salmon'
)
size_scale.grid(row=0, column=2, padx=5, pady=5)


# Speed Value Scaler
speed_scale = Scale(
    interface,
    from_=0.1,
    to=3.0,
    length=100,
    digits=2,
    resolution=0.2,
    orient=HORIZONTAL,
    label="Speed Selector",
    bg='salmon'
)
speed_scale.grid(row=1, column=0, padx=5, pady=5)


# Minimum Value Scaler
min_scale = Scale(
    interface,
    from_=0,
    to=100,
    resolution=1,
    orient=HORIZONTAL,
    label="Minimum Value",
    bg='salmon'
)
min_scale.grid(row=1, column=1, padx=5, pady=5)


# Maximum Value Scaler
max_scale = Scale(
    interface,
    from_=10,
    to=100,
    resolution=1,
    orient=HORIZONTAL,
    label="Maximum Value",
    bg='salmon'
)
max_scale.grid(row=1, column=2, padx=5, pady=5)


# Start Button
Button(
    interface,
    text="   Start   ",
    command=start_sort,
    bg='salmon'
).grid(row=0, column=3, padx=5, pady=5)


# Generate Button
Button(
    interface,
    text="Generate",
    command=generate,
    bg='salmon'
).grid(row=1, column=3, padx=5, pady=5)


root.mainloop()
