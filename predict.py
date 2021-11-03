# Import pandas as pd
import pandas as pd

theta0 = 7990.866013397061
theta1 = -4610.2051096833275
data = "data.csv"

def normalize(x, init):
    return (x - min(init)) / (max(init) - min(init))

def main() :
	set = pd.read_csv(data, index_col=False)

	X = set['km']
	Y = set['price']

	# check if data is empty 
	if len(X) == 0 or len(Y) == 0:
		print("No data to process")
		return
	
	# chck is dta has a string
	if isinstance(X[0], str) or isinstance(Y[0], str):
		print("Data must be numeric")
		return

	# check if an data is not a number or is negative
	if min(X) < 0 or min(Y) < 0:
		print("Invalid data")
		return

	while True :
		try:
			prompt = int(input("Enter the mileage or negative to exit : "))
			if prompt < 0 :
				print("Exit")
				break
				
			else :
				# estimateP rice(mileage) = θ0 + (θ1 ∗ mileage)
				print(int(theta0 + (theta1 * normalize(prompt, X))))
			

		except ValueError:
			print("This is not a valid number. Try Again !")

main()