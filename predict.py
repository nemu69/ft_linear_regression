# Import pandas as pd
import pandas as pd



def main() :
	while True :
		try:
			prompt = int(input("Enter the mileage: "))
			print(prompt)
			
			break
		except ValueError:
			print("This is not a valid number. Try Again !")

main()