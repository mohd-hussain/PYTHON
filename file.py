
fp=open("hussain.txt","w")
c=''
while(c!='.'):
	c=input()
	fp.write(c)
	fp.close()

fp=open("hussain.txt","r")

printf(fp.read())
