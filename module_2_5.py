def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        sp = []
        matrix.append(sp)
        for j in range(m):
            sp.append(value)
            #sp.insert(j, value)
    return matrix

m1 = get_matrix(2, 2, 10)
m2 = get_matrix(3, 5, 42)
m3 = get_matrix(4, 2, 13)
m4 = get_matrix(1,11,7)
print(m1)
print(m2)
print(m3)
print(m4)