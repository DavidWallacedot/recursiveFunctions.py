#David Wallace
#5-22-2018
# This is a program that contains several recursive functions
import random,sys				
def sumOfNumbers(inputNum):
	num = int(inputNum)
	if(num != 0):
		num = num + sumOfNumbers(num-1);	
	return num

def isMember(array,value,size):
	if(size != 0):
		if(value==array[size]):
			return  True
		else:
			isMember(array, value, size -1)			
		
		if(size ==0):
			return False
			
	

def stringReverser(tempString, size):
	if (size != -1):
		print(tempString[size],end =" ")
		stringReverser(tempString,size-1)

def isPalindrome(testStr):
	if(len(testStr) == 1):
		return True
		
	if(testStr[0] == testStr[len(testStr)-1]):
			
			isPalindrome(testStr[0:len(testStr)-2])
			return True
			
	return False

def multiply(x, y):
		
		if(x!=1):
			y += multiply(x-1,y)	
		
		return y
	


while True:

	switch = [sumOfNumbers,isMember,stringReverser,isPalindrome,multiply]

	print ("\n\nWhat do you want to do?\n")
	print ("\t1.  Sum of Numbers\n")
	print ("\t2.  IsMember Array Function\n")
	print ("\t3.  String Reverser\n")
	print ("\t4.  Palindrome Detector\n")	
	print ("\t5.  Recursive Multiplication\n")
	print ("\t6.  End the Program\n")
	print ("CHOOSE 1-6:  ")
	choice = int(input())	
	while(choice < 1 or choice > 6):
		print('input valid choice 1-6')
		choice = int(input())
	
	if choice == 6:
		sys.exit()
	if choice == 1:
		print('Please enter a number')
		print("\n\nSUM OF NUMBERS\n")
		num =  int(input())
		print(switch[choice-1](num))
	elif choice ==2:
		array = []
		for i in range(9):
			array = array + [random.randint(1,100)]
		print('Is member array function')
		print('Please enter an integer')
		num = int(input())
		print('Here are the array values')
		for i in range(len(array)):
			print(array[i])
		if (isMember(array,num,len(array)-1)==True):
			print('The element was found in the array')
		else:
			print('the element was not found in the array')
	elif choice ==3:
		print('String Reverser')
		print('Enter a string and I will reverse it: ')
		userString = input()
		stringReverser(userString,len(userString)-1)
	elif choice == 4:
		print( "\n\nPALINDROME DETECTOR\n")
		print( "Enter a string and I will tell you if it is a palindrome:  ")
		userString = input()
		userString.upper()
		userString.replace(" ","")
		if (isPalindrome(userString)==1):
			print('You have entered a palindrome')
		else:
			print('The string you entered is not a palindrome')
	elif choice ==5:
		print('Recursive Multiplication')
		print('Enter the first integer')
		num1 = int(input())
		print('Enter the second integer')
		num2 = int(input())
		print('The product of the two numbers is:', end=" ")
		print(multiply(num1,num2))
		

