def long_length():          
 str=input("\nEnter a string : ")
 M_str=" "
 i=0
 while (i<len(str)):
  word=" "
  while (str[i]!=" "):
   word+=str[i]
   i=i+1
   if(i==len(str)):
    break
  if (i!=len(str)):
   while(str[i]==' '):
    i=i+1
  if(len(M_str) < len(word)):
    M_str = word
 print(" Longest word in the string is :", M_str)
 

def palindrone():            
 str=input("\nEnter a string : ")
 b=0
 e=len(str)-1
 while (b<e):
  if (str[b] != str[e]):
   break
  b+=1
  e-=1
 if(b<e):
  print("Given string is not a Palindrone ")
 else:
  print("Given string is a Palindrone") 
 
  
def character_frequency():          
 str=input("\nEnter a string : ")
 character=input("Enter a character whose frequency is to be checked : ")
 count=0
 for i in range(0,len(str)): 
  if(str[i]==character):
   count+=1
 print("Frequency of ",character," is : ",count)
 
 
def word_frequency():               
 str=input("\nEnter a string : ")
 str = str.split()
 M_str=[]
 i=0
 for i in str:
     if i not in M_str:
        M_str.append(i)
 for i in range (0,len(M_str)):
  print("\nFrequency of ",M_str[i]," is : ", str.count(M_str[i])) 
 
  
def substring_index():              
 str = input("\nEnter a string : ")
 substring = input("Enter a sub-string whose index is to be checked : ")
 index = str.find(substring)
 if (index >= 0):
  print("Index is : ", index)
 else: 
  print("Sub-string not found.")    
     
#<------------------------------------------------------------------------------------------------->

flag=1
while flag==1:
  print("\n--------------------MENU--------------------- ")
  print("1.To display the word with the longest length : ")
  print("2.To determine the frequency of occurence of particular character in the string : ")
  print("3.To check if the given string is palindrone or not : ")
  print("4.To display index of first appearance of the sub-string : ")
  print("5.To count the occurence of each word in a given string : ")
  print("6 EXIT \n")
  ch=int(input("Enter your choice (from 1 to 6) : "))
  
  if ch==1:
   print("1. To display the word with the longest length :")
   long_length()
   a=input("\n\nDo you want to continue (yes/no) : ")
   if a=="yes":
     flag=1
   else:
     flag=0
     print("Thank you for using this program!")
     
  elif ch==2:
   print("2. To determine the frequency of occurence of particular character in the string :")
   character_frequency()
   a=input("\n\nDo you want to continue (yes/no) : ")
   if a=="yes":
     flag=1
   else:
     flag=0
     print("Thank you for using this program!")
     
  elif ch==3:
   print("3. To check if the given string is palindrone or not : ")
   palindrone()
   a=input("\n\nDo you want to continue (yes/no) : ")
   if a=="yes":
     flag=1
   else:
     flag=0
     print("Thank you for using this program!")
     
  elif ch==4:
   print("4. To display index of first appearance of the sub-string : ")
   substring_index()
   a=input("\n\nDo you want to continue (yes/no) : ")
   if a=="yes":
      flag=1
   else:
      flag=0
      print("Thank you for using this program!")   
  
  elif ch==5:
   print("5. To count the occurence of each word in a given string : ")
   word_frequency()
   a=input("\n\nDo you want to continue (yes/no) : ")
   if a=="yes":
     flag=1
   else:
     flag=0
     print("Thank you for using this program!")
     
  elif ch==6:
   flag=0
   print("Thank you for using this program!")
   
  else:
   print("WRONG CHOICE !!")
   a=input("\n\nDo you want to continue (yes/no) : ") 
   if a=="yes":
     flag=1
   else:
     flag=0
     print("Thank you for using this program!")  
