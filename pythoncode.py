'''
y= 4
x='vamsi'
print (x+str(y))
a,b='vmc','krn'
print(a,b)

n1=3+5j
n2=3+3j

print(n1+n2)

import random
print(random.randrange(0,5))
st1='hello . world!  '
print(st1.strip())

print(st1.replace('h','j'))

t=(st1.split('.'))
print(t[0].strip())

age=50
weight=70

txt=" your weight is {} ,your age is {} "

print(txt.format(weight,age))
'''

'''s1=8
s1<<=1
print(s1)

items=['apple','banana','choc']
for x in items:
    if 'apple' or 'banana' in x:
        print('omg apple and banana!')
    print(x)

items.append('orange')
print (items)
citems=items.copy()
print(citems)
'''

# dictval={'a':'apple','b':'banana','c':'cherry'}
# for ab,cd in dictval.items():
#     print('a= {} and b={}' .format(ab,cd))
#
# dictval2={1:'one',2:'two',3:'three'}
# for k in dictval2.keys():
#     print('key= {} value={}' .format(k,dictval2.get(k)))
# dictval3={'apple':100,'mango':200}
# for s in dictval3.keys():
#     print(s,dictval3.get(s))
#
# x= lambda a: a+10
# print(x(10))
#
# user='vmc'
# def change(name):
#     globals() ['user']='vamsi'
#     user=name
#     print(user)
# change('kiran')
# print(user)
#
# import math
# print (math.__name__)
# print(math.__doc__)
# import io
# print(io.__file__)
# print(math.__dict__)
#
# print("new method",dir(math))
# def fibo():
#     a,b=0,1
#     fibolist=[]
#     n=int(input("enter the number"))
#     while b<n:
#         fibolist.append(b)
#         a,b=b,a+b
#     return fibolist
#
# if __name__=='__main__':
#     print("fibo",fibo())
#
# help('modules')


# import os
# #os.mkdir('d:\\tempdir')
# print(os.getcwd())
# os.rmdir('d:\\tempdir')

# import sys
#
#
# print(sys.version)
#
#
# import math
# print(math.sin(60))
# print(math.log2(8))
#
#
#
# def getseq(x):
#     try:
#         for a in range(x):
#             yield a
#     except StopIteration:
#         print('exit')
#
#
# val=getseq(5)
# next(val)
#
# squr=(x*x for x in range(5))
# for a in range(5):
#     print(next(squr))
#
# import math
# sum=sum(x*x for x in range(5))
# print (sum)
#
# def square(x):
#     return x*x
# numbers=[1,2,3,4,5]
#
# val=map(square,numbers)
#
# for x in range(5):
#      print(next(val))

#
# val2=[1,2,3,4,5]
# result=map(lambda x:x*x ,val2)
# for a in range(5):
#     print(next(result))
#
# def isprime(x):
#     for a in range(2,x):
#         if x%a==0:
#             return False
#         else:
#             return True
#
# primenumbers=filter(isprime,range(20))
# print(list(primenumbers))
#
# import functools
# def sqr(x,y):
#     return x*y
# fact=functools.reduce(sqr,range(1,6))
# print (fact)
#
# list1=[1,2,3]
#
# list2=[4,5,6]
#
# combo=[(x,y) for x in list1 for y in list2]
# print (combo)
#
#
# matrix=[ [1,2,3],[4,5,6]]
#
# data=[num for row in matrix for num in row]
# print(data)
#
# def facto(num):
#     if num==1:
#         print (num)
#         return 1
#     else:
#         return num*facto(num-1)
#
# print(facto(5))

# num=10
# # assert num<25,"number should be less than 5"
# # print("value is {}" .format(num))
#
# def display(str):
#      print(str)
# def decofunc(fn):
#     def wrapper_display(value):
#         print("output",end=" ")
#         fn(value)
#     return wrapper_display
# x=decofunc(display)
# x("vamsi")
#
# @decofunc
# def show(a):
#     print(a)
#
# show('kiran')
#
#
#
# def calculator_decorator(func):
#     def calc_wrapper(x,y):
#         print('the sum of two numbers is',end=" ")
#         func(x,y)
#     return calc_wrapper
#
# @calculator_decorator
# def addnumbers(a,b):
#     print(a+b)
# addnumbers(5,10)

