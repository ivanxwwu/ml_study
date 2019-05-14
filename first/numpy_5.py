import numpy as np
data = np.sin(np.arange(20)).reshape(5,4)
print(data)
print(range(data.shape[1]))
ind = data.argmax(axis=0)
print(ind)
data_max = data[ind, range(data.shape[1])]
print(data.shape[1])
#print data_max
print(all(data_max== data.max(axis=0)))

print('==========================1')
a = np.arange(0, 40, 10)
b = np.tile(a, (3, 5))
print(b)

print('==========================2')
a = np.array([[4, 3, 5], [1, 2, 1]])
#print a
#b = np.sort(a, axis=1)
#print b
#b
#a.sort(axis=1)
#print a
a = np.array([4, 3, 1, 2])
j = np.argsort(a)
print(j)
print(a[j])