#	AUTHORS : PRAGYA PRAKASH(2016067), TANYA RAJ(2016108)

import re
import timeit

def getfields(metafile):
	file = open(metafile,"r")
	s =""
	for line in file:
		line = line.rstrip('\n')
		if(line.split(" = ")[0] =="Field Name"):
			s+=(line.split(" = ")[1]+", ")
	s+="\n"
	return s

def fileread(filename,metafile):
    file = open(metafile,"r")
    for line in file:
        line = line.rstrip('\n')
        if(line.split(" = ")[0] =="Field Name"):
            print(line.split(" = ")[1],end = '\t')
    print()
    file1 = open(filename,"r")
    for line in file1:
        print(line)
		

def filewrite(filename,readfile,metafile):
    file = open(filename,"r")
    file1 = open(readfile,"w")
    file2 = open(metafile,"r")
    s =""
    for line in file2:
        line = line.rstrip('\n')
        if(line.split(" = ")[0] =="Field Name"):
            s+=(line.split(" = ")[1]+"\t")
    s+="\n"
    file1.write(s)
    for line in file:
        file1.write(line)
        
def findsum(fieldname,filename,metafile):
        file = open(filename,"r")
        file1 = open(metafile,"r")
        sum =0
        counter =0
        found =0
        datatype =""
        for line in file1:
            line = line.rstrip('\n')
            if(line.split(" = ")[0] =="Field Name"):
                if(line.split(" = ")[1]==fieldname):
                    found =1    
                else:
                    counter+=1
            if(line.split(" = ")[0] =="Field DataType"):
                if(found==1):
                    datatype = line.split(" = ")[1]
                    break
        for line in file:
            l = line
            values = re.split(r'\t+', l.rstrip('\n'))
            if(datatype == "Integer"):
                sum+=int(values[counter])
            elif(datatype == "Float" ):
                sum+=float(values[counter])
            elif(datatype == "Double" ):
                sum+=double(values[counter])
            else:
                print("Invalid Fieldname:- Can't Add Strings")
                break
        print("The sum is :- "+str(sum))


if __name__=='__main__': 
	
	filewrite("MetaInput.txt","UserFile.txt","MetaData.txt")
	
	while(True):
			print("\n\n\nWelcome to the Database");
			print("\nMENU: ")
			print("Enter P for printing the data")
			print("Enter S for finding sum of the all values in a field")
			print("Press Q to exit")
			
			ch = input("\n\nPress a Key: ")
			
			if(ch=="P"):
				print("\nHere is the data of all files:")
				start = timeit.default_timer()
				fileread("MetaInput.txt","MetaData.txt")
				stop = timeit.default_timer()
				total_time = stop - start
				print("Time Taken is: ",total_time," seconds.")
				
			elif(ch=="S"):
				print("The possible field names are: ",getfields("Metadata.txt"))
				field = input("Enter Field Name: ")
				start = timeit.default_timer()
				findsum(field,"MetaInput.txt","MetaData.txt")
				stop = timeit.default_timer()
				total_time = stop - start
				print("Time Taken is: ",total_time," seconds.")
				
			elif(ch=='Q'):
				break
			else:
				print("\nPlease enter a valid option")
        
            
