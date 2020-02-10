#This is the list I will create for random inspirational quotes
from random import randint

#I create a class
class inSpire:
    def __init__(self, fortune):
        self.fortune = fortune
    
#This is a list of integers 1-20
theBills = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#Each string has been assigned to a letter a-t
a = str('Dont let yesterday take up too much of today.')
b = str('Dont be afraid of who you are. Embrace it.')
c = str('You learn more from failure than from success.')
d = str('The Way Get Started Is To Quit Talking And Begin Doing.')
e = str('We Generate Fears While We Sit. We Overcome Them By Action.')
f = str('Do What You Can With All You Have, Wherever You Are.')
g = str('Successful entrepreneurs are givers and not takers of positive energy.')
h = str('Opportunities don’t happen, you create them.')
i = str('I have not failed. I’ve just found 10,000 ways that won’t work.')
j = str('No one can make you feel inferior without your consent.')
k = str('Don’t raise your voice, improve your argument.')
l = str('What seems to us as bitter trials are often blessings in disguise.')
m = str('No masterpiece was ever created by a lazy artist.')
n = str('Do one thing every day that scares you.')
o = str('Life is not about finding yourself. Life is about creating yourself.')
p = str('Your problem isn’t the problem. Your reaction is the problem.')
q = str('You can do anything, but not everything.')
r = str('Innovation distinguishes between a leader and a follower.')
s = str('I find that the harder I work, the more luck I seem to have.')
t = str('I find that the harder I work, the more luck I seem to have.')



#I assign the the elements inside of the list to a string
theBills[0] = str(a)
theBills[1] = str(b)
theBills[2] = str(c)
theBills[3] = str(d)
theBills[4] = str(e)
theBills[5] = str(f)
theBills[6] = str(g)
theBills[7] = str(h)
theBills[8] = str(i)
theBills[9] = str(j)
theBills[10] = str(k)
theBills[11] = str(l)
theBills[12] = str(m)
theBills[13] = str(n)
theBills[14] = str(o)
theBills[15] = str(p)
theBills[16] = str(q)
theBills[17] = str(r)
theBills[18] = str(s)
theBills[19] = str(t)

#I import randint from random
#I assign forTune to a random integer between 0 and 20
#I now pass the random integer through theBills to generate random phrase
from random import randint
forTune = randint(0,20)
cOOkie = theBills[forTune]

userName = input('\n Please enter your name:')

welcomeString = ('Welcome back %s!') %userName

print ('\n ' + welcomeString)

quoteOftheDay =('''\n Your quote of the day is:
\n %s''') %(cOOkie)

print(quoteOftheDay)


