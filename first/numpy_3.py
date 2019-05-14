import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.size)
print(np.zeros ((3,4)))
print(np.ones( (2,3,4), dtype=np.int32 ))
print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2, 0.3 ))
print('===================================1')
print(np.arange(12).reshape(4,3))
print(np.random.random((2,3)))
print('===================================2')
from numpy import pi
print(np.linspace( 0, 2*pi, 100 ))
print(np.sin(np.linspace( 0, 2*pi, 100 )))
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
#print a
#print b
#b
c = a-b
#print c
b**2
#print b**2
print(a<35)
print('===================================3')
A = np.array( [[1,1],
               [0,1]] )
B = np.array( [[2,0],
               [3,4]] )
print(A)
print(B)
#print A*B
print(A.dot(B))
print(np.dot(A, B))