# Import pandas as pd
import pandas as pd
import sys
import numpy as np

import matplotlib.pyplot as plt
 
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)
 
def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "g", marker = "o", s = 50)
	
	# estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)
	y_pred = b[0] + b[1]*x
	print(y_pred)
	
	# plotting the regression line
	plt.plot(x, y_pred, color = "r")
	
	# putting labels
	plt.xlabel('mileage')
	plt.ylabel('price')
	
	# function to show plot
	plt.show()

def main() :
	args = sys.argv[1:]
	# args is a list of the command line args
	print(args[0])
	# Import the cars.csv data: cars
	data = pd.read_csv(args[0], index_col=False).sort_values(by=['km'], ascending=False)

	arr1 = data['km']
	arr2 = data['price']
	print(arr1)
	print(arr2)
	b = estimate_coef(arr1, arr2)
	print(b)
	plot_regression_line(arr1, arr2, b)
	

if __name__ == "__main__":
    main()