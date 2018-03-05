from math import sqrt
import copy

class Vector3:
	#num_of_vectors = 0
	def __init__(self,x,y,z):
		if type(x) not in [int,float] or type(y) not in [int,float] or type(z) not in [int,float]:
			raise TypeError('Vector component must be a integer or a float')
		self.x = x
		self.y = y
		self.z = z		
		#Vector3.num_of_vectors +=1

	def norm(self):
		return sqrt(self.x**2+self.y**2+self.z**2)

	def __del__(self):
		#print('Destructed the instance {} from memory location {}'.format(self.__class__.__name__,hex(id(self))))
		#Vector3.num_of_vectors -= 1
		pass
	def __delattr__(self,attr):
		self.attr = 0
		return self
	
	def __str__(self):
		return "{}: {}i+{}j+{}k".format(self.__class__.__name__,self.x,self.y,self.z)
	def __repr__(self):
		return "{} object with values {}i {}j {}k, at memory location: {}".format(self.__class__.__name__ ,self.x,self.y,self.z,hex(id(self)))

	# def __copy__(self):
	# 	return copy.copy(self)
	# def __deepcopy__(self):
	# 	return copy.deepcopy(self)

	def __getitem__(self,key):
		assert isinstance(key,int)
		return [self.x,self.y,self.z][key]
	
	def __setitem__(self,key,value):
		assert isinstance(value,int)
		if key == 0:
			self.x = value
		elif key == 1:
			self.y = value
		elif key == 2:
			self = value
		else:
			raise ValueError('Invalid key')
		return self
	
	def __add__(self,other):
		if type(self) !=  type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		x = self.x+other.x
		y = self.y+other.y
		z = self.z+other.z
		return Vector3(x,y,z)
	def __iadd__(self,other):
		if type(self) !=  type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		x = self.x+other.x
		y = self.y+other.y
		z = self.z+other.z
		return Vector3(x,y,z)
	
	def __sub__(self,other):
		if type(self) !=  type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		x = self.x-other.x
		y = self.y-other.y
		z = self.z-other.z
		return Vector3(x,y,z)
	def __isub__(self,other):
		if type(self) !=  type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		x = self.x-other.x
		y = self.y-other.y
		z = self.z-other.z
		return Vector3(x,y,z)
	
	def __mul__(self,other):
		# Scalar multiplicaiton of one vector with a scalar or two vectors
		if type(self) == type(other):
			x = self.x*other.x
			y = self.y*other.y
			z = self.z*other.z
			return (x+y+z)
		if type(other) not in [int,float]:
			raise TypeError('Invalid type of multiplier :{}'.format(type(other)))
		return Vector3(self.x*other,self.y*other,self.z*other)
	def __imul__(self,num):
		# Multiplies inplace the vector with a scalar only! 
		if type(num) not in [int,float]:
			raise TypeError('Multiplies only a vector with a scalar')
		return Vector3(self.x*num,self.y*num,self.z*num)
	def __rmul__(self,num):
		if type(num) not in [int,float]:
			raise TypeError('Multiplies only a vector with a scalar')
		return Vector3(self.x*num,self.y*num,self.z*num)


	def __truediv__(self,num):
		# Divides the vector with a scalar only! 
		if type(num) not in [int,float]:
			raise TypeError('Invalid type')
		return Vector3(self.x/num,self.y/num,self.z/num)
	def __itruediv__(self,num):
		# Divides inplace the vector with a scalar only! 
		if type(num) not in [int,float]:
			raise TypeError('Invalid type')
		return Vector3(self.x/num,self.y/num,self.z/num)
	def __floordiv__(self,num):
		if type(num) not in [int,float]:
			raise TypeError('Invalid type')
		return Vector3(self.x//num,self.y//num,self.z//num)
	def __ifloordiv__(self,num):
		if type(num) not in [int,float]:
			raise TypeError('Invalid type')
		return Vector3(self.x//num,self.y//num,self.z//num)

	def __pow__(self,num):
		if type(num) not in [int]:
			raise TypeError('Invalid type: power can only be an positive integer')
		if num < 0:
			raise ValueError('Power cannot be a negative number (Because of my insufficient knowledge of algebra)')
		if num % 2 == 0:
			return (self*self)**(num/2)
		return (self*self)**(num//2)*self

	def __lt__(self,other):
		if type(self) !=  type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		return self.norm() < other.norm()
	def __le__(self,other):
		if type(self) !=  type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		return self.norm() <= other.norm() 
	def __gt__(self,other):
		if type(self) != type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		return self.norm() > other.norm()
	def __ge__(self,other):
		if type(self) !=  type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		return self.norm() >= other.norm()
	def __eq__(self,other):
		if type(self) !=  type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		return self.x == other.x and self.y == other.y and self.z == other.z 
	def __ne__(self,other):
		if type(self) !=  type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		return self.x != other.x or self.y != other.y or self.z != other.z 
	def __bool__(self):
		return True if not (0*self==self) else False

	def __neg__(self):
		return Vector3(-self.x,-self.y,-self.z)
	def __pos__(self):
		return self
	def __abs__(self):
		return Vector3(abs(self.x),abs(self.y),abs(self.z))

	def vecMul(self,other):
		# Vectoral multiplication of two 3 dimensinal vectors
		if type(self) != type(other) :
			raise TypeError('Both must a instance of Vector3 class')
		x = self.y*other.z - self.z*other.y
		y = self.z*other.x - self.x*other.z
		z = self.x*other.y - self.y*other.x
		return Vector3(x,y,z)
	def unitVec(self):
		# return the unit vector in the same direction
		return Vector3(self.x/self.norm(),self.y/self.norm(),self.z/self.norm())



class Vector2(Vector3):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.z = 0
	def 


class Vector1(Vector3):
	def __init__(self,x):
		self.x = x
		self.y = 0
		self.z = 0

		






