def fib():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a+b
        
def even(seq):
    for i in seq:
        if i%2==0:
            yield i

def under_a_million(seq):
    for i in seq:
        if i>4000000:
            break
        else:
            yield i

print(sum(under_a_million(even(fib()))))
