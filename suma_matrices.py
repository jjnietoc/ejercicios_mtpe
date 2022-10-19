#usuario input y devuelve algo


filas = int(input("Cuantas filas? "))
colum = int(input("Cuantas columnas? "))

mat_a = []
for i in range(filas):
    mat_a.append([0]*colum)
    print(mat_a[i])

mat_b = []
for i in range(filas):
    mat_b.append([0]*colum)
    print(mat_b[i])

for i in range(filas):
    for j in range(colum):
        mat_a[i][j] = int(input('Numero para (%d,%d): '%(i,j)))
    
for i in range(filas):
    print(mat_a[i])

for i in range(filas):
    for j in range(colum):
        mat_b[i][j] = int(input('Numero para (%d,%d): '%(i,j)))

for i in range(filas):
    print(mat_b[i])


mat_sum = []
for i in range(filas):
    mat_sum.append([0]*colum)

for i in range(filas):
    for j in range(colum):
        mat_sum[i][j] = mat_a[i][j] + mat_b[i][j]

for i in range(filas):
    mat_f = []
    for j in range(colum):
        mat_f.append(mat_sum[i][j])
    print(mat_f)