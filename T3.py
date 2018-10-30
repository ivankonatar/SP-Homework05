""" Write a Python program that inputs a list of words, separated by white- space, and outputs how
    many times each word appears in the list."""

str = input("Enter your string: ")
splitStr = str.split()

pom_str = []
for c in splitStr:
    if c not in pom_str:
        pom_str.append(c)

for i in range(len(pom_str)):
    br=0
    for j in range(len(splitStr)):
        if (pom_str[i]==splitStr[j]):
            br+=1
    print("Word  -{0}- in string is appears {1} times".format(pom_str[i],br))

