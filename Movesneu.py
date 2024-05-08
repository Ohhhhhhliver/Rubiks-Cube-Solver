

def u(epos,eperm):
    epos = [epos[3],epos[0],epos[1],epos[2],epos[4],epos[5],epos[6],epos[7]]
    return [epos,eperm]    
    
def u2(epos,eperm):
    epos = [epos[2],epos[3],epos[0],epos[1],epos[4],epos[5],epos[6],epos[7]]
    return [epos,eperm]

def uPrime(epos,eperm):
    epos = [epos[1],epos[2],epos[3],epos[0],epos[4],epos[5],epos[6],epos[7]]
    return [epos,eperm]

def d(epos,eperm):
    epos = [epos[0],epos[1],epos[2],epos[3],epos[5],epos[6],epos[7],epos[4]]
    return [epos,eperm]

def d2(epos,eperm):
    epos = [epos[0],epos[1],epos[2],epos[3],epos[6],epos[7],epos[4],epos[5]]
    return [epos,eperm]

def dPrime(epos,eperm):
    epos = [epos[0],epos[1],epos[2],epos[3],epos[7],epos[4],epos[5],epos[6]]
    return [epos,eperm]

def l(epos,eperm):
    epos = [epos[5],epos[1],epos[2],epos[0],epos[3],epos[4],epos[6],epos[7]]
    eperm = eperm[:]
    for i in range(4):
        a = [0,3,4,5]
        if a[i] != 7:
            if i == 0 or i == 2: 
                b = eperm[a[i]]
                b = b + 1
                if b == 3:
                    b = 0
                eperm.pop(a[i])
                eperm.insert(a[i], b)


            if i == 1 or i == 3:
                b = eperm[a[i]]
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a[i])
                eperm.insert(a[i], b)

    return [epos , eperm[:]]

def l2(epos,eperm):
    epos = [epos[4],epos[1],epos[2],epos[5],epos[0],epos[3],epos[6],epos[7]]
    
    return [epos , eperm]

def lPrime(epos,eperm):
    epos = [epos[3],epos[1],epos[2],epos[4],epos[5],epos[0],epos[6],epos[7]]
    eperm = eperm[:]
    for i in range(4):
        a = [0,3,4,5]
        if a[i] != 7:
            if i == 0 or i == 2: 
                b = eperm[a[i]]
                b = b + 1
                if b == 3:
                    b = 0
                eperm.pop(a[i])
                eperm.insert(a[i], b)


            if i == 1 or i == 3:
                b = eperm[a[i]]
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a[i])
                eperm.insert(a[i], b)

    return [epos , eperm[:]]

def f(epos,eperm):
    epos = [epos[0],epos[1],epos[3],epos[4],epos[7],epos[5],epos[6],epos[2]]
    eperm = eperm[:]
    for i in range(4):
        a = [2,3,4,7]         
        if a[i] != 7:    
            if i == 1 or i == 3: 
                b = eperm[a[i]]               
                b = b + 1               
                if b == 3:
                    b = 0
                eperm.pop(a[i])
                eperm.insert(a[i], b)
            
            
            if i == 0 or i == 2:
                b = eperm[a[i]]               
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a[i])
                eperm.insert(a[i], b)
        else: 
            continue

    return [epos , eperm[:]]

def f2(epos,eperm):
    epos = [epos[0],epos[1],epos[4],epos[7],epos[2],epos[5],epos[6],epos[3]]

    return [epos , eperm]

def fPrime(epos,eperm):
    epos = [epos[0],epos[1],epos[7],epos[2],epos[3],epos[5],epos[6],epos[4]]
    eperm = eperm[:]
    for i in range(4):
        a = [2,3,4,7]         
        if a[i] != 7:    
            if i == 1 or i == 3: 
                b = eperm[a[i]]               
                b = b + 1               
                if b == 3:
                    b = 0
                eperm.pop(a[i])
                eperm.insert(a[i], b)
            
            
            if i == 0 or i == 2:
                b = eperm[a[i]]               
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a[i])
                eperm.insert(a[i], b)
        else: 
            continue
    
    return [epos , eperm[:]]

def r(epos,eperm):
    epos = [epos[0],epos[2],epos[7],epos[3],epos[4],epos[5],epos[1],epos[6]]
    eperm = eperm[:]
    for i in range(4):
        a = [1,2,6,7]
        if a[i] != 7:
            if i == 1 or i == 2: 
                b = eperm[a[i]]
                b = b + 1
                if b == 3:
                    b = 0
                eperm.pop(a[i])
                eperm.insert(a[i], b)


            if i == 0 or i == 3:
                b = eperm[a[i]]
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a[i])
                eperm.insert(a[i], b)


    return [epos , eperm[:]]

def r2(epos,eperm):
    epos = [epos[0],epos[7],epos[6],epos[3],epos[4],epos[5],epos[2],epos[1]]
    
    return [epos , eperm]

def rPrime(epos,eperm):
    epos = [epos[0],epos[6],epos[1],epos[3],epos[4],epos[5],epos[7],epos[2]]
    eperm = eperm[:]
    for i in range(4):
        a = [1,2,6,7]
        if a[i] != 7:
            if i == 1 or i == 2: 
                b = eperm[a[i]]
                b = b + 1
                if b == 3:
                    b = 0
                eperm.pop(a[i])
                eperm.insert(a[i], b)


            if i == 0 or i == 3:
                b = eperm[a[i]]
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a[i])
                eperm.insert(a[i], b)
    
    return [epos , eperm[:]]

def b(epos,eperm):
    epos = [epos[1],epos[6],epos[2],epos[3],epos[4],epos[0],epos[5],epos[7]]
    eperm = eperm[:]
    for i in range(4):
        a = [0,1,5,6]
        if a[i] != 7:
            if i == 1 or i == 2: 
                b = eperm[a[i]]
                b = b + 1
                if b == 3:
                    b = 0
                eperm.pop(a[i])
                eperm.insert(a[i], b)


            if i == 0 or i == 3:
                b = eperm[a[i]]
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a[i])
                eperm.insert(a[i], b)

    return [epos , eperm[:]]

def b2(epos,eperm):
    epos = [epos[6],epos[5],epos[2],epos[3],epos[4],epos[1],epos[0],epos[7]]
    return [epos , eperm]

def bPrime(epos,eperm):
    epos = [epos[5],epos[0],epos[2],epos[3],epos[4],epos[6],epos[1],epos[7]]
    eperm = eperm[:]
    for i in range(4):
        a = [0,1,5,6]
        if a != 7:
            if i == 1 or i == 2: 
                b = eperm[a[i]]
                b = b + 1
                if b == 3:
                    b = 0
                eperm.pop(a[i])
                eperm.insert(a[i], b)


            if i == 0 or i == 3:
                b = eperm[a[i]]
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a[i])
                eperm.insert(a[i], b)
    
    return [epos , eperm[:]]


