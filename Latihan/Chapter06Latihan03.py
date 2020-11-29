#faktorial(n)

def faktorial(n):
    faktorialN=1
    while(n>0):
        faktorialN=faktorialN * n
        n-=1
    return faktorialN

def kombinasi(a,b):
    c=a-b

    hasil=faktorial(a)/(faktorial(b)*faktorial(c))
    print(hasil)

#3a
#C=kombinasi
a=5
b=3
kombinasi(a,b)

def permutasi(a,b):
    c=a-b

    hasil=faktorial(a)/faktorial(c)
    print(hasil)

#3b
#P=permutasi
c=10
d=7
permutasi(c,d)
