# exercise 1
# start = list(range(2000, 3201, 1))
# end = []
#
# for item in start:
#     if item % 5 != 0 and item % 7 ==0:
#         end.append(item)
#
# print(end)

#exercise 2

# factorial = int (input('Please enter en integer. '))
#
# for item in (list(range(1, factorial))) :
#     factorial = factorial * item
#
# print(factorial)

#exercise 3

# start =  int (input('Please enter en integer. '))
# out = {
#
# }
#
# def func(num):
#     num = num
#     square = num*num
#     out.update({num: square})
# for num in range(1, start+1):
#     func(num)
#
# print(out)


#exercise 4
# input_list = list(input('Please input a list ').split(','))
# input_tuple = tuple(input_list)
#
# print(input_tuple, input_list)

#exercise 5
#class Player:
#     def __init__(self, player):
#         self.player = player
#     def getString(self):
#         self.name = input('What is your name? ')
#     def printString(self):
#         print(f'Hello {self.name.upper()}! You are Player {self.player}. ')
#
#
#
# Player1 = Player(1)
# Player1.getString()
# Player1.printString()

#Exercise 6
# from math import sqrt
# qlist=[]
# c=50
# h=30
# def equasion(num):
#     q=int(sqrt(2*c*num/h))
#     qlist.append(q)
#
#
# user_input = (input('Please input numbers ').split(','))
#
# for num in user_input:
#     num = float(num)
#     equasion(num)
#
# print(user_input, qlist)

#Exercise 7
#
# XY = input('enter X,Y   ').split(',')
# X = list(range(0, int(XY[0])))
# Y = list(range(0, int(XY[1])))
# print(X, Y)
#
# Xlist = []
#
# for item in X:
#     Ylist = []
#     for num in Y:
#         thingy = item * num
#         Ylist.append(thingy)
#     Xlist.append(Ylist)
#
# print(Xlist)

#Exercise 8

# words = input('talk to me...  ').split(',')
#
# sorted_words = sorted(words)
# string = ''
# for item in sorted_words:
#     string = string + item + ','
#
# print(sorted_words)
# print(string[:-1])

# lst = input('talk to me ').split(',')
# lst.sort()
# print(",".join(lst))
# print(lst)

#Exercise 9

# lines = []
#
# while True:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else:
#         break
#
# for l in lines:
#     print(l)

#Exercise 10

# text = input('talk to me  ').split(' ')
# txtup = sorted(list(set(text)))
#
#
# print(' '.join(txtup))

#Exercise 11

# test = input('input binary: ').split(',')
# print(test)
# bin_list = []
# for num in test:
#     deci = int(num, 2)
#     if deci % 5 == 0:
#         bin_list.append((bin(deci))[2:])
#
#
# print(bin_list)
# print(",".join(bin_list))


#Exercise 12 I failed this one

# start = input('enter numbers: ').split(',')
#
# lst = []
#
# for i in range(int(start[0]), (int(start[1]))):
#     flag = 1
#     for j in str(i):          # every integer number i is converted into string
#         if int(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
#             flag = 0          # flag becomes zero if any odd digit found
#         elif int(j) == 0:       #added this bit as ord accepts zero as devisable by 2
#             flag = 0
#     if flag == 1:
#         lst.append(str(i))    # i is stored in list as string
#
# print(",".join(lst))


#Exercise 13

# test = input('talk to me... ').replace(' ', '')
# print(test)
# digits = []
# letter = []
# for i in test:
#     try:
#         i = int(i)
#         digits.append(i)
#     except:
#         letter.append(i)
# print(digits)
# print(letter)
# len_let = len(letter)
# len_dig = len(digits)
# print('LETTERS ',len_let)
# print('DIGITS', len_dig)
# Andre solution
# word = input()
# letter,digit = 0,0
#
# for i in word:
#     if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
#         letter+=1
#     if '0'<=i and i<='9':
#         digit+=1
#
# print("LETTERS {0}\nDIGITS {1}".format(letter,digit))

#Exercise 14

