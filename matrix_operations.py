import numpy as np

print("=" * 45)
print("        MATRIX OPERATIONS TOOL")
print("=" * 45)

# Get matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# -----------------------------
# Input Matrix A
# -----------------------------
print("\nEnter elements of Matrix A:")
A = []

for i in range(rows):
    while True:
        row = list(map(float, input(f"Row {i + 1}: ").split()))

        if len(row) == cols:
            A.append(row)
            break
        else:
            print(f"❌ Please enter exactly {cols} values.")

A = np.array(A)

# -----------------------------
# Input Matrix B
# -----------------------------
print("\nEnter elements of Matrix B:")
B = []

for i in range(rows):
    while True:
        row = list(map(float, input(f"Row {i + 1}: ").split()))

        if len(row) == cols:
            B.append(row)
            break
        else:
            print(f"❌ Please enter exactly {cols} values.")

B = np.array(B)

# Display Matrices
print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# -----------------------------
# Menu
# -----------------------------
while True:

    print("\n" + "=" * 40)
    print("           MATRIX MENU")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose of Matrix A")
    print("5. Transpose of Matrix B")
    print("6. Determinant of Matrix A")
    print("7. Determinant of Matrix B")
    print("8. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            print("\nResult:")
            print(A + B)
            print("-" * 40)

        elif choice == 2:
            print("\nResult:")
            print(A - B)
            print("-" * 40)

        elif choice == 3:
            if A.shape[1] == B.shape[0]:
                print("\nResult:")
                print(np.matmul(A, B))
            else:
                print("\n❌ Matrix multiplication cannot be performed.")
            print("-" * 40)

        elif choice == 4:
            print("\nTranspose of Matrix A:")
            print(A.T)
            print("-" * 40)

        elif choice == 5:
            print("\nTranspose of Matrix B:")
            print(B.T)
            print("-" * 40)

        elif choice == 6:
            if rows == cols:
                print("\nDeterminant of Matrix A:")
                print(np.linalg.det(A))
            else:
                print("\n❌ Determinant can only be calculated for square matrices.")
            print("-" * 40)

        elif choice == 7:
            if rows == cols:
                print("\nDeterminant of Matrix B:")
                print(np.linalg.det(B))
            else:
                print("\n❌ Determinant can only be calculated for square matrices.")
            print("-" * 40)

        elif choice == 8:
            print("\n" + "=" * 45)
            print(" Thank you for using Matrix Operations Tool 😊")
            print("=" * 45)
            break

        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 8.")

    except ValueError:
        print("\n❌ Invalid input! Please enter a numeric choice.")