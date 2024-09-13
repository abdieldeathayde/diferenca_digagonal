import math
import os
import random
import re
import sys

def diagonal_difference(arr):

    if __name__ == '__main__':   
        ftpr = open(os.environ['OUTPU_PATH'], 'w') 
        tamanho_matriz = int(input().strip())
        arr = []

        for _ in range(tamanho_matriz):
            arr.append(list(map(int, input().rsplit().split())))
    resultado = diagonal_difference(arr)

    ftpr.write(str(resultado) + '\n')
    ftpr.close()
    
        