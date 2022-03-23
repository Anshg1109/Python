# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")





# def palindrome(a):
# 	mid = (len(a)-1)//2	 
# 	start = 0			 
# 	last = len(a)-1
# 	flag = 0
# 	while(start <= mid):

# 		if (a[start]== a[last]):			
# 			start += 1
# 			last -= 1
# 		else:
# 			flag = 1
# 			break;
			
# 	if flag == 0:
# 		print("The entered string is palindrome")
# 	else:
# 		print("The entered string is not palindrome")
		
# def symmetry(a):
# 	n = len(a)
# 	flag = 0
# 	if n%2:
# 		mid = n//2 +1
# 	else:
# 		mid = n//2
# 	start1 = 0
# 	start2 = mid
	
# 	while(start1 < mid and start2 < n):
		
# 		if (a[start1]== a[start2]):
# 			start1 = start1 + 1
# 			start2 = start2 + 1
# 		else:
# 			flag = 1
# 			break

# 	if flag == 0:
# 		print("The entered string is symmetrical")
# 	else:
# 		print("The entered string is not symmetrical")

# string = input("Enter the string : ")
# palindrome(string)
# symmetry(string)


# def uncommon(a,b):
# 	list_a = a.split()
# 	list_b = b.split()
# 	uc = ''
# 	for i in list_a:
# 		if i not in list_b:
# 			uc = uc+" "+i
# 	for j in list_b:
# 		if j not in list_a:
# 			uc = uc+" "+j

# 	return uc

# # Driver code
# a = "apple banana mango"
# b = "banana fruits mango"

# print("Uncommon Words are : ",uncommon(a,b))


# def add_string(str1):
#   length = len(str1)

#   if length > 2:
#     if str1[-3:] == 'ing':
#       str1 += 'ly'
#     else:
#       str1 += 'ing'

#   return str1
# print(add_string('ab'))
# print(add_string('abc'))
# print(add_string('string'))


# a = False
# b = True
# c = True
  
# if not a or b:
#     print (1)
# elif not a or not b and c:
#     print (2)
# elif not a or b or not b and a:
#     print (3)
# else:
#     print (4)

count = 1


def doThis():

    global count

    for i in (1, 2, 3):
        count += 1


doThis()

print(count)

for i in (4,3,-1):
    print(i)


str = "Python , Output , based , Questions"
word=str.split(",")
print(word)


for i in range():
    print("Python Output based Questions")
print("Python Output based Questions")\


for i in range(7,-2,-9):
	print (i)

	
L= ['a','b','c','d']
result= "".join(L)
print(result)