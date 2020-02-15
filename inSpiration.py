from quoteFunctions import (welcomeUser,
quoteGenerate)

# I will ask the user to enter their name
# And pass userInput to uName in welcomeUser function
userInput = input('Please enter your name: ')

theuserWelcome = welcomeUser(userInput)

# After the user is greeting by welcome message
# The code will generate a random inspirational message

theInspiration = quoteGenerate()

