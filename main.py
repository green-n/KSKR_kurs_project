import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns
import scipy.stats as stats


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




epsilon = 0.000000001

arr_to_solve = matrix_reading_from_file("./matrix2.txt")
print(arr_to_solve)
matrix_without_answers = arr_to_solve[:, :-1]
print(matrix_without_answers)
answers = arr_to_solve[:, -1]
print(answers)


# Solve the system
result = method_of_simple_iterations(matrix_without_answers, answers, epsilon)

print("----------------------------------------------------- RESULT -----------------------------------------------------")

print(result)