#
# class person:
#     def __init__(self):
#         self.__name=""
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
#     @name.deleter
#     def name(self):
#         print('deleting value')
#         del self.__name
#
# p1=person()
# p1.name="vamsi"
# print(p1.name)
#
# del p1.name
#
# print(p1.name)
#
# class quard:
#     def __init__(self,a,b,c,d):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#     def perimeter(self):
#         p=(self.a+self.b+self.c+self.d)
#         return p
#
# q=quard(1,2,3,4)
# print(q.perimeter())
#
# class rect(quard):
#     def __init__(self,a,b):
#         super().__init__(a,b,a,b)
#
#     def area(self):
#         return (self.a*self.b)
#
#
# class square(rect):
#     def __init__(self,a):
#         super().__init__(a,a)
#
#     def area(self):
#         return pow(self.a,2)
#
# s=square(4)
# print(s.area())
# r=rect(2,4)
# print(r.area())
#
# f=open('D:\sampletest.txt','w')
# f.write("hello world")
# f.close()

# f=open('D:\sampletest.txt','r')
# while True:
#     try:
#         line=next(f)
#         print(line)
#     except StopIteration:
#         break
#
# f.close()
#
# f=open()
# def mybuttonclick():
#     print('clicked')
#
#
# from tkinter import *
#
# window=Tk()
# btn=Button(window,text='click to start',fg='yellow',bg='black')
# #btn.bind('<button-1>',mybuttonclick)
# btn.place(x=150,y=100)
# window.title("snake game")
# window.geometry("400x200+10+10")
# window.mainloop()


