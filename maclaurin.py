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
        suku_sin = (-1**n)*ml.suku(x,n*2-1)
    return jumlah

if __name__=='__main__':
    print('========= Test ========')
    x = 0.5
    a = sin_ml(x)
    b = sin(x)
    print('1. Sinus\n')
    print('Sin(%f) ngitung sendiri: %f\n' % (x,a))
    print('Sin(%f) dari math module: %f\n' % (x,a))
    print('Selisih: %f\n' % (b-a))
