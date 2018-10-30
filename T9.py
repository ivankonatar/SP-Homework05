""" T9. Write a Python program for a matrix class that can add and multiply two- dimensional arrays of numbers,
    assuming the dimensions agree appropri- ately for the operation."""

n1 = int(input("Enter the number of rows in a matrix A: "))
m1 = int(input("Enter the number of colums in a matrix A: "))
n2 = int(input("Enter the number of rows in a matrix B: "))
m2 = int(input("Enter the number of colums in a matrix B: "))

if (n1==n2 and m1==m2) or n1==m2 or n2==m1:
    x=[]
    y=[]
    z=[]
    rezultat=[]
    for g in range(n1):
        rezultat.append([])
        for h in range (m2):
            rezultat[g].append(0)
    for i in range(n1):
        x.append([])
        for j in range(m1):
            broj = int(input("Matrix A - Enter element {0}.row {1}.colum  : ".format(i+1,j+1)))
            x[i].append(broj)

    for p in range(n2):
        y.append([])
        for q in range(m2):
            broj = int(input("Matrix B - Enter element {0}.row {1}.colum  : ".format(p+1,q+1)))
            y[p].append(broj)
    print("Matrix A: ")
    for vektor in x:
       print(vektor)
    print("Matrix B: ")
    for vektor in y:
        print(vektor)

    if n1 == n2 and m1 == m2:
        for k in range(n2):
            z.append([])
            for l in range(m2):
                broj = int(x[k][l]) + int(y[k][l])
                z[k].append(broj)
        print("Matrix A+B: ")
        for vektor in z:
            print(vektor)
    else:
        print("matrices can't be added, because the number of columns and rows of matrices A and B isn't the same")

    for a in range(len(x)):
        for b in range(len(y[0])):
            for c in range(len(y)):
                rezultat[a][b]+= x[a][c] * y[c][b]
    print("Matrix A*B: ")
    for vektor in rezultat:
        print(vektor)
else:
    print("matrices can't be added or multiply, because the number of columns and rows "
          "of matrices A and B is irregular for these functions")
