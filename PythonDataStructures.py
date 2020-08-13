#!/usr/bin/env python
# coding: utf-8

# In[1]:


grocery_list = ["Chicken", "Onions", "Tomatoes", "Cooking Oil", "Royco"]
print(grocery_list)


# In[5]:


mixed_list = ["Jurugo Brian", "jurugobrian@gmail.com", "30", "20.56", ["Antonio", "Loum", "1.3"]]
print(mixed_list)


# In[6]:


for item in mixed_list:
    print(item)


# In[7]:


mixed_list[3] = ["Judith", "Arinitwe"]
print(mixed_list)


# In[8]:


"Jurugo Brian" in mixed_list


# In[9]:


"AK Mbuga" in mixed_list


# In[11]:


first_numbers = [0, 1, 2, 3, 4]
second_numbers = [5, 6, 7, 8, 9]
print(first_numbers + second_numbers)


# In[13]:


third_numbers = [10, 11, 12, 13, 14, 15]
print(third_numbers)
fourth_numbers = third_numbers * 3
print(fourth_numbers)


# In[19]:


shorter_list = mixed_list[0:3]
print(shorter_list)


# In[22]:


my_vowels = ["a", "e", "i", "o", "u"]
print(my_vowels)


# In[23]:


first_vowels = my_vowels[0:2]
print(first_vowels)
second_vowels = my_vowels[2:]
print(second_vowels)


# In[24]:


my_vowels[:3]


# In[25]:


my_vowels[2:]


# In[26]:


my_vowels[:]


# In[27]:


print(my_vowels[::2])


# In[36]:


print(my_vowels[4:1:-1])
my_vowels[:-1]


# In[41]:


my_vowels.append('j')
print(my_vowels)


# In[42]:


my_vowels.extend(['k', 'l', 'm', 'n', 'o', 'p', 'q'])
print(my_vowels)


# In[44]:


del my_vowels[6:9]


# In[45]:


print(my_vowels)


# In[46]:


del my_vowels[6]
print(my_vowels)


# In[47]:


my_vowels.sort()


# In[48]:


print(my_vowels)


# In[50]:


del my_vowels[-5]
print(my_vowels)


# In[51]:


my_vowels.pop(-1)


# In[52]:


print(my_vowels)


# In[1]:


t = ['a', 'b', 'c', 'd']


# In[2]:


t


# In[3]:


t.append('e')


# In[4]:


t


# In[5]:


u = ['n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


# In[6]:


u


# In[7]:


u.sort()


# In[8]:


u


# In[9]:


a = ['a', 'b', 'c', 'd']


# In[10]:


a


# In[11]:


b = ['e', 'f', 'g', 'h']


# In[12]:


b


# In[17]:


a.extend(b)


# In[18]:


a


# In[19]:


list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def add_all(list_nums):
    total_sum = 0
    for num in list_nums:
        total_sum += num
    return total_sum


# In[20]:


add_all(list_nums)


# In[22]:


sum(list_nums)


# In[ ]:




