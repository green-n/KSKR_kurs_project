from tkinter import filedialog

import numpy as np
# import methods.py
import methods as m
import tkinter as tk
import os
import tkinter as tk
from tkinter import filedialog, Text, messagebox, ttk, scrolledtext, Menu, END
import os

file_path = ""
height_of_array = 3
# function for input of array from application
def input_array():

    matrix = []
    multiplier = int(20*height_of_array/3)
    small_frame = tk.Frame(frame, width=10 * multiplier, height=10 * multiplier, bg="lightgray")
    small_frame.pack()
    TextBox = tk.Text(small_frame, height=height_of_array, width=multiplier)
    TextBox.pack()
    check = False
    saveButton = tk.Button(small_frame, text="Save", command=lambda: save_array(TextBox,small_frame))
    # TextBox.bind("<Return>", lambda event: save_array(TextBox))
    # saveButton.bind("<Button-1>", lambda event: small_frame.destroy())

    saveButton.pack()
    #destroy the save button after it is clicked






def save_array(TextBox, small_frame):

    matrix = []
    matrix = TextBox.get("1.0", "end-1c")
    matrix = matrix.split("\n")
    matrix = [x.split(" ") for x in matrix]
    matrix = [list(map(float, x)) for x in matrix]
    # convert to numpy array
    matrix = np.array(matrix)
    print(matrix)
    addFile.matrix = matrix
    #destroy the save button after it is clicked
    small_frame.destroy()
    matrixLabel = tk.Label(frame, text=matrix)
    matrixLabel.pack()



def addFile():
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("all files", "*.*"), ("text files", "*.txt")))
    matrix = m.matrix_reading_from_file(file_path)
    lableMatrix = tk.Label(frame, text=matrix)
    lableMatrix.pack()
    addFile.matrix = matrix
    addFile.path = file_path
    # print(matrix)

def solveEquation():
    matrix = addFile.matrix

    epsilon = 0.00001
    result = []
    arr_to_solve = matrix
    print(arr_to_solve)
    matrix_without_answers = arr_to_solve[:, :-1]
    answers = arr_to_solve[:, -1]
    result = m.method_of_simple_iterations(matrix_without_answers, answers,epsilon)
    print(result)
    lableResult = tk.Label(frame, text="Result: ")
    lableResult.pack()
    iterResult = tk.Label(frame, text=result)
    iterResult.pack()
    solveEquation.result = result

def save_result(result):
    file_path = filedialog.asksaveasfilename(initialdir=addFile.path, title="Save file", filetypes=(("all files", "*.*"), ("text files", "*.txt")), defaultextension=".txt")
    m.save_result_as_file(result, file_path)




root = tk.Tk()
root.title("Simple iteration method")

canvas = tk.Canvas(root, width=900, height=600, bg='gray')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.7,relx=0.1, rely=0.05)


openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="black", command=addFile)
openFile.pack()
solve = tk.Button(root, text="Solve", padx=10, pady=5, fg="white", bg="black", command=solveEquation)
solve.pack()
inputFromKeyboard = tk.Button(root, text="Input from keyboard", padx=10, pady=5, fg="white", bg="black", command=input_array)
inputFromKeyboard.pack()
saveResultAsFile = tk.Button(root, text="Save result as file", padx=10, pady=5, fg="white", bg="black", command=lambda: save_result(solveEquation.result))
saveResultAsFile.pack()
defaultSave = tk.Button(root, text="Default save", padx=10, pady=5, fg="white", bg="black", command=lambda: m.save_result_as_file(solveEquation.result, addFile.path + "result.txt"))
defaultSave.pack()
root.mainloop()

































# epsilon = 0.000000001
# print("----------------------------------------------------- MATRIX -----------------------------------------------------")
# arr_to_solve = m.matrix_reading_from_file("./matrix1.txt")
# print(arr_to_solve)
# matrix_without_answers = arr_to_solve[:, :-1]
#
# answers = arr_to_solve[:, -1]
#
#
#
# # Solve the system
# result = m.method_of_simple_iterations(matrix_without_answers, answers, epsilon)
#
# print("----------------------------------------------------- RESULT -----------------------------------------------------")
#
# print(result)


