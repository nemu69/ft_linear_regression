import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 

class Linear_Regression:
	def __init__(self, X, Y):
		self.X = X
		self.Y = Y
		self.b = [0, 0]
	  
	def update_coeffs(self, learning_rate):
		Y_pred = self.predict()
		Y = self.Y
		m = len(Y)
		self.b[0] = self.b[0] - (learning_rate * ((1/m) * 
								  np.sum(Y_pred - Y)))
  
		self.b[1] = self.b[1] - (learning_rate * ((1/m) * 
								  np.sum((Y_pred - Y) * self.X)))
		return self.b
  
	def predict(self, X=[]):
		Y_pred = np.array([])
		if not X: X = self.X
		b = self.b
		for x in X:
			Y_pred = np.append(Y_pred, b[0] + (b[1] * x))
  
		return Y_pred
	  
	def get_current_accuracy(self, Y_pred):
		p, e = Y_pred, self.Y
		n = len(Y_pred)
		return 1-sum(
			[
				abs(p[i]-e[i])/e[i]
				for i in range(n)
				if e[i] != 0]
		)
  
	def compute_cost(self, Y_pred):
		m = len(self.Y)
		J = (1 / 2*m) * (np.sum(Y_pred - self.Y)**2)
		return J
  
	def plot_best_fit(self, Y_pred, fig):
				plt.figure(fig)
				plt.scatter(self.X, self.Y, color='b')
				plt.plot(self.X, Y_pred, color='g')
				plt.show()

	def precision(self):
		Y = self.Y
		y_pred = self.predict()
		u = ((Y - y_pred)**2).sum()
		v = ((Y - Y.mean())**2).sum()
		return 1 - u/v
  

def normalize(x):
	return (x - min(x)) / (max(x) - min(x))

	


def main() :
	if len(sys.argv) != 2:
		print("Usage: python main.py <csv_file>")
		exit(1)
	args = sys.argv[1:]

	# DataSet
	data = pd.read_csv(args[0], index_col=False)

	X = data['km']
	Y = data['price']

	# check if data is empty 
	if len(X) == 0 or len(Y) == 0:
		print("No data to process")
		exit(1)
	
	# chck is dta has a string
	if isinstance(X[0], str) or isinstance(Y[0], str):
		print("Data must be numeric")
		exit(1)

	# check if an data is not a number or is negative
	if min(X) < 0 or min(Y) < 0:
		print("Invalid data")
		exit(1)

	# Stabilize value
	X = normalize(X)

	# Building the model
	print("X :", X)
	print("Y :", Y)
	regressor = Linear_Regression(X, Y)
  
	iterations = 0
	steps = 1000
	learning_rate = 0.1
	costs = []
	  
	#original best-fit line
	Y_pred = regressor.predict()
	regressor.plot_best_fit(Y_pred, 'Initial Best Fit Line')
	print("Loading...")
	while 1 :
		Y_pred = regressor.predict()
		cost = regressor.compute_cost(Y_pred)
		costs.append(cost)
		b = regressor.update_coeffs(learning_rate)

		iterations += 1
		if steps - iterations == 0:
			print("Finish !")
			print(iterations, "epochs elapsed and coefficient of determination  ", regressor.precision())
			break
	

	regressor.plot_best_fit(Y_pred, 'Final Best Fit Line')

	with open("predict.py", "r") as in_file:
		buf = in_file.readlines()

	with open("predict.py", "w") as out_file:
		for line in buf:
			if line.find("theta0 =") != -1:
				line = "theta0 = " + str(b[0]) + "\n"
			if line.find("theta1 =") != -1:
				line = "theta1 = " + str(b[1]) + "\n"
			if line.find("data =") != -1:
				line = "data = \"" + str(args[0]) + "\"\n"
			out_file.write(line)
	
	# Plot to verify cost fuction decreases
	plt.figure('Precision')
	plt.plot(range(iterations), costs, color='b')
	plt.show()

if __name__ == "__main__":
	main()