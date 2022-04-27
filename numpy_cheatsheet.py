#! /usr/bin/python3

import numpy as np
import math



a = np.array([1.2,2.5,3.2,1.8])
print("numpy offers has its own array struct",type(a))
print("elements type",a.dtype,sep=" ")
print("array dimension",a.ndim,sep=" ")
print("number of lines and cols ",a.shape,sep=" ")
print("gives the number of elements in the row if dim=1 else number of cols",a.size,sep=" ")
print("\n \n \n")

print("we can set explicity the type of elements")
b= np.array([1,2,4],dtype=float)

print("\n \n \n")

print("Elements can be objects too !")
c= np.array([{"Toto":(45,20000)},{"Tata":[34,1500]}])
print(c)
print(c.dtype)


print("\n \n \n")

print("Numpy helps us create arrays quickly")
print("Generates suite arithmetic")
d= np.arange(start=0,stop=10)
print(d)

print("\n \n \n")

print("Generates suite by the whatever step we want")
e= np.arange(start=0,step=2,stop=10)
print(e)

print("\n \n \n")

print("Array with fill values")
print(np.ones(shape=5))
print(np.full(shape=5,fill_value=3.2))
print("Suite lineaire",np.linspace(start=0,stop=10,num=5),sep=" ")

print("\n \n \n")

print("loading elements from a file")
f =np.loadtxt("vectors.txt",dtype=float)
print("use `os.chdir` to change the working directory")

print("\n \n \n")

print("You can convert python arrays to numpy")
lst = [1,2,3,4,5]
print(type(lst))
print(lst)
g=np.asarray(lst,dtype=float)
print(type(g));
print(g)

print("\n \n \n")

print("manipulates arrays as you like")
h=np.array([1,2,3,4,5],dtype=int)
print(h,"let's add an element at the end ",sep="\n")
h=np.append(h,10)

print("\n \n \n")

print("let's delete a value now")
h= np.delete(h,3)
print(h)

print("\n \n \n")

print("let's change the size of our array")
#h=np.resize(h,new_shape=10)
print(h)

print("\n \n \n")

print("concatinating arrays too")
x=np.array([1,2])
z=np.array([3,4])
y=np.array([5,6])
print(x,z,y,sep="\n")
print(np.concatenate((x,z,y)))


print("\n \n \n")

print("Extracting values")
i=np.array([1,2,3,4,5,6,],dtype=int)
print(i,end="\n\n")
print("all array",i[:],end="\n\n")
print("first element",i[0],end="\n\n")
print("last element",i[i.size-1],end="\n\n")
print("from the first till third element exclusive",i[1:3],end="\n\n")
print("start to 3 element exclusive",i[:3],end="\n\n")
print("start from 2 element",i[2:],end="\n\n")
print("last element revisited",i[-1],end="\n\n")
print("the three last element",i[-3:],end="\n\n")
print("All results arrays are of type np.array, the format is start:end:step ==> step can be negative")
print("Printing elements that verifies condition",i<3,i[i<3],sep="\n\n")
print("we can use `extract()`",np.extract(i<3,i),sep="\n",end="\n\n")
print("\n \n \n")



print("Sorting and Searching")
print("The max element in the array",np.max(i))
print("The min element in the array",np.min(i))
print("The index of the biggest element in the array",np.argmax(i))
j =np.array([4,22,56,12,1,2,3,3])
print(j)
print("Sorting the array",np.sort(j))
print("Getting indexes of sorted array",np.argsort(j))
print("Getting all distinct elements in the array",np.unique(j))
print("\n \n \n")

print("Statistics",)
print(j)
print("moyenne ",np.mean(j))
print("mediane ",np.median(j))
print("variance ",np.var(j))
print("quantile 50% ",np.percentile(j,50))
print("sum of elements ",np.sum(j))
print("Cumulative sum ",np.cumsum(j))
print("\n \n \n")

print("Operations with arrays")
k=np.array([1.2,3,1])
l=np.array([2,6,4])
print("Scalar product (If not the same size it throws an error ",np.vdot(k,l))
print("The equivalent of ",np.sum(k*l))
print("The norme value of \n",k,"\n is ",np.linalg.norm(k))
print("The equivalent of ",math.sqrt(np.sum(k**2)))
print("\n \n \n")

print("Play with groups ( ensembles ) ")
m= np.array([1,2,1.2])
print(k)
print(m)
print("The intersection array ",np.intersect1d(m,k))
print("The union array ",np.union1d(m,k))
print("The difference array ",np.setdiff1d(m,k))
print("\n \n \n")