# list_up = 0
# list_low = 0
#
# test = input('talk to me... ')
#
# for i in test:
#     if ('a'<=i and i<='z'):
#         list_low+=1
#     elif ('A'<=i and i<='Z'):
#         list_up+=1
#
# print('UPPER CASE ', list_up)
# print('LOWER CASE ', list_low)

#Exercise 15

# num = int(input('talk to me...  '))
#
# output = num*4 + num*30 + num*200 + num*1000
#
# print(output)

#Exercise 16

# start = input('talk to me... ').split(',')
# list = []
# for num in start:
#     if int(num)%2 != 0:
#         list.append(str((int(num)**2)))
#
# print(','.join(list))

#Exercise 17
# deposit = 0
# withdrawl = 0
# try:
#     while True:
#         start = input('talk to me... ')
#         if start[0] == 'D':
#             deposit = deposit + int(start[2:])
#         elif start[0] == 'W':
#             withdrawl = int(start[2:])
#         else:
#             break
# except:
#     balance = deposit - withdrawl
# print('BALANCE ', balance)

#Exercise 18

# import re
#
# pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,12}")
# wordlst = []
# password = input('enter password ').split(',')
# for word in password:
#     a = pattern.fullmatch(word)
#     if a:
#         wordlst.append(word)
# print(','.join(wordlst))
# while True:
#     try:
#         password = input('enter password ')
#         a = pattern.fullmatch(password)
#         print('passwords is ', a.end(), ' characters long ')
#     except:
#         print('Please try again ')
#     else:
#         print('Thank you')
#         break

#Exercise 19
# from operator import itemgetter
#
# people = []
#
# while True:
#         peeps = input('talk to me...  ')
#         if peeps:
#             tmp = tuple(peeps.split(','))
#             people.append(tmp)
#         else:
#             break
#
#
#
# # a = (sorted(people, key=itemgetter(0, 1, 2)))
# # the above works, but the below is simpler
# # print(a)
#think it didn't work the first time as I was trying to print the wrong thing
#was trying to make a new variable or put a print round the sort,
#but the sort returns none, just changes the orginal file
# #people.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))
# people.sort(key= lambda x:x[0])
# print(people)

#Exercise 21
# from math import sqrt
# up = 0
# down = 0
# left = 0
# right = 0
#
# while True:
#     step = input('How many steps? ')
#     if 'U' in step:
#         up = up + int(step[3])
#     elif 'D' in step:
#         down = down + int(step[5])
#     elif 'L' in step:
#         left = left + int(step[5])
#     elif 'R' in step:
#         right = right + int(step[6])
#     else:
#         break
# print(up, down, left, right)
# dis = int(sqrt(((up - down)**2) + ((left - right)**2)))
# print(dis)


#Exercise 22

# sentence = input('talk to me...  ').split(' ')
#
# sentence.sort()
# for word in sentence:
#     print(word,':', sentence.count(word))
# #print(sentence)

#Exercise 23

# def square_num(num):
#      return num**2
#
#
# innum = int(input('talk to me... '))
# square = square_num(innum)
#
#
# print(square)

#Exercise 24

#print(abs.__doc__)

#Exercise 25

# class Car:
#     name = "Car"
#
#     def __init__(self,name = None):
#         self.name = name
#
# honda=Car("Honda")
# print("%s name is %s"%(Car.name,honda.name))

# toyota=Car()
# toyota.name="Toyota"
# print("%s name is %s"%(Car.name,toyota.name))

#Exercise 26

# def func(num1, num2):
#     return  num1 + num2
#
#
# print(func(3,5))

#Exercise 27

# def func(num):
#     print(str(num))
#
# func(5)

#Exercise 28

# from word2number import w2n
#
# def convert(num1, num2):
#     num1 = w2n.word_to_num(num1)
#     num2 = w2n.word_to_num(num2)
#     answer = int(num1) + int(num2)
#     print(answer)
#
# convert('five', 'six')

#Exercise 29

# def func(str1, str2):
#     print(str1 + str2)
#
# func('mad', 'cat')

#Exercise 30

# def func(str1, str2):
#     if len(str1) > len(str2):
#         print(str1)
#     elif len(str1) < len(str2):
#         print(str2)
#     else:
#         print(str1)
#         print(str2)
#
# func('boo', 'ha')
# func('do', 'dah')
# func('yep', 'pie')

