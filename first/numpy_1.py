
import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",")
print(type(world_alcohol))
matrix = numpy.array([
                    [5, 10, 15],
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print (matrix == 25)

vector = numpy.array([5, 10, 15, 20])
equal_to_ten = (vector == 10)
print(equal_to_ten)
print(vector[equal_to_ten])

matrix = numpy.array([
                [5, 10, 15],
                [20, 25, 30],
                [35, 40, 45]
             ])

second_column_25 = (matrix[:,1] == 25)
print(matrix[[True, True, False],:])
print(second_column_25)
print(matrix[second_column_25, :])


print('=======================================1')

vector = numpy.array([5, 10, 15, 20])
equal_to_ten_and_five = (vector == 10) & (vector == 5)
print(equal_to_ten_and_five)


vector = numpy.array([5, 10, 15, 20])
equal_to_ten_or_five = (vector == 10) | (vector == 5)
print(equal_to_ten_or_five)

print('========================================2')
matrix = numpy.array([
            [5, 10, 15],
            [20, 25, 30],
            [35, 40, 45]
         ])
second_column_25 = matrix[:,1] == 25
print(second_column_25)
matrix[second_column_25, 1] = 10
print(matrix)
print('========================================3')
vector = numpy.array(["1", "2", "3"])
print(vector.dtype)
print(vector)
vector = vector.astype(float)
print(vector.dtype)
print(vector)
vector = numpy.array([5, 10, 15, 20])
print(vector.sum())
matrix = numpy.array([
                [5, 10, 15],
                [20, 25, 30],
                [35, 40, 45]
             ])
print(matrix.sum(axis=1))

matrix = numpy.array([
                [5, 10, 15],
                [20, 25, 30],
                [35, 40, 45]
             ])
print(matrix.sum(axis=0))

print('==============================4')
#replace nan value with 0
world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",")
#print world_alcohol
is_value_empty = numpy.isnan(world_alcohol[:,4])
#print is_value_empty
world_alcohol[is_value_empty, 4] = '0'
alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()
print(total_alcohol)
print(average_alcohol)

print('===============================5')

world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",", dtype="U75", skip_header=1)
print(world_alcohol)
uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]
print (uruguay_other_1986)
print (third_country)

print("===============================6")
vector = numpy.array([5, 10, 15, 20])
print(vector[0:3])
