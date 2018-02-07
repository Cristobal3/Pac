
#Problem 1
name = input('What is your name? ')
if name:
	print('Hello',name)
else:
	print("Please input your name")

#Problem 2
name = input('WHAT IS YOUR NAME? ')
if name:
	print('HELLO',name)
	print('YOUR NAME HAS ', len(name),' LETTERS IN IT! AWESOME!')
else:
	print("Please input your name")

#Problem 3
print('___(name)___\'s favorite subject in school is ___(subject)___.')
name = input('What is the name? ')
subject = input('What is the subject? ')
print(name, '\s favorite subject in school is ', subject,'.')

#Problem 4
day = int(input('Day (0-6)? '))
day_of_the_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
print(day_of_the_week[day])

#Problem 5
day = int(input('Day (0-6)? '))
day_of_the_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
if day_of_the_week.index(day) == 0 or day_of_the_week.index(day) == 6:
	print('Sleep in')
else:
	print('Go to work')

#Problem 6
f = int(input('Temperature in C?'))
c = f*1.8 + 32
print(f,' F')

#Problem 7
bill = int(input('What is the total bill? '))
serv = input("Level of service? [Please specify 'good', 'fair', 'bad'] ")
level = ['good','fair','bad']
perc = [.2,.15,.1]
x = level.index(serv) 
tip = bill*perc[x]
total = tip + bill
print('Tip amount: $',"{:.2f}".format(tip))
print('Total amount: $',"{:.2f}".format(total))
	
#Problem 8
bill = int(input('What is the total bill? '))
serv = input("Level of service? [Please specify 'good', 'fair', 'bad'] ")
split = int(input('Split how many ways? '))
level = ['good','fair','bad']
perc = [.2,.15,.1]
x = level.index(serv) 
tip = bill*perc[x]
total = tip + bill
app = total/split
print('Tip amount: $',"{:.2f}".format(tip))
print('Total amount: $',"{:.2f}".format(total))
print('Tip amount: $',"{:.2f}".format(app))

#Problem 9
cnt = 1
dum = 10*[0]
for l in dum:
	print(cnt)
	cnt +=1

#Problem 10
coins = 0
while True:
	print('You have ',coins,' coins.')
	que = input("Do you want another coin? [Please answer 'yes' or 'no'")
	coins += 1
	if que == 'no':
		print('Bye')
		break


