a,b,result = 0,1,0
def fib(a,b):
    global result
    c = a+b
    if c > 4000000:
        print(result)
        return
    if c%2==0:
        result = result +  c
    a,b = b,c
    fib(a,b)
fib(a,b)

