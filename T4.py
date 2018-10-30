""" T4. Write a Python program that inputs a document and then outputs a bar- chart plot of the frequencies
of each alphabet character that appears in that document. """
import matplotlib.pyplot as plt

str = input("Enter your document: ")


pom_str = ""
x=[]
y=[]
for c in str:
    if c not in pom_str and (ord(c) >= ord("A") and ord(c) <= ord("Z") or ord(c) >= ord("a") and ord(c) <= ord("z")):
        pom_str+=c
        x.append(c)

for i in range(len(pom_str)):
    br=0

    for j in range(len(str)):
        if (pom_str[i]==str[j]):
            br+=1
    y.append(br)

plt.bar(range(len(x)), list(y), align='center')
plt.xticks(range(len(x)), list(x))

plt.show()