import time
import math
def calculate_time(func):
    def inner (*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f'Execution Time : {end-start}')
        
@calculate_time
def myloop(n):
    for x in range(n):
        
myloop(1000)

@calculate_time

def myloop2(s):
    math.factorial(s)

myloop(2000)
