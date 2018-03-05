from matplotlib import pyplot as plt
import numpy as np
from math import sqrt, floor

class Polynomial(): 
        def __init__(self,coefficients): 
            if type(coefficients) not in [list]:
                raise TypeError('Coefficients must be an array containing  coeeficients of the function')
            self.coefficients = coefficients

        def __str__(self):
            return '{} object with coefficients {}'.format(self.__class__.__name__,self.coefficients)
        def __repr__(self):
            return '{} object with coefficients {}'.format(self.__class__.__name__,self.coefficients)

        def __add__(self,other):
            if type(other) not in [int,float,Polynomial]:
                raise TypeError('Invalid type')
            if type(other) == Polynomial:
                if len(self.coefficients) >= len(other.coefficients):
                    lst1 = self.coefficients[::-1]
                    lst2 = other.coefficients[::-1]
                    for i in range(len(lst2)):
                        lst1[i] += lst2[i]
                    return Polynomial(lst1[::-1])
                else:
                    lst1 = self.coefficients[::-1]
                    lst2 = other.coefficients[::-1]
                    for i in range(len(lst1)):
                        lst2[i] += lst1[i]
                    return Polynomial(lst2[::-1])
            else:
                self.coefficients[len(self.coefficients)-1] += other
                return Polynomial(self.coefficients)
        
        def __radd__(self,other):
            if type(other) not in [int,float]:
                raise TypeError('Invalid type')
            self.coefficients[len(self.coefficients)-1] += other
            return Polynomial(self.coefficients)

        def __iadd__(self,other):
            if type(other) not in [int,float,Polynomial]:
                raise TypeError('Invalid type')
            if type(other) == Polynomial:
                if len(self.coefficients) >= len(other.coefficients):
                    lst1 = self.coefficients[::-1]
                    lst2 = other.coefficients[::-1]
                    for i in range(len(lst2)):
                        lst1[i] += lst2[i]
                    return Polynomial(lst1[::-1])
                else:
                    lst1 = self.coefficients[::-1]
                    lst2 = other.coefficients[::-1]
                    for i in range(len(lst1)):
                        lst2[i] += lst1[i]
                    return Polynomial(lst2[::-1])
            else:
                self.coefficients[len(self.coefficients)-1] += other
                return Polynomial(self.coefficients)
            
        def __sub__(self,other):
            if type(other) not in [int,float,Polynomial]:
                raise TypeError('Invalid type')
            if type(other) == Polynomial:
                if len(self.coefficients) >= len(other.coefficients):
                    lst1 = self.coefficients[::-1]
                    lst2 = other.coefficients[::-1]
                    for i in range(len(lst2)):
                        lst1[i] -= lst2[i]
                    return Polynomial(lst1[::-1])
                else:
                    lst1 = self.coefficients[::-1]
                    lst2 = other.coefficients[::-1]
                    for i in range(len(lst1)):
                        lst2[i] -= lst1[i]
                    return Polynomial(lst2[::-1])
            else:
                self.coefficients[len(self.coefficients)-1] -= other
                return Polynomial(self.coefficients)
        def __rsub__(self,num):
            if type(num) not in [int,float]:
                raise TypeError('Invalid type: {}'.format(type(num)))
            self.coefficients[len(self.coefficients)-1] -= num
            return Polynomial(self.coefficients)
        def __isub__(self,other):
            if type(other) not in [int,float,Polynomial]:
                raise TypeError('Invalid type')
            if type(other) == Polynomial:
                if len(self.coefficients) >= len(other.coefficients):
                    lst1 = self.coefficients[::-1]
                    lst2 = other.coefficients[::-1]
                    for i in range(len(lst2)):
                        lst1[i] -= lst2[i]
                    return Polynomial(lst1[::-1])
                else:
                    lst1 = self.coefficients[::-1]
                    lst2 = other.coefficients[::-1]
                    for i in range(len(lst1)):
                        lst2[i] -= lst1[i]
                    return Polynomial(lst2[::-1])
            else:
                self.coefficients[len(self.coefficients)-1] -= other
                return Polynomial(self.coefficients)


        def __mul__(self,other):
            if type(other) in [int,float]:
                return Polynomial([other*num for num in self.coefficients])
            cache = {}        
            if len(self.coefficients) >= len(other.coefficients):
                c1 = self.coefficients; c2 = other.coefficients
            else:
                c2 = self.coefficients; c1 = other.coefficients
            for i in range(len(c1)):
                for n in range(len(c2)):
                    p = (len(c2)-1-n)+(len(c1)-1-i)
                    if p not in cache:
                        cache[p] = c1[i]*c2[n]
                    else:
                        cache[p] += c1[i]*c2[n]
            return Polynomial([val for val in cache.values()])
        def __rmul__(self,num):
            if type(num) not in [int,float]:
                raise TypeError('Invalid type')
            return Polynomial([num*i for i in self.coefficients])
        def __imul__(self,other):
            if type(other) in [int,float]:
                return Polynomial([other*num for num in self.coefficients])
            cache = {}        
            if len(self.coefficients) >= len(other.coefficients):
                c1 = self.coefficients; c2 = other.coefficients
            else:
                c2 = self.coefficients; c1 = other.coefficients
                for i in range(len(c1)):
                    for n in range(len(c2)):
                        p = (len(c2)-1-n)+(len(c1)-1-i)
                        if p not in cache:
                            cache[p] = c1[i]*c2[n]
                        else:
                            cache[p] += c1[i]*c2[n]
            return Polynomial([val for val in cache.values()])
        def __pow__(self,num):
            if type(num) not in [int]:
                raise TypeError('Power must be an integer')
            if num == 1:
                return self
            return (self*self)**(num//2) if num % 2 == 0 else (self*self)**(num//2)*self


        def __neg__(self):
            return Polynomial([-i for i in self.coefficients])
        def __abs__(self):
            return Polynomial([abs(i) for i in self.coefficients])

        def __lt__(self,other):
            if type(self) != type(other):
                raise TypeError('Both must be a Polynomial')
            return len(self.coefficients) < len(other.coefficients)
        def __le__(self,other):
            if type(self) != type(other):
                raise TypeError('Both must be a Polynomial')
            return len(self.coefficients) <= len(other.coefficients)
        def __gt__(self,other):
            if type(self) != type(other):
                raise TypeError('Both must be a Polynomial')
            return len(self.coefficients) > len(other.coefficients)
        def __ge__(self,other):
            if type(self) != type(other):
                raise TypeError('Both must be a Polynomial')
            return len(self.coefficients) >= len(other.coefficients)
        def __eq__(self,other):
            return self.coefficients == other.coefficients
        def __ne__(self,other):
            return self.coefficients != other.coefficients
        def __bool__(self):
            return self == 0*self

        
        def Eval(self,x):
            p = len(self.coefficients)
            y = [self.coefficients[i]*pow(x,p-1-i) for i in range(p)]
            return sum(y)

        def derivative(self):
            p = len(self.coefficients)
            y = [self.coefficients[i]*(p-1-i) for i in range(p)]
            return Polynomial(y[0:])

        def integral(self):
            p = len(self.coefficients)
            y = [self.coefficients[p-1-i]/(i+1) for i in range(p)]
            y = [0] + y
            return Polynomial(y[::-1])
        
        def simple_plot(self):
            x = np.linspace(0,10,100)
            y = [self.Eval(xi) for xi in x]
            plt.plot(x,y)
            plt.show()
