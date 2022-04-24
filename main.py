matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
b_vector = [2, 6, 5]
variables = []
epsilon = 0.00001

b_vector_copy = b_vector.copy()
max_iterations = 50


def init():
    b_vector_copy.clear()
    for var in b_vector:
        b_vector_copy.append(var)

    if not check_diagonal_dominance(matrix):
        print("The matrix is not diagonally dominant, calling fix_dominance().")
        temp_matrix = fix_dominance(matrix)
    else:
        temp_matrix = copy_matrix(matrix)

    matrix_copy = copy_matrix(temp_matrix)

    variables.clear()
    for _ in matrix:
        variables.append(0)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                matrix_copy[i][j] /= (temp_matrix[i][i] * -1)
        matrix_copy[i][i] = 0
        b_vector_copy[i] /= temp_matrix[i][i]

    return matrix_copy


def copy_matrix(mat):
    mat_copy = []
    for row in mat:
        mat_copy.append(row.copy())
    return mat_copy


def check_diagonal_dominance(mat):
    for i in range(len(mat)):
        d_sum = 0
        for j in range(len(mat[i])):
            d_sum += abs(mat[i][j])
        d_sum -= abs(mat[i][i])
        if d_sum > abs(mat[i][i]):
            return False
    return True


def fix_dominance(mat):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            mat_copy = copy_matrix(mat)
            mat_copy[i], mat_copy[j] = mat_copy[j], mat_copy[i]
            if check_diagonal_dominance(mat_copy):
                b_vector_copy[i], b_vector_copy[j] = b_vector_copy[j], b_vector_copy[i]
                print("The matrix is now diagonally dominant.")
                return mat_copy
    print("Could not make the matrix diagonally dominant, we will try the method anyway.")
    return matrix


def jacobi_method():
    mat = init()

    for i in range(max_iterations):
        variables_copy = variables.copy()

        for n in range(len(variables)):
            variable_sum = 0
            for j in range(len(variables)):
                variable_sum += variables_copy[j] * mat[n][j]
            variable_sum += b_vector_copy[n]
            variables[n] = variable_sum

        print("{}. {}".format(i + 1, variables))
        if compare_iterations(variables_copy, variables):
            print("Result found, it took {} iterations.".format(i + 1))
            break
        elif i == max_iterations - 1:
            print("Could not find result after {} iterations.".format(i + 1))


def gauss_seidel_method():
    mat = init()

    for i in range(max_iterations):
        variables_copy = variables.copy()

        for n in range(len(variables)):
            variable_sum = 0
            for j in range(len(variables)):
                variable_sum += variables[j] * mat[n][j]
            variable_sum += b_vector_copy[n]
            variables[n] = variable_sum

        print("{}. {}".format(i + 1, variables))
        if compare_iterations(variables_copy, variables):
            print("Result found, it took {} iterations.".format(i + 1))
            break
        elif i == max_iterations - 1:
            print("Could not find result after {} iterations.".format(i + 1))


def compare_iterations(res1, res2):
    for i in range(len(res1)):
        if not (abs(res1[i] - res2[i]) < epsilon):
            return False
    return True


for _ in range(2):
    user_input = int(input("1. Gauss Seidel Method\n2. Jacobi Method\nEnter selection: "))

    if user_input == 1:
        gauss_seidel_method()
    elif user_input == 2:
        jacobi_method()
    else:
        print("Incorrect input.")
    print()