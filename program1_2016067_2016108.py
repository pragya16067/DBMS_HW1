import re
import timeit

#	AUTHORS : PRAGYA PRAKASH(2016067), TANYA RAJ(2016108)

class Student(object):
    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name   = name
        self.marks  = marks
        
    def filewrite(self,filename):
        file = open(filename,"w")
        file.write(self.rollno+"\t"+str(self.name)+"\t"+str(self.marks))
        
    def findsum(self,fieldname,filename):
        file = open(filename,"r")
        sum =0;
        counter =0;
        if(fieldname == "Roll Number"):
            counter =0;
        elif(fieldname == "Marks"):
            counter =2;
        else:
            print("Invalid Fieldname ")
            return
        for line in file:
            l = line
            values = re.split(r'\t+', l.rstrip('\n'))
            sum+=int(values[counter])
        print("The sum is :- "+str(sum))
        
    def fileread(self,filename):
        file = open(filename,"r")
        print("Roll No\tName\tMarks")
        for line in file:
            print(line)


if __name__=='__main__':
	s = Student(0,"",0)
	while(True):
		print("\n\n\nWelcome to the Student Database");
		print("\nMENU: ")
		print("Enter P for printing the Student data")
		print("Enter S for finding sum of the all values in a field")
		print("Press Q to exit")
		
		ch = input("\n\nPress a Key: ")
		
		if(ch=="P"):
			print("\nHere is the data of all files:")
			start = timeit.default_timer()
			s.fileread("Input.txt")
			stop = timeit.default_timer()
			total_time = stop - start
			print("Time Taken is: ",total_time," seconds.")
			
		elif(ch=="S"):
			print("The possible field names are: Roll Number, Name, Marks")
			field = input("Enter Field Name: ")
			start = timeit.default_timer()
			s.findsum(field,"Input.txt")
			stop = timeit.default_timer()
			total_time = stop - start
			print("Time Taken is: ",total_time," seconds.")
			#print(total_time)
			
		elif(ch=='Q'):
			break
			
		else:
			print("\nPlease enter a valid option")
            
    
