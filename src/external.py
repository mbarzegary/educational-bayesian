import sys
import numpy as np

# we expect 6 arguments (the first arg is always the program name)
# the next one is the run number, which is used to name the output files
# the last four args are the passed coefficients of the polynomial
if len(sys.argv) != 6:
    print("Not enough input parameters!")
    quit()

runNumber = sys.argv[1] # used to create the output filename
coefs = [float(arg) for arg in sys.argv[2:6]] # convert args from string to float
coefs.append(0) # we already know that the function pass through (0, 0)

func = np.poly1d(coefs) # create the main polynomial function using the passed args

x = np.linspace(0, 5, 21)
y = func(x) # evaluate the function on the range (0, 5)

f = open("output/result-{0}.txt".format(runNumber), 'w+')

# we write the passed four coefficients to the first line of the output
# it helps us to know which parameters have caused this output
firstLine = "".join([str(item) + " " for item in coefs])
f.write(firstLine + "\n")

# write each point in a separate line
for i in range(len(x)):
    f.write("{0} {1}\n".format(x[i], y[i]))
