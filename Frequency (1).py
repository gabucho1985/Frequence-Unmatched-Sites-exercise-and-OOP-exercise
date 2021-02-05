#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[6]:


#1.	What is the frequency of each email domain in the dataset

import numpy as np
import pandas as pd
import csv
import string
from itertools import zip_longest
from collections import Counter
import re
data= pd.read_csv(r'C:\Users\Patricia Distano\Desktop\PIPL Project\email_data_set_pipl.csv')
data
#datas= data['email'].str.split('@').str[0] # it will get the names rather than emails like line below, for instance
g= data['email'].str.split('@').str[-1] #this will get the domain ex: verizon.net, cox.net, etc.

dtype_before = type(data['email']) 
list1 = data['email'].tolist()
#list1 = [g.strip(' ') for g in list1]
dtype_after = type(list1)
list1= [x for x in list1 if str(x) != 'nan']
list1 = [u.strip(' ') for u in list1]
#print(list1)
list11=[i.split('@', 1)[-1] for i in list1] #check this 


x=Counter(list11)
#print(len(x))
print("There are " + str(len(x)) + " different types of domains: ")
print("\n")
#Counter({'verizon.net': 5, 'attb1.com': 3, 'cox.net': 2}
for i in x.items(): #In Python Dictionary, items() is used to return the list with all dictionary keys with values
    total= ((i[1]/5000) * 100) # i[1]{ gets the value  ex: 5,3 and 2  from 'verizon.net': 5, 'attb1.com': 3, 'cox.net': 2}
    print(round(total, 2),"%", "of emails have the domain", i[0])


# In[5]:


#compare sites(mnemonic) from "Unknown" against other columns (US,EMEA ASIA, CANADA,LATAM) and we are trying to find 
#sites from "Unknown" that no longer exist in any of the otehr regions

import numpy as np
import pandas as pd
import csv
import string
from itertools import zip_longest
#import re
data= pd.read_csv(r'C:\Users\Patricia Distano\Anaconda3\pkgs\notebook-5.7.8-py37_0\hi.csv')
#data
#data.dropna(inplace = True)
dtype_before = type(data['Unknown']) 
list1 = data['Unknown'].tolist()
#list1 = [g.strip(' ') for g in list1]
dtype_after = type(list1)
list1= [x for x in list1 if str(x) != 'nan']
list1 = [u.strip(' ') for u in list1]
print(len(list1))

dtype_befor = type(data['US'])
list2 = data['US'].tolist()
dtype_afte = type(list2)
list2= [x for x in list2 if str(x) != 'nan']
list2 = [u.strip(' ') for u in list2]
#print(list2)

dtype_befo = type(data['EMEA'])
list3 = data['EMEA'].tolist()
dtype_aft = type(list3)
list3= [x for x in list3 if str(x) != 'nan']
list3 = [u.strip(' ') for u in list3]
#print(list4)

dtype_bef = type(data['ASIA'])
list4 = data['ASIA'].tolist()
dtype_af = type(list4)
list4= [x for x in list4 if str(x) != 'nan']
list4 = [u.strip(' ') for u in list4]
#print(list5)

dtype_be = type(data['CANADA'])
list5 = data['CANADA'].tolist()
dtype_a = type(list5)
list5= [x for x in list5 if str(x) != 'nan']
list5 = [u.strip(' ') for u in list5]
#print(list6)

dtype_b = type(data['LATAM'])
list6 = data['LATAM'].tolist()
dtype_ = type(list6)
list6= [x for x in list6 if str(x) != 'nan']
list6 = [u.strip(' ') for u in list6]
#print(list3)

superlist=[[],[],[],[],[]]
def finalList(lista, lis, supe):
    for i in lista:
        for g in lis:      
            if i[:5]==g[:5]:
                if i[:] not in supe:
                    #continue
                    supe.append(i[:])

            
finalList(list1, list2, superlist[0])
finalList(list1, list3, superlist[1])
finalList(list1, list4, superlist[2])
finalList(list1, list5, superlist[3])
finalList(list1, list6, superlist[4])

lista11=[]
for z in list1:
    if z in superlist[0]:
        continue
    if z in superlist[1]:
        continue
    if z in superlist[2]:
        continue
    if z in superlist[3]:
        continue
    if z in superlist[4]:
        continue
    else:
        lista11.append(z)

#print(lista11)
total= len(superlist[0]+superlist[1]+superlist[2]+superlist[3]+superlist[4]+lista11)

print("Total is: " + str(total))

print(str(total))
print(superlist[0])
print(len(superlist[0]))
print(superlist[1])
print(len(superlist[1]))
print(superlist[2])
print(len(superlist[2]))
print(superlist[3])
print(len(superlist[3]))
print(superlist[4])
print(len(superlist[4]))

g=[superlist[0], superlist[1], superlist[2], superlist[3], superlist[4], lista11]

