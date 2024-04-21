#!/usr/bin/env python
# coding: utf-8

# In[7]:


password = 1234


# In[10]:


user_pass = int(input("please enter password"))

if user_pass == password:
    print("correct")
else:
    print("wrong")


# In[22]:


name = input("what is your name:")

if name == "GEORGE":
    print(f"i know you , {name}")
elif name == "Ben":
    print("how did you get here")
elif name == "Cece":
    print("my gee is here")
else:
    print("i no know your papa")


# In[7]:


Evm232 = int(input("what is your test score:"))
Evm554 = int(input("what is your quiz score"))
Evm613 = int(input("what is your assignment score"))
Exam = int(input("what is your exam score"))
total_score = Evm232 + Evm554 + Evm613 + Exam 
if total_score >= 70:
    print("A")
elif  total_score >= 60:
    print("B")
elif  total_score >= 50:
    print("C")
elif  total_score >= 40:
    print("D")
else:
    print("F")


# In[ ]:


# AND & OR


# In[10]:


# N ORDER TO DRIVE, YOU HAVE TO BE 18 YEARS AND ABOVE
Dlicence = input("do you have a licence:")
Age = int(input("how old are you:"))

if Age >= 18 and Dlicence == "yes":
    print("welcome, you are eligible to drive")
else:
    print("you are not eligible to drive")


# In[13]:


# BOB RICE OR BEANS

Rice = input("Did you cook rice madam")
Beans = input("Did you cook beans madam")
if Rice == "yes" or Beans == "yes":
    print("buy")
else:
    print("I no dey buy")


# In[14]:


### IF/ELIF/ELSE AND/OR statement 


# In[19]:


weather = input("what is the weather like (cold, warm, freezing):")
temperature = int(input("what is the temperatue (in celsius):"))

# processing weather/temperature to recommend activities
if weather.lower() == "warm" and temperature >= 40:
   activity = "it is safe to drive/work"
elif weather.lower() == "cold" and temperature < 30:
   activity = "it is a nice day for walk/jog"
elif weather.lower() == "freezing" or weather.lower() == "cold":
    activity = "it is too cold to drive/walk"
else:
    activity = "udo di na beanyi"
# output
print(activity)


# In[ ]:


### FINANCIAL ADVICE BASED ON AGE


# In[29]:


# INPUT age and annual income
Age = int(input("How old are you",))
income = float(input("What is your annual income? "))

if Age < 30 and income < 50000:
    financial_advice = "it is the right time to start saving money"
elif Age < 30 and income >= 50000:
    financial_advice = "they have to start investing"
elif Age >= 30 and income < 50000:
    financial_advice = "creating a budget plan could help manage your finance"
elif Age >= 30 and income >= 50000:
    financial_advice = "start planning for your retirement"
elif income > 100000 or Age > 65:
    financial_advice = "with your income and age, speaking to a financial advicer is important"
else:
    financial_advice == "seeking a personal financial adviser will be the best action"
print(financial_advice)


# In[ ]:


# FOR LOOP


# name = "George"
# for g in range(4):
#     print(name)

# In[34]:


list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)


# In[49]:


# EVEN Number
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print(f"{num} is an odd number")


# In[41]:


# ODD number
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if num % 2 == 1:
        print(num)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




