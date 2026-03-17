a, b, c = input().split()

A= float(a)
B= float(b)
C= float(c)

pi = 3.14159

tri = (A*C)/2
cir = pi * (C*C)
tra = ((A+B)*C)/2
qua = (B*B)
ret = A*B


print(f'TRIANGULO: {tri:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {tra:.3f}')
print(f'QUADRADO: {qua:.3f}')
print(f'RETANGULO: {ret:.3f}')