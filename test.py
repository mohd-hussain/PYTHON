def func(no):
    if(no%2==1):
        print("Weird")     
    else:
        if(2 <= no <= 5):
            print("Not Weird")
        if(6 <= no <= 20):
            print("Weird")
        else:
            print("Not Weird")
            
n=int(input()) 
func(n)
   
    

    


