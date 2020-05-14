import tkinter as tk
from PIL import Image, ImageTk

"""
This is how we can get the coordinates pressed on the image.
"""


class Board:
    def __init__(self):
        pass

    def mouseClick(self, event):
        print("clicked at ", event.x, event.y)

    def display(self):
        print("You got inside display")
        load = Image.open("Map.jpg")
        root = tk.Tk()
        w = tk.Canvas(root, width=load.width, height=load.height)
        w.pack()
        img = ImageTk.PhotoImage(load)
        w.create_image(0, 0, image=img, anchor="nw")
        w.bind("<Button-1>", self.mouseClick)
        root.mainloop()

#board = Board()
#board.display()
# display()
