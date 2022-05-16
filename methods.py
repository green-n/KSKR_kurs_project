#from tkinter import filedialog

import numpy as np
#import tkinter as tk
# Load the data
def matrix_reading_from_file(path_to_file):
    data = []
    with open(path_to_file, "r") as matrix:
        for line in matrix:
            data.append([float(x) for x in line.split()])
    sole_arr = np.asarray(data)
    return sole_arr

def method_of_simple_iterations(matrix_without_answers, answers, epsilon):
    size_of_answers = len(answers)
    res = []

    for i in range(size_of_answers):
        res.append(answers[i]/matrix_without_answers[i][i])

    is_bigger_than_epsilon = True
    Temp_arr_of_answers = np.copy(res)

    while is_bigger_than_epsilon:
        for i in range(size_of_answers):
            Temp_arr_of_answers[i] = answers[i]/matrix_without_answers[i][i]
            for j in range(size_of_answers):
                if j != i:
                    Temp_arr_of_answers[i] -= matrix_without_answers[i][j]/matrix_without_answers[i][i]*res[j]

        for i in range(size_of_answers):
            if abs(Temp_arr_of_answers[i] - res[i]) > epsilon:
                is_bigger_than_epsilon = True
            else:
                is_bigger_than_epsilon = False

        res = np.copy(Temp_arr_of_answers)

    return res

def save_result_as_file(result, path_to_file):
    with open(path_to_file, "w") as file:
        for i in range(len(result)):
            file.write(str(result[i]) + "\n")