# Exercise 31

# def printdict(num1, num2):
#     newdict = {num: num**2 for num in range(num1, (num2 + 1))}
#     print(newdict)
#
#
#
# printdict(1, 20)

#Exercise 32

# def printdict(num1, num2):
#     newdict = {num: num**2 for num in range(num1, (num2 + 1))}
#     print(newdict.keys())
#
#
# printdict(1, 20)

#Exercise 33

# def printlist(num1, num2):
#     newlist = [num**2 for num in range(num1, (num2 + 1))]
#     print(newlist)
#
# printlist(1, 20)

#Exercise 34

# def printlist(num1, num2):
#     newlist = [num**2 for num in range(num1, (num2 + 1))]
#     print(newlist[0:5])
#
# printlist(1, 20)

#Exercise 35

# def printlist(num1, num2):
#     newlist = [num**2 for num in range(num1, (num2 + 1))]
#     print(newlist[num2 - 5:])
#
# printlist(1, 20)

#Exercise 36

# def printlist(num1, num2):
#     newlist = [num**2 for num in range(num1, (num2 + 1))]
#     print(newlist[5:])
#
# printlist(1, 20)

#Exercise 37

# def printtuple(num1, num2):
#     newlist = [num**2 for num in range(num1, (num2 + 1))]
#     newtuple = tuple(newlist)
#     print(newtuple)
#
# printtuple(1, 20)

#Exercise 38

# newtuple = (1,2,3,4,5,6,7,8,9,10)
#
# print(newtuple[:5], end = ' ')
# print(newtuple[5:])
#
# tpl = (1,2,3,4,5,6,7,8,9,10)
#
# for i in range(0,5):
#     print(tpl[i],end = ' ')
# print()
# for i in range(5,10):
#     print(tpl[i],end = ' ')

#Exercise 39

# newtuple = (1,2,3,4,5,6,7,8,9,10)
# tmp = []
# for num in newtuple:
#     if num%2 == 0:
#         tmp.append(num)
#
# print(tuple(tmp))

#Exercise 40

# tmp = input('talk to me... ')
# tmp = tmp.upper()
#
# if tmp == 'YES':
#     print('Yes')
# else:
#     print('No')

#Exercise 41

# newlist = [1,2,3,4,5,6,7,8,9,10]
#
# print(list(map(lambda x: x**2, newlist)))

#Exercise 42

#newlist = [1,2,3,4,5,6,7,8,9,10]

#print(list(map(lambda x: x**2, (filter(lambda x: x%2 == 0, newlist)))))

#Exercise 43

#print(list(filter(lambda x: x%2 == 0, range(1,21))))

#Exercise 44

#print(list(map(lambda x: x**2,range(1,21))))

#Exercise 45

# class American:
#
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
#     def printNationality(self):
#         print(f'{self.name} is a {self.age} year old American')
#
# dude = American('Fred', 24)
#
# dude.printNationality()
# print((dude.name))


#Exercise 47

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 22*((self.radius)**2)/7
#
# plate = Circle(5)
#
# print(plate.area())
# print(plate.radius)

#Exercise 48

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# oblong = Rectangle(4, 5)
#
# print (oblong.area())

#Exercise 49

# class Shape:
#     def __init__(self, a=0):
#         self.area = a
#
#
#     def p_area(self):
#         print(0)
#
#
# class Square(Shape):
#     def __init__(self, l=0):
#         Shape.__init__(self)
#         self.length = l
#         self.area = (self.length)**2
#
#     def p_area(self):
#         print(self.area)
#
# rhomus = Square(3)
# test = Shape()
# rhomus.p_area()
# test.p_area()

#Exercise 51

# try:
#     print(5/0)
# except:
#     print('Don\'t be a knob')

#Exercise 52

# class PlumError(Exception):
#     def __init__(self, message):
#         self.message = message
#
# num = input('talk to me... ')
#
# try:
#     if int(num) == 10:
#         print('fine')
#     else:
#         raise PlumError('Don\'t be a plum!!!')
# except PlumError as P:
#     print(P.message)

