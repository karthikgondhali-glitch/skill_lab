'''import keyword
print (keyword.kwlist)


a=None
print(a)
a=0
print(type(a))
print(bool(a))
print(bool(0.0))
print(bool(1.8))
print(int())

a=3j+5
print(a)

a="Happy Father's Day"
print(a)
# To access F 
print(a[6])

#List
my_list = [1, 2, 3, 4, 'hello', 5.6, True]
# to Extract hello from the list
print(my_list[4])
# Now H from hello 
print(my_list[4][0])

#Appened Function
my_list.append(10)
print(my_list)

#Pop Function
print(my_list.pop())
print(my_list)
#finding data type of list
print(type(my_list))

#TUPLE
my_tuple = (1, 2, 3, 4,5J,'hello', 5.6, True,)
#set operations     
set1 = {1, 2, 3, 4, 'hello', 5.6, True}
print(type(set1))

my_dict = {'a':[10,20,30], 'b':[40]}
print(my_dict['a'][-2])
#list of keys
print(my_dict.keys())

#slicing 
a = "hello world"
print(a[0:5])
print(a[6:11])
print(a[2:4])
print(a[2:4 + 1:3])

#accesing from right to left
print(a[-8:-10:-1])
a = "good morning"
print(a[7:11])
#same with negative indexing
print(a[-5:-1])

a = "hello"
print(a[3:0:-1])
#same with negative indexing
print(a[-2:-5:-1])
#reverse the string
print(a[::-1])

a = "good morning"
print(a[1:5+1:2])
#extract mng
print(a[5::3])
#reversing the same mng
print(a[-7::3])

print(a[3:0:-1])
print(a[10:4-1:-3])

#collection of type input
a = eval(input("Enter : "))
print(a,type(a))

b = int(input("Enter : "))
if b%2==0:
    print("Even")
else:
    print("Odd")
c = eval(input("Enter : "))
if (len(c)==5):
    print("the length of the list is 5")
else:
    print("the length of the list is not 5")

print(ord('j')+ord('a')+ord('v')+ord('a'))
print(chr(65))
print(chr(95))    

#how to change capital latter to small letter without using inbuilt function
chr = input("Enter a capital letter : ")
if "A" < chr < "Z":
    print("upper case letter")
elif "a" < chr < "z":
    print("lower case letter")
else:
    print("not a letter")           


un = input("Enter a user name : ")
if un =='hero':
    print("user name is correct")
    pow=(input("Enter a password : ")) 
    if pow == 'hero123':
        print("successfully logged in")
    else:
        print("incorrect password")        
else:
    print("incorrect user name")

i=100
while i<=100 and i>=1:
    print(i)
    i-=1

n= int(input("Enter a number : "))
rev=0
while(n <0):
    ld=n%10
    n= n//10
    rev=rev*10+ld
print(rev)    

l = [10,20,30,40,50]
for i in l:
    print(i)

s = input('enter:')
out=''
for i in s:
    if"A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif"a"<=i<="z":
        out+=chr(ord(i)-32)
    else:
        out+=i    
print(out)        

s = input("Enter a string : ")
rev = ''
for i in s:
    rev = i + rev
print(rev)

#Nested for Loops 
for i in range(1, 6):
    for j in range(1, 6):
        print('*', end=' ')
    print()



for i in range(1, 6):
    for j in range(1, 6):
        if i==j:
            print('*', end=' ')
        else:
            print('@', end=' ')
    print()

a = "happy birthday"
#slice htr
print(a[-4:-7:-1])
#functions with arg with return
def convert_to_uppercase(s,out):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result
print(convert_to_uppercase(input("Enter a string : "),""))

#function with arg without return
def convert():
    s= input("enter:")
    out=''
    for i in s:
        if"a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
convert()
#function without arg with return

#function without arg without return
# class and object
class college:
    cname ="gopalan"
    cloc="bangalore"
s1=college()
print(s1.cname)
print(s1.cloc)
college.cloc = "mysore"
s2=college()
print(s2.cname)#this is a class variable which is shared by all the objects of the class
print(s2.cloc)#this is a class variable which is shared by all the objects of the class

s1=college()
s1.sname='EREN'
s1.phone='0000000000'

s2=college()
s2.sname='MIKASA'
s2.phone='0000000001'

print(s1.cname)
s1.cloc='KR puram'
print('After Changing')
print(s1.cloc)
print(s2.cloc)
print(college.cloc)
print(s1.phone)'''
class college():
    def __init__(self,sname,phno,usn):
        self.sname=sname
        self.phno=phno
        self.usn=usn

s1=college('EREN','0000000000','DEMO001')
s2=college('MIKASA','0000000001','DEMO002')
print(s1.sname)
print(s1.phno)
s1.display= lambda : print(s1.sname,s1.phno,s1.usn)
s1.display()
