# Sukurkite funkciją, kuri sudaugintų (NxN) matricas (two dimensional arrays) ir gražintų rezultatą.

# 🤷‍♂️ Čia nėra jokių konkrečių nurodymų 🤷‍♂️ Pagalvokite, ką darytumėte, jei jums būtų duota tokia užduotis darbe.



def multiply_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Error: matrices are not of the same size")
    result = [[0 for _ in range(len(mat1))] for _ in range(len(mat1[0]))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


mat1 = [[1, 2], [3, 4]]
mat2 = [[2, 0], [1, 2]]
result = multiply_matrices(mat1, mat2)
print(result)