# import mysql.connector
#
# # mydb=mysql.connector.connect(
# #
# #     host='127.0.0.1',
# #     user='root',
# #     passwd='root123'
# # )
# # mycursor=mydb.cursor()
# # mycursor.execute('Create DATABASE mystore')
#
#
# # mydb=mysql.connector.connect(
# #
# #     host='127.0.0.1',
# #     user='root',
# #     passwd='root123',
# #     database='mystore'
# # )
#
# # mycursor=mydb.cursor()
# #mycursor.execute('create table jail (rooms varchar(50),incharge varchar(20),incharge_id int)')
# #mycursor.execute('create table prisoners (name varchar(30),assigned_to int)')
# # sql='insert into jail values (%s,%s,%s)'
# # val=[('ordinary','nik',1),
# #      ('ordinary','ashwik',2),
# #      ('oridinary','vamsee',3),
# #      ('oridinary','john',4)]
# # sql='insert into prisoners values (%s,%s)'
# # val=[('nikhil',3),
# #      ('ram',1),
# #      ('ali',1),
# #      ('pete',3),
# #      ('ash',2),
# #      ('nish',1)]
# # mycursor.executemany(sql,val)
# # mydb.commit()
#
# # sql='select rooms,incharge,name from jail right join prisoners on jail.incharge_id=prisoners.assigned_to'
# # mycursor.execute(sql)
# # data=mycursor.fetchall()
# # for x in data:
# #     print(x)
#
# #
# # import pymongo
# #
# #
# # client = pymongo.MongoClient("mongodb+srv://vamsi:<vamsi>@cluster0-mhtkr.mongodb.net/test?retryWrites=true&w=majority")
# # mydb=client['mongodb2']
# # mycol=mydb['employee1']
# #
# # my_dict={'name':'vamsee','age':23}
# # x=mycol.insert_one(my_dict)
# # y=mycol.find_one()
# # print(y)
#
# # db = client.test
# # print(db)
#
# # myclient=pymongo.MongoClient('mongodb+srv://root:<root123>@cluster0-mhtkr.mongodb.net/test?retryWrites=true&w=majority')
# # mymongodb=myclient['mongodatabase']
# # dblist=myclient.list_database_names()
# # if 'mongodatabase' in dblist:
# #     print('data base exist')
#
#
# # x=input("enter string to reverse")
# #
# # rev=x[::-1]
# # print(rev)
#
# # mylist=list()
# # op='Y'
# # while op=='Y':
# #     mylist.append(input('enter list item'))
# #     op=input('enter Y to add more ,enter N to exit')
# #
# # newlist=list(dict.fromkeys(mylist))
# # print(newlist)
#
# # def print_directory_contents(sPath):
# #     import os
# #     for sChild in os.listdir(sPath):
# #         sChildPath = os.path.join(sPath,sChild)
# #         if os.path.isdir(sChildPath):
# #             print_directory_contents(sChildPath)
# #         else:
# #             print(sChildPath)
#
# # def print_directory_contents(sPath):
# #     import os
# #     for sChild in os.listdir(sPath):
# #         sChildpath=os.path.join(sPath,sChild)
# #         if os.path.isdir(sChildpath):
# #             print_directory_contents(sChildpath)
# #         else:
# #             print(sChildpath)
# #
# # import os
# # x=os.walk(".",topdown=False)
# # print(next(x))
# # def sq(x):
# #     return (x*x)
# #
# #
# # import cProfile
# # cProfile.run(sq(2))
# #
# # import re
# #
# # regex=r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$'
# # email='ayushiwashere@gmail.com'
# # # reg= re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$','ayushiwashere@gmail.com')
# # reg= re.search(regex,email)
# # print(reg.group())
# # lis=[1,2,3,5,9,8,6,4,5]
# # n=int(input('enter x'))
# # count=0
# # for x in range(1,n):
# #     if x in lis:
# #         count=count+1
# #     if count>=2:
# #         print(x)
# #     count=0
#
# # listval=[1,2,3,55,8,8,6,4,55]
# # k=66
# #
# # def substr():
# #     sum = 0
# #     for x in listval:
# #         sum=sum+x
# #         if sum==k:
# #             return True
# #         else:
# #             return False
# #
# #
# #
# # print(substr())
# # import functools
# #
# # def subarr(xval,y):
# #         z = xval + y
# #         if z==k:
# #             return 1
# # for x in range(len(listval)):
# #     a=[]
# #     a.append(x)
# #     res=functools.reduce(subarr,[1,2,3,55,8,8,6,4,55])
# #     if res==1:
# #         print(a)
# #         break
#
#
#
#
# #res=list(dict.fromkeys(listval))
#
# #print(res)
#
#
# # list1=[1,2,3,4]
# # list1 *=0
# # print(list1)
# # list2=[5,6,7,3,2,1]
# # x=list2[]
# # print(x)
#
#
#
#
#
# # def Reverse_items(items):
# #     newlist=items[::-1]
# #     return newlist
#     # approach 2
#     # items.reverse()
#     # return items
#     # approach 1
#     # return [x for x in reversed(items)]
#
#
# # def rev_items(li_items):
# #     return [val for val in li_items[::-1]]
# #
# #
# # items=[8,6,5,9,3,7]
# # print(rev_items(items))
# #
# #
# #
# # ltems=[6,7,4,3,8,5]
# # print(Reverse_items(ltems))
#
# # def cloning(items):
# #     items_copied=items[:]
# #     return items_copied
# #
# # list1=[4,5,3,2,8,9]
# # print(list1)
# # list1.append(10)
# # list2=cloning(list1)
# # list1.append(99)
# # print(list2)
# # print(list1)
#
# # def cloning(items):
# #     items_copied=items[:]
# #     return items_copied
# #
# # items=[4,3,5,6,2,8]
# # print(items)
# # print(cloning(items))
# # items.append(10)
# # print(items)
#
# # from collections import Counter
# # list_items=[8,6,7,9,4,2,3,2,2,6,22]
# # x=2
# #
# # #using simple approach
# # def method1(list_items):
# #     count =0
# #     for items in list_items:
# #         if items==x:
# #             count=count+1
# #     return count
# #
# # #using count() method
# # def method2(list_items):
# #     return list_items.count(x)
# #
# # #using counter()
# # def method3(list_items):
# #     dict=Counter(list_items)
# #     return dict
# #
# # dict_items=method3(list_items)
# # print('the element {} has appeared {} times' .format(x,dict_items[x]))
#
# # list_items=[3,5,7,1,9]
#
# # def sum_of_list(list_items,size):
# #     if (size ==0):
# #         return 0
# #     else:
# #         return list_items[size-1]+sum_of_list(list_items,size-1)
# #
# # tot=sum_of_list(list_items,len(list_items))
# # print(tot)
# #
# # tot=sum([x for x in list_items])
# # print(tot)
#
# # def multiply_items(list_items):
# #     result=1
# #     for x in list_items:
# #         result=result*x
# #     return result
# #
# #
# #
# # import numpy
# # print(numpy.prod(list_items))
# #
# # from functools import reduce
# #
# #
# # def mul_function(x,y):
# #     return x*y
# #
# # list_values=[8,9,4,5,7,8]
# # result=reduce(mul_function,list_values)
# # print(result)
# #
# # list_values2=[5,7,9,3,1,8]
# # result1=reduce((lambda x,y:x*y),list_values2)
# # print(result1)
# #
# # list_values2.sort()
# # print(list_values2[:1])
#
# # find the second maximum element
# # val=[10,99,45,20,8]
# # max=max(val[0],val[1])
# # second_max=min(val[0],val[1])
# #
# # for i in range(2,len(val)):
# #     if val[i]>max:
# #         second_max=max
# #         max=val[i]
# #     else:
# #         if val[i]>second_max:
# #             second_max=val[i]
# #
# # print('the second highest element is',str(second_max))
#
# #
# # def Nmaxelements(items,n):
# #     final=[]
# #     for i in range(0,n):
# #         max=0
# #         for j in range(len(items)):
# #             if items[j]>max:
# #                 max=items[j]
# #
# #         items.remove(max)
# #         final.append(max)
# #     print(final)
# #
# # list1=[5,7,3,7,8,2]
# # n=3
# # Nmaxelements(list1,n)
# # list_values=[5,2,8,9,4,2,6]
# # even_numbers=[num for num in list_values if num%2 == 0]
# # print('even numbers list is',even_numbers)
# #
# # evns=list(filter(lambda x:(x%2 ==0),list_values))
# # print(evns)
# #
# # even_count=len(list(filter(lambda x:(x%2 ==0),list_values)))
# # odd_count=[ num for num in list_values if num%2!=0]
# # count=len(odd_count)
# # print(even_count,count)
# #
# # list_tuples=[(),(2,3,5),('','','hi'),(),(''),(1,2,3)]
# #
# # def remove_empty(tuples):
# #     tuples=[ t for t in tuples if t]
# #     return tuples
# #
# # print(remove_empty(list_tuples))
# #
# #
# # def repeat(x):
# #     size=len(x)
# #     repeated=[]
# #     for i in range(size):
# #         k=i+1
# #         for j in range(k,size):
# #             if (x[i]==x[j] and x[i] not in repeated):
# #                 repeated.append(x[i])
# #
# #     return repeated
#
# #print(repeat([4,5,3,3,4,5,6,7,8]))
#
# #mylist1=['hello','world','world','hi','this','is','29th','july']
# # mylist1=['a','z','c','b','g','d','i']
# # mylist2=[0,1,0,0,2,3,4,5,7]
# # # def divide_chunks(items,n):
# #     for i in range(0,len(items),n):
# #         yield items[i:i+n]
# #
# #
# # n=3
# # res=list(divide_chunks(mylist,n))
# # print(res)
# # x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# # y = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]
# # def sort_list(list1,list2):
# #     zipped_pair=zip(list2,list1)
# #     z=[x for _,x in sorted(zipped_pair)]
# #     return z
# # print(sort_list(mylist1,mylist2))
# #input_str='malayalamt'
# import math
# # def is_palindrome(name):
# #     rev=name[::-1]
# #     return rev
#
# # if input_str==is_palindrome(input_str):
# #     print('it a palindrome')
# # else:
# #     print('not a palin')
# #
# # for i in range(0,math.ceil(len(input_str)/2)):
# #     if input_str[i]!=input_str[len(input_str)-i-1]:
# #         print('not a')
# #         break
# #     print('its a')
# #
# #
# # reverse=''.join(reversed(input_str))
# # print(reverse)
#
# # sentence='hello i am vamsee from mpl'
# # input_words=sentence.split(" ")
# # print(input_words)
# #
# # input_words=input_words[::-1]
# # print(input_words)
# # output='    '.join(input_words)
# # print(output)
#
# # def check(str1,str2):
# #     if(str1.find(str2)==-1):
# #         print('no')
# #     else:
# #         print('yes')
# #
# # str1='vamsee kiran'
# # str2='iran'
# # check(str1,str2)
#
# # def count(str1,str2):
# #     set_string1=set(str1)
# #     set_string2=set(str2)
# #     matched_characters=set_string1 & set_string2
# #     print('the no of matched characters are {}'.format(len(matched_characters)))
# #
# # if __name__=='__main__':
# #     str1='aabcdddlk@1'
# #     str2='cddacfk'
# #     count(str1,str2)
# # def vowel_count(str):
# #     count=0
# #     vowel=set('aeiouAEIOU')
# #     for i in str:
# #         if i in vowel:
# #             count=count+1
# #
# #     print('no of vowel- {}'.format(count))
# #
# # str="GeeksforGeeks"
# #
# # vowel_count(str)
#
#
# # from collections import OrderedDict
# #
# # def removeDupWithOrder(str):
# #     return "".join(OrderedDict.fromkeys(str))
# #
# # print(removeDupWithOrder('geeksforgeeks'))
#
# # from collections import OrderedDict
# # seq=('name','age','gender','age')
# # dict=OrderedDict.fromkeys(seq)
# # print(dict)
# #
# # dict1=OrderedDict.fromkeys(seq,10)
# # print(dict1)
#
#
# import turtle
#
# # def run(str):
# #     regex=re.compile('[!@#$%^&*()_+{}:?/\']')
# #     if (regex.search(str) ==None):
# #         print('string is accepted')
# #     else:
# #         print('string is not accepted')
# #
# # str='hellow  man'
# # run(str)
#
# # import turtle
# #
# # def square():
# #     window = turtle.Screen()
# #     window.bgcolor("skyblue")
# #
# #     brad = turtle.Turtle()
# #     brad.shape("square")
# #     brad.forward(100)
# #     brad.right(90)
# #     brad.forward(100)
# #     brad.right(90)
# #     brad.forward(100)
# #     brad.right(90)
# #     brad.forward(100)
# #     brad.right(90)
# #     brad.circle(250)
# #     brad.fillcolor("red")
# # square()
# import psycopg2
#
# # import re
# # str='vmc123@gm.in'
# # regexp=r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$'
# # reg= re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$','ayushiwashere@gmail.com')
# # if regexp.search(str)==None:
# #     print('the is not valid address')
# # else:
# #     print('this is valid')
#
# # import re
# #
# # regex=r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$'
# # email='ayushiwashere2@gmail.com'
# # reg= re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$','ayushiwashere@gmail.com')
# # reg= re.search(regex,email)
# # print(reg)
# #
# # regex=r'[0-9a-zA-Z.]+@[a-zA-Z]+'
#
# # import string
# # import random
# # import time
# # possible_chars=string.ascii_lowercase+string.digits+string.ascii_uppercase
# # print(possible_chars)
# # text='vmc'
# # attemptone=''
# # counter=0
# # while (attemptone!=text):
# #     attemptone=''.join(random.choice(possible_chars) for i in range(len(text)))
# #     print(attemptone)
# #     counter=counter+1
# #
# # print('value found at {}'.format(counter))
#
# # import random
# # import string
# # possible_chars=string.ascii_lowercase+string.digits+string.ascii_uppercase
# # attempt_one=''
# # text='34g'
# # counter=0
# # while(text!=attempt_one):
# #     attempt_one=''.join(random.choice(possible_chars) for i in range(len(text)))
# #     counter=counter+1
# #
# # print(counter)
#
#
# # def str_len(k,str):
# #     temp_str=[]
# #     text=str.split(" ")
# #     for i in text:
# #         if len(i)>= k:
# #             temp_str.append(i)
# #
# #
# #     return temp_str
# #
# # str='hello vamsi welcome to mpl'
# # print(str_len(3,str))
#
# # def remove(string,i):
# #     str=""
# #     count=0
# #     for val in string:
# #         if count!=i:
# #             str=str+val
# #         count=count+1
# #
# #     return str
# #
# # print((remove('hello',3)))
#
#
# # Function to find all close matches of
# # input string in given list of possible strings
# # from difflib import get_close_matches
# #
# # def closeMatches(patterns, word):
# # 	print(get_close_matches(word, patterns))
# #
# # # Driver program
# # if __name__ == "__main__":
# #     word = 'puppi'
# #     patterns = ['puppy','pupper' ,'ded', 'doggie']
# #     closeMatches(patterns,word)
#
# # from difflib import get_close_matches
# # items=['nik','akhil','sunil','ash']
# # text='nikhil'
# # res=get_close_matches(text,items)
# # print(res)
# #
# # str1='hello this is vamsee'
# # str2='hello this is john'
# #
# # str_val=':( )'
# # swapped_val=str_val.maketrans
# # final=str_val.translate(swapped_val('(',')'))
# # print(final)
# #
# # str_val=str_val.replace('(','temp')
# # str_val=str_val.replace(')','(')
# # str_val=str_val.replace('temp',')')
# # print(str_val)
# #
# # from itertools import permutations
# # items='abcdefg'
# # res=permutations(items)
# #
# # def check_empty(str_value,text):
# #     if (len(str_value)==0):
# #         return 'false'
# #     while(len(str_value)!=0):
# #         index=str_value.find(text)
# #         if(index==(-1)):
# #             return 'false'
# #         str_value=str_value[0:index]+str_value[index+len(text):]
# #     return 'true'
# #
# # str='hehelloll'
# # text='hello'
# # print(check_empty(str,text))
#
# # from collections import Counter
# # def duplicates(input):
# #     col=(Counter(input))
# #     j=-1
# #     for key,val in col.items():
# #         if val >1:
# #             print(key)
# #
# #
# # if __name__=='__main__':
# #     input='hello catty'
# #     duplicates(input)
#
# # from collections import Counter
# # def duplications(input):
# #     col=Counter(input)
# #     for key,val in col.items():
# #         if val>1:
# #             print(key)
# #
# # duplications('tweety')
#
#
# # Python3 program to accept an amount
# # and count number of notes
#
# # Function to count and print
# # currency notes
# # def countCurrency(amount):
# #     notes = [2000, 500, 200, 100,
# #              50, 20, 10, 5, 1]
# #
# #     noteCounter = [0, 0, 0, 0, 0,
# #                    0, 0, 0, 0]
# #
# #     print("Currency Count -> ")
# #
# #     for i, j in zip(notes, noteCounter):
# #         if amount >= i:
# #             j = amount // i
# #             amount = amount - j * i
# #             print(i, " : ", j)
#
#         # Driver code
#
#
# # amount = 1897
# # countCurrency(amount)
# #
# #
# # def Currency(amount):
# #     notes=[2000,500,200,100,50,20,10,5,2,1]
# #     noteCounter=[0,0,0,0,0,0,0,0,0,0]
# #
# #     for i,j in zip(notes,noteCounter):
# #         if amount >= i:
# #             j=amount//i
# #             amount=amount-j*i
# #             print(i,":",j)
# #
# #
# # amount=1843
# # Currency(amount)
#
#
# # def change_files():
# #     file_names=os.listdir(r"D:\Photos\modified")
# #     print(file_names)
# #     os.chdir(r"D:\Photos\modified")
# #     for val in file_names:
# #
# #         tab=val.maketrans('0','0','0')
# #
# #         res=val.translate(tab)
# #         print(res)
# #         os.rename(val,val.translate(tab))
# #
# #     os.chdir(r'C:\Users\Sai Ashwik\PycharmProjects\pythonbasics')
# #
# # change_files()
#
# import turtle
# windows=turtle.Screen()
# windows.bgcolor("powderblue")
# brad=turtle.Turtle()
# brad.shape('turtle')
# brad.color('black')
# brad.forward(100)
# brad.right(90)
# brad.forward(100)
# brad.right(90)
# brad.forward(100)
# brad.right(90)
# brad.forward(100)
# brad.right(90)
# cir=turtle.Turtle()
# cir.circle(100)
# cir.shape('circle')
# cir.color('red')
# windows.exitonclick()

# from twilio.rest import Client
#
#
# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
#
#
# def notify(name):
#
#     account_sid = 'AC08244817520604a66a1c172a508f740b'
#     auth_token = '770a42c4c701a4812093fb0f35fdfc74'
#     client = Client(account_sid, auth_token)
#     if name =="nar":
#         message = client.messages \
#             .create(
#             body='good night',
#             from_='+12038069215',
#             to='+917981718850',
#         )
#     elif name =="vamsi":
#         message = client.messages.create(body='hello good night',
#                                          from_='+12038069215',
#                                          to='+918919434063',
#                                          )
#
#
#
#
#     print(message.sid)
#
#
# name=input("enter name to notify")
# notify(name)
# import urllib.request
#
# text=open("D:\sampletest.txt")
# data=text.read()
# print(data)
# text.close()
# resp=urllib.request.urlopen("http://www.wdylike.appspot.com//?q="+data)
# result=resp.read()
# print(result)
# import webbrowser
# import time
# loop=3
# counter=0
# while(counter<loop):
#     time.sleep(90)
#     webbrowser.open("https://www.youtube.com/watch?v=SkXux-bc5es&list=RDSkXux-bc5es&start_radio=1")
#     counter=counter+1

# N=int(input('enter no of elements'))
# a=[]
# while(N!=0):
#     temp=int(input('enter element'))
#     a.append(temp)
#     N=N-1
#
# def adddd(x,y):
#     return x+y
# import functools
# res=functools.reduce(adddd,a)
# print(res)
#
#
# res=sum([x for x in a])
# print(res)

# from http.server import HTTPServer,BaseHTTPRequestHandler
# class Handler_class(BaseHTTPRequestHandler):
#     def do_task(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain; charset=utf-8')
#         self.end_headers()
#         self.wfile.write((self.path[1:]).encode())
#
#
# if __name__=='__main__':
#     server_address=(' ',8000)
#     http_obj=HTTPServer(server_address,Handler_class)
#     http_obj.serve_forever()

# import requests
# payload={'key1':'val1'}
# headers={'content-type':'text/html'}
# y=requests.get('http://127.0.0.1:8000/faq/',headers=headers,params=payload)
# print(y.url)
# print(y.text)



from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import  parse_qs,urlparse
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        data=self.path[2:]
        self.wfile.write(data.encode())

    def do_POST(self):
        length=int(self.headers.get('content-length',0))
        data=self.rfile.read(length).decode()
        print(data.encode())

        self.wfile.write(data.encode())


if __name__ == '__main__':
    address = ('', 8000)
    http_call = HTTPServer(address, HelloHandler)
    http_call.serve_forever()


# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)
#
# import webbrowser
# webbrowser.open_new("https://www.google.com")

from urllib.parse import urlparse,parse_qs
# import requests
# # from PIL import Image
# # from io import BytesIO
# # param={'key1':'value1','key2':'value2'}
# # r = requests.get('https://www.google.com',params=param)
# # url=r.url
# # print(urlparse(url))
# # print(r.text)
#
# resp=requests.get("https://swapi.co/api/people/1/")
# print(resp.text)
# x=open("D:\Photos\json_data.txt",'w')
# x.write(resp.text)
# x.close()

# import numpy
# val=numpy.random.randint(low=1,high=6,size=10)
# val=val+10
# print(val)