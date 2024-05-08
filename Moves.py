epos = [0,1,2,3,4,5,6,7]
eperm = [0,0,0,0,0,0,0]
 
def u(epos,eperm):
    ul = [epos[0],epos[1],epos[2],epos[3]]
    
    ul = [epos[0], epos[1], epos[2], epos[3]]
    k = ul.pop(3)
    ul.insert(0,k)

    for i in range(4): 
        epos.pop(i)
        epos.insert(i,ul[i])

    return [epos , eperm]

def u2(epos,eperm):

    for i in range(2):
        u(epos,eperm)

    return [epos , eperm]

def uPrime(epos,eperm):
    
    for i in range(3):
        u(epos,eperm)

    return [epos , eperm]

def d(epos,eperm):
    dl = [epos[4], epos[5], epos[6], epos[7]]
    k = dl.pop(0)
    dl.insert(3,k)

    for i in range(4): 
        epos.pop(i+4)
        epos.insert(i+4,dl[i])

    return [epos , eperm]

def d2(epos,eperm):

    for i in range(2):
        d(epos,eperm)

    return [epos , eperm]

def dPrime(epos,eperm):
    
    for i in range(3):
        d(epos,eperm)

    return [epos , eperm]

def l(epos,eperm):
    ll = [epos[0], epos[3], epos[4], epos[5]]
    
    for i in range(4):
        a = ll[i]
        if a != 7:
            if i == 0 or i == 2: 
                b = eperm[a]
                b = b + 1
                if b == 3:
                    b = 0
                eperm.pop(a)
                eperm.insert(a, b)


            if i == 1 or i == 3:
                b = eperm[a]
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a)
                eperm.insert(a, b)

    k = ll.pop(3)
    ll.insert(0,k)

    for i in range(4): 
        list = [0,3,4,5]
        epos.pop(list[i])
        epos.insert(list[i],ll[i])
    
    return [epos , eperm]

def l2(epos,eperm):
    for i in range(2):
        l(epos,eperm)
    return [epos , eperm]

def lPrime(epos,eperm):
    for i in range(3):
        l(epos,eperm)

    return [epos , eperm]

def f(epos,eperm):
    fl = [epos[2], epos[3], epos[4], epos[7]]
    
    for i in range(4):
        a = fl[i]         
        if a != 7:    
            if i == 1 or i == 3: 
                b = eperm[a]               
                b = b + 1               
                if b == 3:
                    b = 0
                eperm.pop(a)
                eperm.insert(a, b)
            
            
            if i == 0 or i == 2:
                b = eperm[a]               
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a)
                eperm.insert(a, b)
        else: 
            continue

    k = fl.pop(0)
    fl.insert(3,k)

    for i in range(4): 
        list = [2,3,4,7]
        epos.pop(list[i])
        epos.insert(list[i],fl[i])

    return [epos , eperm]

def f2(epos,eperm):
    for i in range(2):
        f(epos,eperm)

    return [epos , eperm]

def fPrime(epos,eperm):
    for i in range(3):
        f(epos,eperm)

    return [epos , eperm]

def r(epos,eperm):
    rl = [epos[1], epos[2], epos[6], epos[7]]
    
    for i in range(4):
        a = rl[i]
        if a != 7:
            if i == 1 or i == 2: 
                b = eperm[a]
                b = b + 1
                if b == 3:
                    b = 0
                eperm.pop(a)
                eperm.insert(a, b)


            if i == 0 or i == 3:
                b = eperm[a]
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a)
                eperm.insert(a, b)

    k0 = rl[0]
    k1 = rl[1]
    k2 = rl[2]
    k3 = rl[3]
    rl = [k1,k3,k0,k2]

    for i in range(4): 
        list = [1,2,6,7]
        epos.pop(list[i])
        epos.insert(list[i],rl[i])

    return [epos , eperm]

def r2(epos,eperm):
    for i in range(2):
        r(epos,eperm)
    return [epos , eperm]

def rPrime(epos,eperm):
    for i in range(3):
        r(epos,eperm)
    return [epos , eperm]

def b(epos,eperm):
    bl = [epos[0], epos[1], epos[5], epos[6]]
    
    for i in range(4):
        a = bl[i]
        if a != 7:
            if i == 1 or i == 2: 
                b = eperm[a]
                b = b + 1
                if b == 3:
                    b = 0
                eperm.pop(a)
                eperm.insert(a, b)


            if i == 0 or i == 3:
                b = eperm[a]
                b = b - 1
                if b == -1:
                    b = 2
                eperm.pop(a)
                eperm.insert(a, b)

    k0 = bl[0]
    k1 = bl[1]
    k2 = bl[2]
    k3 = bl[3]
    bl = [k1,k3,k0,k2]

    for i in range(4): 
        list = [0,1,5,6]
        epos.pop(list[i])
        epos.insert(list[i],bl[i])

    return [epos , eperm]

def b2(epos,eperm):
    for i in range(2):
        b(epos,eperm)
    return [epos , eperm]

def bPrime(epos,eperm):
    for i in range(3):
        b(epos,eperm)
    return [epos , eperm]


