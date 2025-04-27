def accept_array(A):
	n=int(input("\n Enter the total number of students"))
	for i in range (n):
		x=int(input("\n Enter the roll no of student %d:" %(i+1)))
		A.append(x)
	print("\n Student information accepted successfully")
	return n
	
	
def display_array(A,n):
	if (n==0):
		print("\n No records in the database")
	else:
		print("Students array:",end='')
		for i in range (n):
			print("%d " %A[i], end='')
		print("\n")
		
		
def linear_search(A,n,x):
	for i in range(n):
		if(A[i]==x):
			return i
	return -1
	
		
def sentinal_search(A,n,x):
	last=A[n-1]
	i=0
	A[n-1]=x
	while (A[i]!=x):
		i=i+1
	A[n-1]=last
	if((i<n-1) or (x==A[n-1])):
		return i
	else:
		return -1
	
		
def Main():
	A=[]
	while True:
		print("\t 1. Accept and display studen information")
		print("\t 2. Linear search")
		print("\t 3. Sentinal search")
		print("\t 4. Exit")
		ch= int(input("Enter your choice"))
		if (ch==4):
			print("End of the program")
			print("Thank you for using the program")
			quit()
		elif(ch==1):
			A=[]
			n=accept_array(A)
			display_array(A,n)
		elif(ch==2):
			x=int(input("Enter the roll no. to be searched"))
			flag = linear_search(A,n,x)
			if(flag == -1):
				print("\n Roll no. to be searched not found")
			else:
				print("\n Roll no. found at location %d" %(flag + 1))
		elif(ch==3):
			x=int(input("Enter the roll no. to be searched"))
			flag = sentinal_search(A,n,x)
			if(flag==-1):
				print("\n Roll no. to be searched not found")
			else:
				print("\n Roll no. found at location %d" %(flag + 1))
		else:
			print("\n WRONG CHOICE")
		
						
Main()
