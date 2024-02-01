# Integer

# Global variable
d = 9

def add(a, b):        
    c = 1;    
    return a + b + c + d;

def does_nothing():
    d = 1000

def modifies_global_var():
    global d # declare access to global variable
    d = 2000


if __name__ == '__main__':
    x = 0
    d = 9
    
    does_nothing()
    print(add(1,2)) # (1+2+1+9) = 13
    modifies_global_var()
    print(add(1,2)) # (1+2+1+2000) = 2004

