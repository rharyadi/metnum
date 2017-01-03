#!/usr/bin/python3

# Deret Maclaurin berbagai fungsi

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

def sin_maclaurin(x):
    ml = maclaurin()
    jumlah = 0
    suku_sin = x
    tanda = 1
    n = 1
    while abs(suku_sin)>ml.eps:
        jumlah += suku_sin
        n += 2
        tanda *= -1
        suku_sin = tanda*ml.suku(x,n)
    return jumlah
