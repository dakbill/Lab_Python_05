def do(thing):
    return str(thing) + str(1)
do(5)
#do(5) will have a string value of 51
##########################################################
def do(one, two=5):
    return one+two
do(5)
#do(5) will have an integer value of 10

def do(a,b):
    a=5
    b=5
    return a*b
inp = 8
do(inp,5)
print inp
#do(inp,5) will evaluate to 25 but inp will print 8
##########################################################
def try_to_change_list_contents(the_list):
    the_list.append('four')
outer_list = ['one', 'two', 'three']
try_to_change_list_contents(outer_list)
print outer_list
#4 will be appended to the list
###########################################################
def do(a, f):
    return a*f(a)
def inp(a):
    return a*2
print do(6,inp)
#The output is 72
###########################################################
def factorial(num):
    out=1
    for i in range(num,0,-1):
        out*=i
    return out
num=input("Enter num to calculate its factorial:")
print str(num)+" factorial is "+str(factorial(num)) 
#factorial
###########################################################
def fibonacci(num):
    out=[]
    p1=0
    p2=1
    for i in range(1,num+1):
        if (i < 2):
            numout=i;
        else:
            numout=p2 + p1
            p1=p2
            p2=numout
        out.append(numout)
    return out
print fibonacci(10)
#fibonacci
##############################################################
