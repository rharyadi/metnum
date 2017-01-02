#!/usr/bin/python3

# Nyari epsilon mesin AMD E-450

def epsilon_mesin():
    # Inisialisasi
    eps = 1
    # eps itu bilangan terkecil yg masih dikenalin
    # di bawah eps, bilangan itu dianggep nol
    while eps+1>1:
        eps /= 2
    eps *= 2
    return eps


if __name__ == '__main__':
    eps = epsilon_mesin()
    print('Epsilon: %g' % eps)