#Exercise 53
# import re
# email = input('What is your email address?  ')
#
# test = re.search('@', email)
#
# print(email[:test.start()])
#
# email = "john@google.com"
# email = email.split('@')
# print(email[0])

#Exercise 54

# import re
# email = input('What is your email address?  ')
#
# teststart = re.search('@', email)
# teststop = re.search('\.', email)
#
# #print(teststart.start())
# #print(teststop.start())
# print(email[teststart.start()+1:teststop.start()])
#
# pattern = "@([a-zA-Z]+)\."
# com = re.findall(pattern, email)
# print(com)
#
# pattern = "\w+@(\w+).com"
# ans = re.findall(pattern,email)
# print(ans)

#Exercise 55

# numlst = []
#
# stuff = input('talk to me...  ').split(' ')
#
# for num in stuff:
#     if num.isdigit():
#         numlst.append(num)
#
# print(numlst)

#Exercise 59

# num = int(input('talk to me... '))
# top = list(range(1, num+1))
# #print(top)
# answer = 0
# for item in top:
#     answer = answer + (item/(item+1))
# print(answer)

#Exercise 60
#I didn't get this at first, but it seems to have made a loop
#by making the function refer to itself?
# def f(n):
#     if n == 0:
#         return 0
#     return f(n-1) + 100

# n = int(input())
# print(f(n))

#Exercise 61

# num = int(input('give me a number... '))
#
#
# a=0
# b=1
# fib=0
# for num in range(2, num+1):
#     fib=a+b
#     a=b
#     b=fib
# print(fib)
#
# def f(n):
#     if n < 2:
#         return n
#     return f(n-1) + f(n-2)
#
# print(f(num))

#Exercise 62

# num = int(input('give me a number... '))
#
# fiblist = [0,1]
#
# a=0
# b=1
# fib=0
# for num in range(2, num+1):
#     fib=a+b
#     fiblist.append(fib)
#     a=b
#     b=fib
#
# print(fiblist)

#Exercise 63

# num = int(input('give me a number... '))
#
# for i in (range(0, num+1, 2)):
#     if i < num-1:
#      print(i, end = ',')
#     else:
#         print(i)

#Exercise 64

# num = int(input('give me a number... '))
#
# for i in (range(0, num+1, 5)):
#     if i < num-1 and i % 7 == 0:
#         print(i, end=',')
#     elif i > num-1 and i % 7 == 0:
#         print(i)


#Exercise 65

# lst = [2,4,6,8]
#
# for item in lst:
#     assert item%2 == 0

#Exersice 66

# task = eval(input('talk to me... '))
# print(task)

#Exercise 67


# lst = input('input list  ').split(',')
# target = input('input target  ')
# print(lst)
# a = sorted(lst)
# print(a)
# print(target)
# # nlst = []
# # for item in a:
# #     if item != target:
# #         nlst.append(item)
# #     elif item == target:
# #         nlst.append(item)
# #         print((len(nlst))-1)
# #         break
# top = (len(lst))-1
# bot = 0
# mid = int((top-bot+1)/2)
# def bin_search(a, target, top, bot, mid):
#     lstidx = mid
#     # print(lstidx, a[lstidx])
#     # print('bot in is ', bot)
#     # print('mid in is ', mid)
#     # print('top in is ', top)
#     if target > a[lstidx]:
#         #print('true')
#         bot = mid
#         #return bot
#         mid = bot + int((top - bot)/2) + 1
#         #return mid
#         #print('bot out is ', bot)
#         #print('mid out is ', mid)
#         #print('top out is ', top)
#         bin_search(a, target, top, bot, mid)
#     elif a[lstidx] > target:
#         top = mid
#         mid = bot + int((top - bot)/2)
#         bin_search(a, target, top, bot, mid)
#     else:
#         print(lstidx)
#
#
#
# bin_search(a, target, top, bot, mid)

#Exercise 68

# import random
#
# print(random.uniform(10, 100))

#Exercise 70

# import random
# lst = list(range(0, 12, 2))
# print(lst)
# print(random.choice(lst))

#Exercise 71
import random
# lst = list(range(35, 151, 35))
# print(lst)
#
#
# print(random.choice(lst))

#Exercise 72

# import random
#
# lst=random.sample(range(100,201), 5)
# print(lst)

#Exercise 73
# import random
# lst=random.sample(range(100,201,2), 5)
# print(lst)

#Exercise 74
# import random
# print(random.sample(range(35,10001,35),5))

#Exercise 75

#print(random.randrange(7,16))

#Exercise 76
# import sys
# import zlib
# string = 'hello world! hello word! hello world!'
# print(sys.getsizeof(string))
# a = bytes(string, 'utf-8')
# print(sys.getsizeof(a))
# print(a)
# b = zlib.compress(a)
# print(b)
# print(sys.getsizeof(b))
# c = zlib.decompress(b)
# print(sys.getsizeof(c))
# print(c)
# d=str(c)
# print(sys.getsizeof(d))
# print(d)

#Exercise 77

# import time
#
# def timechk():
#     start = time.time()
#     for i in range(10000):
#         x = 1 + 1
#     stop = time.time()
#     print((stop-start))
#
# timechk()

#Exercise 78
from random import shuffle
# a = [3,6,7,8]
# random.shuffle(a)
# print(a)

#Exercise 79

# sub = ['I', 'You']
# verb = ['Play', 'Love']
# thing = ['Hockey', 'Football']
#
#
# for i in sub:
#     for j in verb:
#         for x in thing:
#             sentence = i + j + x
#             print(sentence)
#             sentence = []
# subjects=["I", "You"]
# verbs=["Play", "Love"]
# objects=["Hockey","Football"]
#
# for sub in subjects:
#     for verb in verbs:
#         for obj in objects:
#             print("{} {} {}".format(sub,verb,obj))
#

#Exercise 80

#print(list(filter(lambda x: x%2 !=0, [5,6,77,45,22,12,24])))

#Exercise 82

# lst = [12,24,35,70,88,120,155,200,201]
# print(lst[1:6:2] + lst[7:])

#Exercise 83

# lst = [12,24,35,70,88,120,155,200,201]
# print(lst[0:2]+lst[5:])
# print([i for i in lst if lst.index(i) not in range(2,5)])

#Exercise 84

# from numpy import zeros
#
# x = zeros((3,5,8), dtype=int)
# print(x)
#
# y = {}
#
# for i in range(3):
#     for j in range(5):
#         for k in range(8):
#             y[i,j,k] = 0
#
# print(y)
# #authors solution
# array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
# print(array)
#
#Exercise 85
# lst = [12,24,35,70,88,120,155]
# index = [0,4,5]
# newlst = []
# for j,i in enumerate(lst):
#     if j not in index:
#         newlst.append(i)
#
# print(newlst)

#Exercise 86

# lst = [12,24,35,70,24,88,120,155,24]
# while 24 in lst:
#     lst.remove(24)
# print(lst)

#Exercise 87

# lst1 = [1,2,3,6,78,35,55]
# lst2 = [12,24,35,24,88,120,155]
# #lst3 = set(lst1).intersection(set(lst2))
# lst3 = set(lst2) & set(lst1)
# print(lst3)

#Exercise 88

# lst = [12,24,35,24,88,120,155,88,120,155]
#
# for item in lst:
#     if lst.count(item) > 1:
#         lst.remove(item)
#
# print(lst)

#Exercise 89

# class Person():
#     def getGender(self):
#         print('Unknown')
#
# class Male(Person):
#     def getGender(self):
#         print('Male')
#
# class Female(Person):
#     def getGender(self):
#         print('Female')

#Exercise 90

# string = input('Talk to me... ')
# chk = {}
#
# for char in string:
#     chk.update({char:string.count(char)})
#
# #print(chk)
# for x,y in chk.items():
#     print(f'{x},{y}')

#Exercise 91

# string = input('talk to me... ')
# print(string[::-1])

#Exercise 92

# string = input('talk to me... ')
# print(string[::2])

#Exercise 93

# lst = [1,2,3]
#
# from itertools import permutations
#
# print(list(permutations(lst)))

#Exercise 94

