import numpy as np
import pandas as pd

matrix = []
while len(matrix) != 9:
    try:
        matrix = list(input("Print 9 numbers separated by spaces: ").split())
        matrix = np.array(matrix).reshape(3,3).astype(float)
        break
    except Exception as exc:
        print("Invalid input, please try again")
        matrix = []
        continue

def calculate(matrix):
    calculations ={}
    calculations['mean'] = [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), np.mean(matrix)]
    calculations['variance'] = [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), np.var(matrix)]
    calculations['standard deviation'] = [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), np.std(matrix)]
    calculations['max'] = [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), np.max(matrix)]
    calculations['min'] = [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), np.min(matrix)]
    calculations['sum'] = [list(np.sum  (matrix, axis=0)), list(np.sum(matrix, axis=1)), np.sum(matrix)]
    return calculations

calculation = calculate(matrix)
df = pd.DataFrame(calculation, index=['axis 1', 'axis 0', 'flattened'])
print(df)