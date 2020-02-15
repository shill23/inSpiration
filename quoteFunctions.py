# This file will used for my functions
from random import randint

# I will create simple function that will welcome the user and present the date
def welcomeUser(uName):
    import datetime
    theDate = datetime.datetime.today().strftime("%B %d, %Y")
    welcomeMessage = 'Welcome %s. \nTodays date is %s.' %(uName,theDate)
    print(welcomeMessage)

# Testing my function
# welcome = welcomeUser('Simone')

# I will create a function that pulls random quote from excel file
import xlrd

def quoteGenerate():
    from random import randint
    loc = ("/Users/simonehill/Desktop/PYTHON FILES/Inspirational Quote of the day/inSpire.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    randomInt = randint(1,20)
    randomCell = sheet.cell_value(randomInt,0)
    print('This is your quote of the day: \n%s' %(randomCell))

# Testing my function
# loc = ("/Users/simonehill/Desktop/PYTHON FILES/Inspirational Quote of the day/inSpire.xlsx")
# greetMe = quoteGenerate(loc)
    
# This is a reference to the location of my excel file
# loc = ("/Users/simonehill/Desktop/PYTHON FILES/Inspirational Quote of the day/inSpire.xlsx")


    

    
    
    
