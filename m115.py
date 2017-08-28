import ctypes
so = ctypes.CDLL('./libm115_encode.so')
a = so.m115_edinit()
print a
