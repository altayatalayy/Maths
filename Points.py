from Vectors import Vector3,Vector2
from math import sqrt

class Point3:
	def __init__(self,x,y,z):
		if type(x) not in [int,float] or type(y) not in [int,float] or type(z) not in [int,float]:
			raise TypeError('Coordinates must be integers')
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return '{}: {}x,{}y,{}z'.format(self.__class__.__name__,self.x,self.y,self.z)
	def __repr__(self):
		return '{}: {}x,{}y,{}z. at {}'.format(self.__class__.__name__,self.x,self.y,self.z,hex(id(self)))

	def __sub__(self,other):
		if not isinstance(other,Point3):
			raise TypeError('Invalid type: {}'.format(type(other)))
		return Vector3(self.x-other.x,self.y-other.y,self.z-other.z)
	def __mul__(self,other):
		if type(other) not in [int,float]:
			raise TypeError('Invalid type: {}'.format(type(other)))
		return Point3(other*self.x,other*self.y,other*self.z)
	def __imul__(self,other):
		if type(other) not in [int,float]:
			raise TypeError('Invalid type: {}'.format(type(other)))
		num = other
		return Point3(num*self.x,num*self.y,num*self.z)
	def __rmul__(self,other):
		if type(other) not in [int,float]:
			raise TypeError('Invalid type: {}'.format(type(other)))
		return Point3(other*self.x,other*self.y,other*self.z)
	def __truediv__(self,num):
		if type(num) not in [int,float]:
			raise TypeError('Invalid type: {}'.format(type(other)))
		return Point3(num/self.x,num/self.y,num/self.z)
	def __itruediv__(self,num):
		if type(num) not in [int,float]:
			raise TypeError('Invalid type: {}'.format(type(other)))
		return Point3(num/self.x,num/self.y,num/self.z)
	def __rtruediv__(self,num):
		if type(nuum) not in [int,float]:
			raise TypeError('Invalid type: {}'.format(type(other)))
		return Point3(num/self.x,num/self.y,num/self.z)
	def __floordiv__(self,num):
		if type(num) not in [int,float]:
			raise TypeError('Invalid type: {}'.format(type(other)))
		return Point3(num/self.x,num/self.y,num/self.z)
	def __ifloordiv__(self,num):
		if type(num) not in [int,float]:
			raise TypeError('Invalid type: {}'.format(type(other)))
		return Point3(num/self.x,num/self.y,num/self.z)
	def __rfloordiv__(self,num):
		if type(num) not in [int,float]:
			raise TypeError('Invalid type: {}'.format(type(other)))
		return Point3(num/self.x,num/self.y,num/self.z)

	def __lt__(self,other):
		if not isinstance(other,Point3):
			raise TypeError('Both must be a Point3 instance')
		return distance_from_origine(self) < distance_from_origine(other)
	def __le__(self,other):
		if not isinstance(other,Point3):
			raise TypeError('Both must be a Point3 instance')
		return distance_from_origine(self) <= distance_from_origine(other)
	def __gt__(self,other):
		if not isinstance(other,Point3):
			raise TypeError('Both must be a Point3 instance')
		return distance_from_origine(self) > distance_from_origine(other)
	def __ge__(self,other):
		if not isinstance(other,Point3):
			raise TypeError('Both must be a Point3 instance')
		return distance_from_origine(self) >= distance_from_origine(other)
	def __bool__(self):
		return 
	def distance_from_origine(self):
		return sqrt(self.x**2+self.y**2+self.z**2)