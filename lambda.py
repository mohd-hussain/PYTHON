
x,y,z=int(input("Enter the value of x y z\n")),int(input()),int(input()),int(input())

a=(lambda x,y,z:2*x+3*y+z) (x,y,z)

print(a)

tup=(1,2,3,4,5)

def myfunc(x):
	return x*2
	
result=list(map(myfunc,tup))

print(result)