# total = 1
# rngrab = {}
#
# for item in range(1,35):
#     rngrab.update({item:35-item})
#
# for numr,numc in rngrab.items():
#     if total != 94:
#         rabbits = int(numr)
#         chickens = int(numc)
#         total = (2*chickens)+(4*rabbits)
#     else:
#         print('chickens are: ',chickens,' ,', 'rabbits are: ',rabbits)
#         break

#Exercise 95

# scores = input('talk to me... ').split(' ')
# for item in scores:
#     if scores.count(item) > 1:
#         scores.remove(item)
#
# scores.sort()
#
# print(scores[-2])

#Exercise 96

# string = input('talk to me... ')
# length = input('how long? ')
#
# while len(string) > 0:
#     print(string[:4])
#     string = string[4:]

#Exercise 97
import string

# num = int(input('talk to me... '))
# alph = list(string.ascii_lowercase[:num])[::-1]
# num_range = list(range(num))
# num_rev = num_range[::-1]
# index = num_range + num_rev[1::]
# jindex = (list(range(num*2-1)))
# print(index)
# # print(alph)
# # print(jindex)
# for i in index:
#     pattern = ''
#     for j in jindex:
#         if j % 2 != 0:
#             pattern = pattern + '-'
#         else:
#             x = int(j / 2)
#             if i >= x >= 0:
#                 pattern = pattern + alph[x]
#             else:
#                 pattern = pattern + '-'
#     patternleft = pattern[1::]
#     rangoli = patternleft[::-1] + pattern
#     #print(pattern)
#     #print(patternleft)
#     print(rangoli)

#import string
# def print_rangoli(size):
#     n = size
#     alph = string.ascii_lowercase
#     width = 4 * n - 3
#
#     ans = []
#     for i in range(n):
#         left = '-'.join(alph[n - i - 1:n])
#         mid = left[-1:0:-1] + left
#         final = mid.center(width, '-')
#         ans.append(final)
#
#     if len(ans) > 1:
#         for i in ans[n - 2::-1]:
#             ans.append(i)
#     ans = '\n'.join(ans)
#     print(ans)
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


#Exercise 98
# import datetime
#
# date = input('talk to me... ').split(' ')
# #print(date)
# year = int(date[2])
# month = int(date[0])
# day = int(date[1])
# x = datetime.datetime(year, month, day)
# print((x.strftime('%A')).upper())
#
# import calendar
#
# month, day, year = map(int, date)
#
# dayId = calendar.weekday(year, month, day)
# print(calendar.day_name[dayId].upper())

#Exercise 99

# ln_m = int(input('input len M '))
# lst_m = input('input list M ').split(' ')
# ln_n = int(input('input len N '))
# lst_n = input('input list N ').split(' ')
#
# lst_symdif = []
#
# # for m in lst_m:
# #     if m not in lst_n:
# #         lst_symdif.append(int(m))
# #
# # for n in lst_n:
# #     if n not in lst_m:
# #         lst_symdif.append(int(n))
#
# lst_symdif.sort()
#
# for i in lst_symdif:
#     print(i)

#Exercise 101
# from operator import itemgetter
# string = input('talk to me... ')
#
# string_dict = {}
#
# for item in string:
#     entry = string.count(item)
#     string_dict.update( {item:entry})
#
# print(string_dict)
#
# for key, value in sorted(string_dict.items(), key = itemgetter(1), reverse = True):
#     print(key, value)

#Exercise 102

# string = input('talk to me... ')
#
# dig = 0
# let = 0
#
# for item in string:
#     if item.isnumeric():
#         dig = dig+1
#     else:
#         let = let+1
#
# print('Digit - ', dig)
# print('Letter - ', let)

#Exercise 103

# N = int(input('talk to me... '))
#
# total = 0
#
# for num in range(1,N+1):
#     total = total + num
#
# print(total)
#
# def rec(n):
#     if n == 0:
#         return n
#     return rec(n-1) + n
#
#
# n = N
# sum = rec(n)
# print(sum)

a = 0
b = a ** 0
if b < a + 1:
 c = 1
elif b == 1:
 c = 2
else:
 c = 3
print(a + b + c)
print(b)