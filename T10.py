""" T10. Write a program that can perform the Caesar cipher for English messages that include
    both upper- and lowercase characters."""

def CaesarCipher():
    s=input("Enter a string: ")
    step=int(input("Enter how many moves in Alphabet do you want: "))
    nova_recenica=''

    for i in range(len(s)):

        if (step>0) and (ord(s[i])>=ord("a")) and (ord(s[i])<=(ord("z")-step)):
            nova_recenica+=chr(ord(s[i])+step)

        elif step>0 and ord(s[i])>=ord("A") and ord(s[i])<=(ord("Z")-step):
            nova_recenica+=chr(ord(s[i])+step)

        elif step>0 and ord(s[i])>(ord("z")-step) and ord(s[i])<=(ord("z")):
            nova_recenica+=chr(ord(s[i])-ord("z")+ord("a")+step-1)

        elif step>0 and ord(s[i])>(ord("Z")-step) and ord(s[i])<=(ord("Z")):
            nova_recenica += chr(ord(s[i]) - ord("z") + ord("a") + step - 1)

        elif step<0 and ord(s[i])>=(ord("a")-step) and ord(s[i])<=ord("z"):
            nova_recenica+=chr(ord(s[i])+step)

        elif step<0 and ord(s[i])>=(ord("A")-step) and ord(s[i])<=ord("Z"):
            nova_recenica+=chr(ord(s[i])+step)

        elif step<0 and ord(s[i])<=(ord("a")-step) and ord(s[i])>=(ord("a")):
            nova_recenica+=chr(ord(s[i])+ord("z")-ord("a")+step+1)

        elif step<0 and ord(s[i]) <= (ord("A") - step) and ord(s[i]) >= (ord("Z")):
            nova_recenica += chr(ord(s[i]) + ord("z") - ord("a") + step + 1)

        else:
            nova_recenica +=s[i]

    return (nova_recenica)
print("Caesar cipher of your string is: ",CaesarCipher())