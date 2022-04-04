def vfunc(a,*b):
    print(type(b))
    for i in range(len(b)):
        a+=b[i]
    return a

print(vfunc(1,2,3,4,5))