print("Hello! Learners.....")
#comment are Written By this "#" Symbol...specially single-line comments.

"""
these are multi-line comments....
"""

'''
these are too....
'''

# Let's Learn Varibales
abc="Priyanshu Joshi"

PriyanshuJoshi="hello"#pascals case

priyanshuJoshi="hello"#camels case

priyanshu_joshi="hello"#snake case

#Integer Type Variable
a=12 #integer
print(type(a))

#Float Type Variable
b=1.5 #float
print(type(b))
c=12/3 #floatß
print(type(c))
#Float Captures Both Decimals and Fractions

#Complex Type Variable
z=8j
print(type(z))
# As we write imaginary No. So in Python We Can Only Use j as i(substitute of imaginary(i) is j(only j nothing else)in python)

#String
st='Hello Developers' #it can also be written as "Hello Developers" both are same no diffrence
print(type(st))

#Boolean
l=True
print(type(l))

u="😭"
print(ord(u))
print(chr(65))

#string indexing
str="Hello! Developers"
print(str[0])#(H)
print(str[-1])#(s)
print(str[:6])#(Hello!)
print(str[0:5:1])#(Hello)
print(str[7:])#(Developers)

#type conversion
str1="123"
print(type(str1))#string
str1=int(str1)
print(type(str1))#integer
str1=float(str1)
print(type(str1))#float


#Input/Output in Python
str3=input("Enter Your Name: ")
str2=int(input("Enter Your Age: "))
#raw string printing
print("Your Name is ",str3 ,"\nYour age is ",str2)
#formatted string
print(f"Your Name is {str3}\nYour age is {str2}")