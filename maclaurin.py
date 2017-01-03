#!/usr/bin/python3

# Deret Maclaurin berbagai fungsi

from math import sin,cos,log

class maclaurin(object):

    def __init__(self, eps=0.0000000001):
        self.eps = eps
    def faktorial(self,n):
        if n==0:
            return 1
        else:
            return n*self.faktorial(n-1)

    def suku(self,x,n):
        return x**n/self.faktorial(n)

def sin_ml(x):
    ml = maclaurin()
    jumlah = 0
    suku_sin = x
    n = 1
    while abs(suku_sin)>ml.eps:
        jumlah += suku_sin
        n += 1
        suku_sin = (-1**n)*ml.suku(x,2*n-1)
    return jumlah

def cos_ml(x):
    ml = maclaurin()
    jumlah = 0
    suku_cos = 1
    n = 1
    while abs(suku_cos)>ml.eps:
        jumlah += suku_cos
        n += 1
        suku_cos = (-1**(n+1))*ml.suku(x,2*n)
    return jumlah

if __name__=='__main__':
    print('========= Test ========')
    x = 0.5
    print('1. Sinus\n')
    a = sin_ml(x)
    b = sin(x)
    print('Sin(%f) ngitung sendiri: %f\n' % (x,a))
    print('Sin(%f) dari math module: %f\n' % (x,a))
    print('Selisih: %f\n' % abs(a-b))
    print('2. Cosinus\n')
    a = cos_ml(x)
    b = cos(x)
    print('Cos(%f) ngitung sendiri: %f\n' % (x,a))
    print('Cos(%f) dari math module: %f\n' % (x,a))
    print('Selisih: %f\n' % abs(a-b))
