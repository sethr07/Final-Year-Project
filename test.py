import time
import sys, os

str1 = "My name is Gauri. Yo what u doin."
str2 = "I am good."
str3 = "I am so happy with life."

start=time.time()
st = str1+str2+str3
end=time.time()

print(st)
size = sys.getsizeof(st)
print("\nTime Taken using + : ", (end-start))
print("\nSize: ", size)

start=time.time()
st = (f'{str1} {str2} {str3}')
end=time.time()
size=sys.getsizeof(st)
print(st)
print("\nTime Taken using f: ", (end-start))
print("\nSize: ", size)


start=time.time()
st = ("".join((str1,str2,str3)))
end=time.time()
size=sys.getsizeof(st)
print(st)
print("\nTime Taken using join: ", (end-start))
print("\nSize: ", size)

