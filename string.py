st=input("Enter the string\n")

d={'alpha':0,'digit':0,'upper':0,'lower':0}

for i in st:
	if(i.isdigit()):
		d['digit']+=1
	
	elif(i.isalpha()):
		d['alpha']+=1

    elif(i.isupper()):
        d['upper']+=1

    else:
        d['lower']+=1
		
print(d)	
	
	
