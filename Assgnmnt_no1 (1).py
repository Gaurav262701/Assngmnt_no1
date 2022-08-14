#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer no.1
print("Hello World")


# In[12]:


#Answer no.2
#Addition
num1 = 30
num2 = 2
sum = num1+num2
print(sum)

#Division
num3 = 30
num4 = 15
result = num3/num4
print(result)


# In[13]:


#Answer no.3
#Program to find area of triangle
a = float(input("First side area:"))
b = float(input("Second side area:"))
c = float(input("Third side area:"))
d = a+b+c
e = a+b+c/2
#Calculating the Area of a triangle using Heron’s Formula
Area = (e*(e-a)*(e-b)*(e-c))**0.5

print("perameter = %.2f"%d)
print("semi perimeter = %.2f"%e)
print("area = %0.2f"%Area)


# In[14]:


#Answer no.4
#program to swap variable
a = 10
b =5

#creating 3 variable for swapping
c = a
a = b
b = c
print("value of a after swapping: {}".format(a))
print("value of b after swapping: {}".format(b))


# In[15]:


#Answer no.5
import random
a = random.random()
print(a)


# In[ ]:




