class Student:
	def __init__(self,first,last,rollno,gmail):
		self.first=first
		self.last=last
		self.rollno=rollno
		self.gmail=gmail
   ''' def fullname(self):
        return '{} {}' format(self.first,self.last)  '''      

			
		
std1=Student('mohammed','hussain','16co37','mohammedhussain8273@gmail.com')
std2=Student('mohammed','atay','16c036','mohammedatay1123@gmail.com')



print(std1.first)
print(std1.last)
print(std1.gmail)
print(std1.rollno)

print('*'*160)

print(std2.last)
print(std2.gmail)
print(std2.rollno)

print('*'*160)

print(std_1.fullname())
print(std_1.fullname())

print('*'*160)