export_data = zip_longest(*g, fillvalue = '')
with open('mynewfile.csv', 'w', encoding= "ISO-8859-1", newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['US', 'EMEA', 'ASIA', 'CANADA', 'LATAM', 'Unknown'])
    wr.writerows(export_data)
    myfile.close()
    


# In[ ]:


#Code using OOP where two children classes inherit from the parent class. 
# Here we write to 2 files (text file and csv file)
from abc import ABC, abstractmethod
import datetime
#import io
class WriteFile(ABC):
    def __init__(self, file, word, delim):
        self.file    =  file
        self.word    =  word
        self.delim   =  delim
        super().__init__()
    
    @abstractmethod
    def write(self):
        pass
    
class LogFile(WriteFile):
    def __init__(self, file):
        self.newfile =   open (file, 'w')
                  
    def write(self, word):
        self.nf  =  self.newfile.write(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))+"   "+ str(word)+ "\n") 
        #self.nf  =  self.newfile.close()
        return   self.nf 
    
#csvfile = io.StringIO()
class DelimFile (WriteFile):
    def __init__(self, file, delim):
        self.newfile = open (file, 'w', newline='')
        self.newfile2= csv.writer(self.newfile)
    
    def write(self, word): 
        self.newfile2.writerow(word)

log = LogFile('log.txt')        
mydelim = DelimFile('cas.csv', ',')  
mydelim.write(['a', 'b', 'c', 'd'])       
mydelim.write(['1', '2', '3', '4'])          
log.write('this is a log message') 
log.write('this is another log message')


# In[ ]:


#code to Get max/min/avg/median/mode/IQR number from list
from collections import Counter 
import math 

class Numeros:
    def __init__(self, mylist):
        self.mylist = mylist
        #self.mas    = mas
        print("Get max/min/avg/median/mode number from list: ")
        
    def num_mayor(self, mas):
        self.mas= mas
        for i in self.mylist:
            if i > mas:
                mas=i
        return mas
    
    def num_menor(self, menor):
        self.menor = menor
        for i in self.mylist:
            if i>menor and menor==0:
                menor=i
            if i<menor:
                menor=i
        return menor
    
    def num_avg(self, number):
        self.number = number
        for i in self.mylist:
               if i > 0:
                    number+=i
        return number/len(self.mylist)
    
    def num_median(self):
        #self.mylista = mylista
        print(sorted(self.mylist))
        
        if len(sorted(self.mylist))%2!=0: # for odd numbers only
            g=math.floor(len(sorted(self.mylist))/2)# answer is 2.5 but with floor(will bring it to 2)
            #print(g)                               # ceil(2.5) will be 3
            #print("Median number is: " + str(sorted(self.mylist)[g]))
            #print(str(sorted(self.mylist)[g]))
            return sorted(self.mylist)[g]
        
        else:
            m=math.floor(len(sorted(self.mylist))/2)
            #print(m)
#             print(sorted(self.mylist)[m])
#             print(sorted(self.mylist)[m-1])
            #print("Median number is: " +str(((sorted(self.mylist)[m]) + (sorted(self.mylist)[m-1]))/2))
            return ((sorted(self.mylist)[m]) + (sorted(self.mylist)[m-1]))/2
            
    def most_frequent(self): 
        occurence_count = Counter(self.mylist) 
        print("The mode is: " + str(occurence_count.most_common(1)[0][0])) # (1) will give you the set that repeats the most
                                                                           #[0] "" the set itself for ex:(2,9) meaning
                                                                           #2 is 9 times on tne list
                                                                          #[0][0] ""will give you the 2 out of (2,9)
                                                                            
        
class Inter_Quart_Range(Numeros):
     #def __init__(self, mylist): 
        #super().__init__(mylist)
        #Numeros.num_median(self)
        def min_interq(self, menor):
            
            #return Numeros.num_menor(self, menor)*Numeros.num_mayor(self, mayor) #change print for return in num_median
            return  Numeros.num_menor(self, menor) * Numeros.num_median(self) 
            #g=int(Numeros.num_menor(self, menor))
            #print(f)
            #for i in self.mylist:
            #c= int(a-b)
            #print(a)
            #print(b)
    
        
            
mylista=[10,20,40,30,10]       
#mylista=[10,20,30,40,50,60,70,80,90,100,110]   
mynumber=Numeros(mylista)
myqrange=Inter_Quart_Range(mylista)
#myqrange.min_interq(0)
# myqrange
# mynumber.num_mayor(0)
# mynumber.num_avg(0)
# print("Max number is: " + str(mynumber.num_mayor(0)))
print("Min number is: " + str(mynumber.num_menor(0)))
# print("Avg number from list is: " + str(mynumber.num_avg(0)))
# mynumber.num_menor(0)
print(mynumber.num_median())
# mynumber.most_frequent()
myqrange.min_interq(0)


# In[ ]:




