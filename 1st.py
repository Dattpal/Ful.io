#!/usr/bin/env python
# coding: utf-8

# In[1]:


# number is valid or not
import re

def isValid(s):
    Pattern = re.compile("()|[+]|(0|2)[-]|[0-9]|[-]")
    return Pattern.match(s)

Num=["+918347419912","212-456-7890","(212)456-7890","(212)-456-7890",
     "212.456.7890","212 456 7890","+12124567890","+12124567890",
     "+1 212.456.7890","+212-456-7890","1-212-456-7890"]
for i in Num:
    if (isValid(i)):
        print ("Valid  Number:",i)
    else :
        print ("Invalid Number:",i)

