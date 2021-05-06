# This is a matrix calculator by Adam Tungtaiya Lukman
# as mini-project for CSC 201 Mini Project Assignment
# This calculator can be able to add, subtract, multiply, find transpose, find adjoint and inverse of matrices
# ID: FMS/0091/19

# These variable are used to save matrices created by the user
mat_a = []
mat_b = []
mat_c = []
mat_d = []


# Main thread of Program
def main():
    print('Matrix Calculator v1.0')
    while True:
        step = input('\n1. Create Matrix\n2. Add or Subtract Matrices\n3. Find Determinant\n4. Find Transpose\n5. '
                     'Find Adjoint\n6. Multiply Matrices\n7. Find Inverse\n8. Exit\n=> ')
        if step == '1':
            create_matrix()
        elif step == '2':
            add_subtract_matrix()
        elif step == '3':
            find_determinant()
        elif step == '4':
            find_transpose()
        elif step == '5':
            find_adjoint()
        elif step == '6':
            matrix_multiply()
        elif step == '7':
            inverse()
        elif step == '8':
            exit()
        else:
            print('Wrong Input. Try Again.')


# Creates a matrix of a specific order and saves it
def create_matrix():
    global mat_a
    global mat_b
    global mat_c
    global mat_d

    while True:
        mat_type = input('\nSelect which matrix you want to create.\n1. MatA\n2. MatB\n3. MatC\n4. MatD\n5. Go '
                         'Back\n=> ')
        if mat_type == '5':
            break
        elif mat_type != '1' and mat_type != '2' and mat_type != '3' and mat_type != '4':
            print('Wrong Input. Try Again')
            continue

        order = input('Select the order. \n1. 1 x 1\t2. 1 x 2\t3. 1 x 3\n4. 2 x 1\t5. 2 x 2\t6. 2 x 3\n7. 3 x 1\t8. 3 '
                      'x 2\t9. 3 x 3\n=> ')
        if order == '1':
            print('\n1 x 1 Matrix')
            matrix = '| a |'
            print(matrix)
            a = int(input('Enter a: '))
            if mat_type == '1':
                mat_a = [[a]]
            elif mat_type == '2':
                mat_b = [[a]]
            elif mat_type == '3':
                mat_c = [[a]]
            elif mat_type == '4':
                mat_d = [[a]]
        elif order == '2':
            print('\n1 x 2 Matrix')
            matrix = '| a  b |'
            print(matrix)
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            if mat_type == '1':
                mat_a = [[a, b]]
            elif mat_type == '2':
                mat_b = [[a, b]]
            elif mat_type == '3':
                mat_c = [[a, b]]
            elif mat_type == '4':
                mat_d = [[a, b]]
        elif order == '3':
            print('\n1 x 3 Matrix')
            matrix = '| a  b  c |'
            print(matrix)
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            c = int(input('Enter c: '))
            if mat_type == '1':
                mat_a = [[a, b, c]]
            elif mat_type == '2':
                mat_b = [[a, b, c]]
            elif mat_type == '3':
                mat_c = [[a, b, c]]
            elif mat_type == '4':
                mat_d = [[a, b, c]]
        elif order == '4':
            print('\n2 x 1 Matrix')
            matrix = '| a |\n| b |'
            print(matrix)
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            if mat_type == '1':
                mat_a = [[a], [b]]
            elif mat_type == '2':
                mat_b = [[a], [b]]
            elif mat_type == '3':
                mat_c = [[a], [b]]
            elif mat_type == '4':
                mat_d = [[a], [b]]
        elif order == '5':
            print('\n2 x 2 Matrix')
            matrix = '| a  b |\n| c  d |'
            print(matrix)
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            c = int(input('Enter c: '))
            d = int(input('Enter d: '))
            if mat_type == '1':
                mat_a = [[a, b], [c, d]]
            elif mat_type == '2':
                mat_b = [[a, b], [c, d]]
            elif mat_type == '3':
                mat_c = [[a, b], [c, d]]
            elif mat_type == '4':
                mat_d = [[a, b], [c, d]]
        elif order == '6':
            print('\n2 x 3 Matrix')
            matrix = '| a  b  c |\n| d  e  f |'
            print(matrix)
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            c = int(input('Enter c: '))
            d = int(input('Enter d: '))
            e = int(input('Enter e: '))
            f = int(input('Enter f: '))
            if mat_type == '1':
                mat_a = [[a, b, c], [d, e, f]]
            elif mat_type == '2':
                mat_b = [[a, b, c], [d, e, f]]
            elif mat_type == '3':
                mat_c = [[a, b, c], [d, e, f]]
            elif mat_type == '4':
                mat_d = [[a, b, c], [d, e, f]]
        elif order == '7':
            print('\n3 x 1 Matrix')
            matrix = '| a |\n| b |\n| c |'
            print(matrix)
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            c = int(input('Enter c: '))
            if mat_type == '1':
                mat_a = [[a, ], [b], [c]]
            elif mat_type == '2':
                mat_b = [[a, ], [b], [c]]
            elif mat_type == '3':
                mat_c = [[a, ], [b], [c]]
            elif mat_type == '4':
                mat_d = [[a, ], [b], [c]]
        elif order == '8':
            print('\n3 x 2 Matrix')
            matrix = '| a  b |\n| c  d |\n| e  f |'
            print(matrix)
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            c = int(input('Enter c: '))
            d = int(input('Enter d: '))
            e = int(input('Enter e: '))
            f = int(input('Enter f: '))
            if mat_type == '1':
                mat_a = [[a, b], [c, d], [e, f]]
            elif mat_type == '2':
                mat_b = [[a, b], [c, d], [e, f]]
            elif mat_type == '3':
                mat_c = [[a, b], [c, d], [e, f]]
            elif mat_type == '4':
                mat_d = [[a, b], [c, d], [e, f]]
        elif order == '9':
            print('\n3 x 3 Matrix')
            matrix = '| a  b  c |\n| d  e  f |\n| g  h  i |'
            print(matrix)
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            c = int(input('Enter c: '))
            d = int(input('Enter d: '))
            e = int(input('Enter e: '))
            f = int(input('Enter f: '))
            g = int(input('Enter g: '))
            h = int(input('Enter h: '))
            i = int(input('Enter i: '))
            if mat_type == '1':
                mat_a = [[a, b, c], [d, e, f], [g, h, i]]
            elif mat_type == '2':
                mat_b = [[a, b, c], [d, e, f], [g, h, i]]
            elif mat_type == '3':
                mat_c = [[a, b, c], [d, e, f], [g, h, i]]
            elif mat_type == '4':
                mat_d = [[a, b, c], [d, e, f], [g, h, i]]


# Calculates inverse
def inverse():
    while True:
        print('\n1. MatA\n2. MatB\n3. MatC\n4. MatD')
        print('Type exit to leave.')
        mat = input('Enter matrix to calculate inverse: ')
        if mat.lower() == 'exit':
            break

        if mat == '1':
            mat = mat_a
        elif mat == '2':
            mat = mat_b
        elif mat == '3':
            mat = mat_c
        elif mat == '4':
            mat = mat_d
        else:
            print('Wrong Input. Try Again.')
            continue

        if len(mat) == 0:
            print('Matrix is empty. Try Again.')
            continue

        if len(mat) != len(mat[0]):
            print('Matrix must be a square matrix.')
            continue

        new_matrix = transpose(adjoint(mat))

        n = len(mat)
        det = determinant(mat)

        if det == 0:
            print('This matrix cannot be inverted')
        else:
            for i in range(0, n):
                for j in range(0, n):
                    new_matrix[i][j] = new_matrix[i][j] / det

            print('\n' + display_matrix(new_matrix))


# Finds the adjoint of a matrix
def find_adjoint():
    while True:
        print('\n1. MatA\n2. MatB\n3. MatC\n4. MatD')
        print('Type exit to leave.')
        mat = input('Enter matrix to calculate adjoint: ')
        if mat.lower() == 'exit':
            break
        if mat == '1':
            mat = mat_a
        elif mat == '2':
            mat = mat_b
        elif mat == '3':
            mat = mat_c
        elif mat == '4':
            mat = mat_d
        else:
            print('Wrong Input. Try Again.')
            continue

        if len(mat) == 0:
            print('Matrix is empty. Try Again.')
            continue

        if len(mat) != len(mat[0]):
            print('Matrix must be a square matrix.')
            continue

        result = adjoint(mat)
        print('\n' + display_matrix(result))


# Calculate the adjoint of a matrix
def adjoint(matrix):
    new_matrix = []
    n = len(matrix)

    if n == 1:
        if matrix[0][0] != 0:
            new_matrix = [[1]]
        else:
            new_matrix = [[0]]
    else:
        for i in range(0, n):
            row = []
            for j in range(0, n):
                if (i + j) % 2 == 0:
                    counter = 1
                else:
                    counter = -1
                row += [counter * determinant(cofactor(matrix, i, j))]
            new_matrix += [row]

    return new_matrix


# Finds the determinant of a matrix
def find_determinant():
    while True:
        print('\n1. MatA\n2. MatB\n3. MatC\n4. MatD')
        print('Type exit to leave.')
        mat = input('Enter matrix to calculate determinant: ')
        if mat.lower() == 'exit':
            break
        if mat == '1':
            mat = mat_a
        elif mat == '2':
            mat = mat_b
        elif mat == '3':
            mat = mat_c
        elif mat == '4':
            mat = mat_d
        else:
            print('Wrong Input. Try Again.')
            continue

        if len(mat) == 0:
            print('Matrix is empty. Try Again.')
            continue

        result = determinant(mat)
        print(result)


# Calculates the determinant of a matrix
def determinant(matrix):
    n = len(matrix)
    total_sum = 0

    if n == 1 and len(matrix[0]):
        return matrix[0][0]
    else:
        for i in range(0, n):
            if i % 2 == 0:
                counter = 1
            else:
                counter = -1
            total_sum += counter * matrix[0][i] * determinant(cofactor(matrix, 0, i))

    return total_sum


# Finds the cofactor of a matrix
def cofactor(matrix, i, j):
    n = len(matrix)
    new_matrix = matrix[0:i] + matrix[i + 1:n]
    for row_index in range(0, n - 1):
        new_matrix[row_index] = new_matrix[row_index][0:j] + new_matrix[row_index][j + 1:n]

    return new_matrix


# Finds the transpose of a matrix
def find_transpose():
    while True:
        print('\n1. MatA\n2. MatB\n3. MatC\n4. MatD')
        print('Type exit to leave.')
        mat = input('Enter matrix to calculate transpose: ')
        if mat.lower() == 'exit':
            break
        if mat == '1':
            mat = mat_a
        elif mat == '2':
            mat = mat_b
        elif mat == '3':
            mat = mat_c
        elif mat == '4':
            mat = mat_d
        else:
            print('Wrong Input. Try Again.')
            continue

        if len(mat) == 0:
            print('Matrix is empty. Try Again.')
            continue

        result = transpose(mat)
        print('\n' + display_matrix(result))


# Calculates the transpose of a matrix
def transpose(matrix):
    new_matrix = []
    n = len(matrix[0])
    m = len(matrix)

    for i in range(0, n):
        row = []
        for j in range(0, m):
            row += [matrix[j][i]]
        new_matrix += [row]

    return new_matrix


# Finds dot_product of two vectors
# This function is used in matrix_multiply function
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        print('Cannot dot product two vectors of different dimensions')
    else:
        n = len(vector1)
        add = 0
        for i in range(0, n):
            add += (vector1[i] * vector2[i])
        return add


# Finds the multiplication of two matrices
def matrix_multiply():
    count = 0
    result = ''

    while True:
        print('\n1. MatA\n2. MatB\n3. MatC\n4. MatD')
        if count == 1:
            print('5. Result')

        print('Type exit to leave.')
        mat_1 = input('Enter first matrix: ')
        if mat_1.lower() == 'exit':
            break
        mat_2 = input('Enter second matrix: ')
        if mat_2.lower() == 'exit':
            break

        if mat_1 == '1':
            mat_1 = mat_a
        elif mat_1 == '2':
            mat_1 = mat_b
        elif mat_1 == '3':
            mat_1 = mat_c
        elif mat_1 == '4':
            mat_1 = mat_d
        elif mat_2 == '5':
            mat_2 = result
        else:
            print('Wrong Input. Try Again.')
            continue

        if mat_2 == '1':
            mat_2 = mat_a
        elif mat_2 == '2':
            mat_2 = mat_b
        elif mat_2 == '3':
            mat_2 = mat_c
        elif mat_2 == '4':
            mat_2 = mat_d
        elif mat_2 == '5':
            mat_2 = result
        else:
            print('Wrong Input. Try Again.')
            continue

        if len(mat_1) == 0 or len(mat_2) == 0:
            print('Matrix is empty. Try Again.')
            continue

        if len(mat_1[0]) != len(mat_2):
            print("Cannot multiply matrices of these dimensions")
        else:
            trans = transpose(mat_2)
            n = len(mat_2[0])
            m = len(mat_1)
            new_matrix = []
            for j in range(0, m):
                new_matrix.append([])
            for i in range(0, n):
                for j in range(0, m):
                    new_matrix[j].append(dot_product(mat_1[j], trans[i]))
            print('\n' + display_matrix(new_matrix))
            result = new_matrix
            count = 1


# Finds the sum or the subtraction of a matrix
def add_subtract_matrix():
    mode = input('\n1. Add Matrices\n2. Subtract Matrices\n=> ')
    if mode == '1':
        result = []
        count = 0
        while True:
            print('\n1. MatA\n2. MatB\n3. MatC\n4. MatD')
            if count == 1:
                print('5. Result\n')
            print('Type exit to leave.')
            mat_1 = input('Enter First Matrix: ')
            if mat_1.lower() == 'exit':
                break
            mat_2 = input('Enter Second Matrix: ')
            if mat_2.lower() == 'exit':
                break

            if mat_1 == '1':
                mat_1 = mat_a
            elif mat_1 == '2':
                mat_1 = mat_b
            elif mat_1 == '3':
                mat_1 = mat_c
            elif mat_1 == '4':

                mat_1 = mat_d
            elif count == 1 and mat_1 == '5':
                mat_1 = result
            else:
                print('Wrong Input. Try Again.')
                continue

            if mat_2 == '1':
                mat_2 = mat_a
            elif mat_2 == '2':
                mat_2 = mat_b
            elif mat_2 == '3':
                mat_2 = mat_c
            elif mat_2 == '4':
                mat_2 = mat_d
            elif count == 1 and mat_2 == '5':
                mat_2 = result
            else:
                print('Wrong Input. Try Again.')
                continue

            if len(mat_1) == 0 or len(mat_2) == 0:
                print('First or Second Matrix has no values. Try Again.')
                continue

            if len(mat_1) != len(mat_2) or len(mat_1[0]) != len(mat_2[0]):
                print('You can only add matrices of the same dimensions and size. Try again')
                continue

            new_matrix = []
            for row1, row2 in zip(mat_1, mat_2):
                new_row = []
                for item1, item2 in zip(row1, row2):
                    new_item = item1 + item2
                    new_row.append(new_item)
                new_matrix.append(new_row)
            result = new_matrix
            print('Answer: ')
            print('\n' + display_matrix(new_matrix))
            count = 1
    elif mode == '2':
        result = []
        count = 0
        while True:
            print('\n1. MatA\n2. MatB\n3. MatC\n4. MatD')
            if count == 1:
                print('5. Result\n')
            mat_1 = input('Enter First Matrix: ')
            if mat_1.lower() == 'exit':
                break
            mat_2 = input('Enter Second Matrix: ')
            if mat_2.lower() == 'exit':
                break

            if mat_1 == '1':
                mat_1 = mat_a
            elif mat_1 == '2':
                mat_1 = mat_b
            elif mat_1 == '3':
                mat_1 = mat_c
            elif mat_1 == '4':
                mat_1 = mat_d
            elif count == 1 and mat_1 == '5':
                mat_1 = result
            else:
                print('Wrong Input. Try Again.')
                continue

            if mat_2 == '1':
                mat_2 = mat_a
            elif mat_2 == '2':
                mat_2 = mat_b
            elif mat_2 == '3':
                mat_2 = mat_c
            elif mat_2 == '4':
                mat_2 = mat_d
            elif count == 1 and mat_2 == '5':
                mat_2 = result
            else:
                print('Wrong Input. Try Again.')
                continue

            if len(mat_1) == 0 or len(mat_2) == 0:
                print('First or Second Matrix has no values. Try Again.')
                continue

            if len(mat_1) != len(mat_2) or len(mat_1[0]) != len(mat_2[0]):
                print('You can only subtract matrices of the same dimensions and size. Try again')
                continue

            new_matrix = []
            for row1, row2 in zip(mat_1, mat_2):
                new_row = []
                for item1, item2 in zip(row1, row2):
                    new_item = item1 - item2
                    new_row.append(new_item)
                new_matrix.append(new_row)
            result = new_matrix
            print('Answer: ')
            print('\n' + display_matrix(new_matrix))
            count = 1


# Return a formatted string of a matrix
def display_matrix(mat):
    mat_str = ''
    order = len(mat)
    count = 0
    length = 1

    for i in mat:
        for digit in i:
            num = len(str(digit))
            if length < num:
                length = num

    for m in mat:
        mat_str += '|'
        for line in m:
            mat_str += ' ' + str(line).rjust(length)
        mat_str += ' |'
        count += 1
        if count < order:
            mat_str += '\n'
    return mat_str


# Start of program
main()
