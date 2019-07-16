dic_fun = {'sigm' : (lambda x: 1/(1 + np.e ** (-x)), lambda x: x * (1 - x)) ,
           'tanH' : (lambda x:(2/(1+np.e **(-2*x)))-1,lambda x: (4*np.e**(-2*x))/((np.e**(-2*x))+1)**2),
           'f_cost' : (lambda Yp, Yr: np.mean((Yp - Yr) **2),lambda Yp, Yr: (Yp -Yr)),
           'perceptron' : (lambda x: x, lambda x: 1) }
