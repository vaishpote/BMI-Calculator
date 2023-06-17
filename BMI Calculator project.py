#!/usr/bin/env python
# coding: utf-8

# In[1]:


# BMI = (Weight in pounds * 703) / (height in inches * height in inches)


# In[14]:


name = input("Enter you name")

weight = int(input("Enter your weight"))

height = int(input("enter your height"))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name+ " , you are under weight. you need to have balance diet")
    elif(BMI<24.9):
        print(name+ " , you are normal weight. you are going well . keep it up")
    elif(BMI<29.9):
        print(name+ " , you are overweight , you need to exercice more and stop sitting and writing so many python codes")
    elif(BMI<34.9):
        print(name+ " , you are obese. you need to do exercise and diet regular")
    elif(BMI<40):
        print(name+ " , you are mordily obese. you need to do exercise and diet and don't choose cheat day for a 6 month regularly ")
    else:
        (name+ " , you are severly obese")


# In[ ]:





# In[ ]:





# In[ ]:


#print(weight)


# In[16]:


#Under 18.5 - Underweight minimal
#18.5 - 24.9 - normal weight - minimal
#25.9 - 29.9 - overweight - increased
#29.9 - 34.9 - obese - high
#35 - 39.9 - severely obese - very high
#40 and overmoridly obese - Extreamely high


# In[ ]:




