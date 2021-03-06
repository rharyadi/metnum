#!/usr/bin/python3

# Deret Maclaurin berbagai fungsi

class maclaurin(object):

    # eps = nilai toleransi suku
    def __init__(self):
        self.eps = 0.00000001
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
    n = 0
    while abs(suku_cos)>ml.eps:
        jumlah += suku_cos
        n += 1
        suku_cos = (-1**n)*ml.suku(x,2*n)
    return jumlah

def exp_ml(x):
    ml = maclaurin()
    jumlah = 0
    suku_exp = 1
    n = 0
    while abs(suku_exp)>ml.eps:
        jumlah += suku_exp
        n += 1
        suku_exp = ml.suku(x,n)
    return jumlah

if __name__=='__main__':

    from math import sin, cos, exp, log
    from sys import argv, exit
    
    x = 0.5
    if len(argv) >= 3:
        exit(1)
    if len(argv) >= 2:
        try:
            x = float(argv[1])
        except ValueError:
            exit(1)

    def ngetest(fungsi, fungsi_math, argumen):
        a = fungsi(argumen)
        b = fungsi_math(argumen)
        print('%s(%f) = %f' % (fungsi.__name__, argumen, a))
        print('%s(%f) = %f' % (fungsi_math.__name__, argumen, b))
        print('Selisih = %f\n' % abs(a-b))

    print('============= Testing ==============')
    print('1. Fungsi Sinus')
    ngetest(sin_ml, sin, x)
    print('2. Fungsi Cosinus')
    ngetest(cos_ml, cos, x)
    print('3. Fungsi Exp(x)')
    ngetest(exp_ml, exp, x)
