""" T1. Write a Python program that outputs all possible strings formed by using thecharacters
    c , a , t , d , o ,and g exactlyonce."""


string=["c","a","t","d","o","g"]
new_str=""
brojac_kombinacija=0

for i in range(len(string)):
    for j in range(len(string)):
        for m in range(len(string)):
            for n in range(len(string)):
                for p in range(len(string)):
                    for q in range(len(string)):
                        if (i!=j and i!=m and i!=n and i!=p and i!=q and j!=m and j!=n and j!=p and j!=q and m!=n and m!=p and m!=q and n!=p and n!=q and p!=q):
                            new_str+=string[i]+string[j]+string[m]+string[n]+string[p]+string[q]+"\n"
                            brojac_kombinacija+=1
print(new_str)
print("We have {0} different strings composed of characters: {1}".format(brojac_kombinacija,string))

