import tkinter as tk
import math
import random
import numpy as np

canvas = None

SQUARE_LENGTH = 100
RADIUS = SQUARE_LENGTH / 2 - 5
POSITION = {"x": 8, "y": 8}
BORDER_WIDTH = 8
NUMBER = 4
LENGTH = SQUARE_LENGTH * NUMBER + BORDER_WIDTH * NUMBER
CELL_COLOR = '#cbbeb5'
BORDER_COLOR = '#b2a698'
PATTERNS = [[i, j] for i in range(4) for j in range(4)]

def set_field():
  canvas.create_rectangle(POSITION["x"], POSITION["y"], LENGTH + POSITION["x"], LENGTH + POSITION["y"], fill='#cbbeb5', width=BORDER_WIDTH, outline=BORDER_COLOR)

  for i in range(NUMBER - 1):
    x = POSITION["x"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    y = POSITION["y"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    canvas.create_line(x, POSITION["y"], x, LENGTH + POSITION["y"], width=BORDER_WIDTH, fill=BORDER_COLOR)
    canvas.create_line(POSITION["x"], y, LENGTH + POSITION["x"], y, width=BORDER_WIDTH, fill=BORDER_COLOR)

def create_canvas():
  root = tk.Tk()
  root.geometry(f"""{LENGTH + POSITION["x"] * 2}x{LENGTH + POSITION["y"] * 2}""")
  root.title("2048")
  canvas = tk.Canvas(root, width=(LENGTH + POSITION["x"]), height=(LENGTH + POSITION["y"]))
  canvas.place(x=0, y=0)

  return root, canvas

def set_number(num, x, y):
  center_x = POSITION["x"] + BORDER_WIDTH * x + BORDER_WIDTH / 2 + SQUARE_LENGTH * x + SQUARE_LENGTH / 2
  center_y = POSITION["y"] + BORDER_WIDTH * y + BORDER_WIDTH / 2 + SQUARE_LENGTH * y + SQUARE_LENGTH / 2
  canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill=CELL_COLOR, width=0)
  canvas.create_text(center_x, center_y, text=num, justify="center", font=("", 70), tag="count_text")
  

def set_array():
  i = 0
  j = 0
  array = [[0 for i in range(4)] for j in range(4)]
  print(array)
  for i, j in random.sample(PATTERNS, 2):
    array[j][i] = random.choice([2, 4])
  print(array)

  for i in range(4):
      for j in range(4):
        if array[j][i] != 0:
          set_number(array[j][i], i, j)

  array0 = np.array(array[0])
  array1 = np.array(array[1])
  array2 = np.array(array[2])
  array3 = np.array(array[3])
  array_all = array0 + array1 + array2 + array3
  print(np.array(array[0]))
  print(np.array(array[1]))
  print(np.array(array[2]))
  print(np.array(array[3]))
  print(array_all)




def operate(event):
  print(event.keysym)
  if (event.keysym == "Up") or (event.keysym =="Down"):
    canvas.delete("count_text")



def play():
  global canvas
  root, canvas = create_canvas()
  set_field()
  set_array()
  root.bind("<Key>", lambda event: operate(event))
  root.mainloop()

play()
