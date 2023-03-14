# some experimenting with tuples
# immutable
import timeit 

# a list can be cast to a tuple as per below
a_list = ['x','y','z','aa']
print (a_list)
b_tuple = tuple(a_list)
print(b_tuple)

# tuple like list but immutable
my_tuple = (1,2,3)  

# simple function to convert list to tuple
def convert(a_list):
    return tuple(a_list)
    
the_list = [1,2]

# cast list to tuple
print(convert(the_list))

empty_tuple = tuple() # or just ()

# one element tuple
solo_tuple = ('x',)




# below shows that tuples are faster than lists - programmatically

print(timeit.timeit('x=(1,2,3,4,5,6,7,8,9,10,11,12)', number=1000000))
print(timeit.timeit('x=[1,2,3,4,5,6,7,8,9,10,11,12]', number=1000000))

