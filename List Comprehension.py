#!/usr/bin/env python
# coding: utf-8

# # List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# ### If i want to get all square value of my current list and store it into new list

# In[2]:


list1=[]
def sqr_list(lists):
    for i in lists:
        list1.append(i*i)
        
    return list1


# In[3]:


newlist=[5,6,7,8,9,10]


# In[4]:


sqr_list(newlist)


# In[5]:


print(list1)


# ## This takes to much time and some times its very hard. We can use list comprehension to avoid that

# In[6]:


newlst=[i*i for i in newlist] #sqr value of newlist elements.. same as the above but this is easy


# In[7]:


newlst


# In[8]:


newlst2=[i*i for i in newlist if i%2==0] #we can use if else also when it needs. even numbers wala sqr root


# In[9]:


newlst2


# In[13]:


testlist=[i for i in range(0,10) if i%2==1]


# In[14]:


testlist


# In[ ]:




