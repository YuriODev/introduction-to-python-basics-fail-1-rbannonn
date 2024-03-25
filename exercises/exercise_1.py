# Exercise 1
# Your solution comes here

fiveDigit = int(input('Enter a five digit number: '))
firstDigit = (fiveDigit //10000) + ((fiveDigit//100)%10) + (fiveDigit%10)
secondDigit = ((fiveDigit//1000)%10) + ((fiveDigit//10)%10)
finalDigit = (firstDigit*10) + secondDigit
print(finalDigit)