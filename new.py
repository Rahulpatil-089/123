def long_length():
 str=input("Please enter a string : ")
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
 print("Word with the longest length in the string is :", M_str)
 return M_str
 

def frequency():
 str=input("\n Please enter a string : ")
 ch=input("Enter the character whose frequency of occurrence you want to calculate : ")
 count=0
 for i in range(0,len(str)):
  if (str[i]==ch):
   count=count+1
 print("Frequency of occurrence of the character is : ",count)
 
 
def palindrome():
 str=input("\n Please enter a string : ")
 b=0
 e=len(str)-1
 while (b<e):
  if (str[b]!=str[e]):
   break
  b=b+1
  e=e-1
 if (b<e):
  print("The given string is not a Palindrome")
 else:
  print("The given string is a Palindrome")


""" 
long_length()
frequency()
palindrome()
"""


flag=1
while flag==1:
 print("\n ******MENU******\n")
 print("1. Word with the longest length in the string:")
 print("2. Frequency of occurrence of the character in the string:")
 print("3. The string is palindrome or not:")
 print("4. Exit:")
 ch=int(input("Enter the choice from 1 to 4:"))
 
if ch==1:
 M_str1=long_length()
 print(M_str1)
 break

elif ch==2:
 print(frequency())
 break
  
elif ch==3:
 print(palindrome())
 break
 
elif ch==4:
 flag=0
 print("Thank u for using the program")
 break
 
else:
 print("Wrong Choice!!")
 a=input("/n Continue(yes/no)")
 if a=="yes":
  flag=1
 else:
  flag=0
  print("Thank u for using the program!!!")
