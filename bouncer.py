#Bouncer code-along
#spits out text based on age
#handles errors

#ask for age
age = input("How old are you?")
if int != "":
	age = int(age)
	#18-21
	if age > 18 and age < 21:
		print('You can enter but you need a wristband')
	#21+ 
	elif age >= 21:
		print('You can drink')
	#other
	else:
		print('You cant come in, little one')
else:
	print('please enter an age')