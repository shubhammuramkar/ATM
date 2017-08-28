print("Welcome! TO The Branch ATM of SBI Bank")
chances = 4
restart = ('Y')
balanc = 78.54
balance = int(balanc)

print("Enter your card!")
print("Card is inserted successfully")
while chances>0:

	pin = int(input("Enter your pin : "))
	if pin == 1234:
		while restart != ('NO','N','no','n'):
			print("1. Balance Info.")
			print("2. Withdrawl an amount")
			print("3. Depositing an amount")
			print("4. Return your card")
			option = int(input("Select your option : "))

			if option == 1:
				print("Your Balance is :",balance)
				restart = str(input("Do you want to go back : "))
				if restart in ('NO','N','no','n'):
					print('Thankyou')
					exit()
				else :
					restart = ('Y')

			elif option == 2:
				amount = int(input("Withdrawal Amount : "))
				if (amount < balance):
					balance = float(balance - amount)
					print("Remaing Amount is : %.2f" %(balance))
					restart = str(input("Do you want to go back : "))					
					if restart in ('NO','N','no','n'):
						print('Thankyou')
						exit()
					else :
						restart = ('Y')	
				else :
					print("Don't have enough balance to withdrawl : ", balance)	
					restart = str(input("Do you want to go back : "))					
					if restart in ('NO','N','no','n'):
						print('Thankyou')
						exit()
					else :
						restart = ('Y')	

			elif option == 3:
				amount = int(input("Depositing Amount : "))
				balance = float(balance + amount)
				print("New Balance is : %.2f" %(balance))
				restart = str(input("Do you want to go back : "))					
				if restart in ('NO','N','no','n'):
					print('Thankyou')
					exit()
				else :
					restart = ('Y')	

			elif option == 4:
				print('Your have logout!')
				print('Collect your card!     Thankyou')
				exit()

	elif pin != (1234):
		print('Invalid pin! Try Again')
		chances -= 1

	if chances == 0:
		print("Sorry! No more trails left")
		break