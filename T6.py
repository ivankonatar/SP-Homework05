""" T6. Create class `ComplexNumber` which implements operator oveloading methods for complex numbers `(+,-,*,/)`."""

import math

class ComplexNumber():

    def __init__(self, re, im):
        self.realni=re
        self.imaginarni=im

    def moduo(self):
        return math.sqrt(self.realni**2 + self.imaginarni**2)

    def saberi(self, z):
        return ComplexNumber(self.realni +z.realni, self.imaginarni +z.imaginarni)
    def oduzmi(self, z):
        return ComplexNumber(self.realni -z.realni, self.imaginarni -z.imaginarni)
    def pomnozi(self,z):
        return ComplexNumber((self.realni*z.realni)-(self.imaginarni*z.imaginarni),
                             (self.imaginarni*z.realni)+(self.imaginarni*z.imaginarni))
    def podijeli(self,z):
        return ComplexNumber((self.realni*z.realni)/(z.realni*z.realni+z.imaginarni*z.imaginarni),
                             (self.imaginarni*z.realni-self.realni*z.imaginarni)/(z.realni*z.realni+z.imaginarni*z.imaginarni))



    def __str__(self):

        znak=" - " if self.imaginarni<0 else " + "
        return str(self.realni)+znak+ str(abs(self.imaginarni))+"i"

z1=ComplexNumber(10,2)
z2=ComplexNumber(2,5)

print("z1= ",z1)
print("z2= ",z2)
print(" ")
sabiranje=z1.saberi(z2)
oduzimanje=z1.oduzmi(z2)
mnozenje=z1.pomnozi(z2)
dijeljenje=z1.podijeli(z2)

print("z1+z2= ",sabiranje)
print("z1-z2= ",oduzimanje)
print("z1*z2= ",mnozenje)
print("z1/z2= ",dijeljenje)


