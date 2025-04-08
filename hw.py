

# hw - Choice-based matrix operation system
import numpy as np

rows = int(input("Rows: "))
cols = int(input("Columns: "))

def get_matrix(name):
    print(f"Enter elements for {name} ({rows} rows, {cols} numbers per row):")
    matrix = []
    for i in range(rows):
        while True:
            row = input(f"Row {i+1}: ").split()
            if len(row) != cols:
                print(f"Please enter exactly {cols} numbers.")
            else:
                matrix.append(list(map(int, row)))
                break
    return np.array(matrix)

A = get_matrix("Matrix A")
B = get_matrix("Matrix B")

op = input("Enter operation (+ or -): ")

if op == '+':
    print("Result:\n", A + B)
elif op == '-':
    print("Result:\n", A - B)
else:
    print("Invalid operation.")