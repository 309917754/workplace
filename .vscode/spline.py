import numpy as np
from scipy.linalg import solve
dx1=[]
dx2=[]
dx3=[]
y=[]

def m(a,b):
    for n in range(len(a)-2):
        x1=(a[n+1]-a[n])/6
        x2=(a[n+2]-a[n])/3
        x3=(a[n+2]-a[n+1])/6
        y1=((b[n+2]-b[n+1])/(a[n+2]-a[n+1]))-((b[n+1]-b[n])/(a[n+1]-a[n]))
        dx1.append(x1)
        dx2.append(x2)
        dx3.append(x3)
        y.append(y1)

    return (dx1,dx2,dx3,y)

c=[4.00,4.35,4.57,4.76,5.26,5.88]
d=[4.19,4.77,6.57,6.23,4.90,4.77]
m(c,d)
y.append(0)
y.append(0)
x11=[dx1[0],dx2[0],dx3[0],0,0,0]
x21=[0,dx1[1],dx2[1],dx3[1],0,0]
x31=[0,0,dx1[2],dx2[2],dx3[2],0]
x41=[0,0,0,dx1[3],dx2[3],dx3[3]]
x51=[1,0,0,0,0,0]
x61=[0,0,0,0,0,1]
a1=np.array([x11,x21,x31,x41,x51,x61])
b1=np.array(y)
u=solve(a1,b1)
print(u)
print(a1)
print(dx1)
print(dx2)
print(dx3)