import math

class Triangle:
	def __init__(self, side0, side1, side2):
		self.side0 = side0
		self.side1 = side1
		self.side2 = side2
		self.sides = sorted([side0, side1, side2])
		self.product 	= self.sides[0]**2 + self.sides[1]**2
		self.bproduct 	= self.sides[2]**2
		self.right, self.acute, self.obtuse = False, False, False
		if self.product == self.bproduct:
			self.right = True
			self.tricomment = 'Right'
		elif self.product < self.bproduct:
			self.obtuse = True
			self.tricomment = 'Obtuse'
		else:
			self.acute = True
			self.tricomment = 'Acute'			
		self.tindent = '\n'+'-'*30+'\n'*2
		self.bindent = '\n'*2+'-'*30+'\n'
		
	def __repr__(self):
		return 	self.tindent+'[Sides:  %s, %s, %s]\n[Type: \t %s]' % (self.side0, self.side1, self.side2, self.tricomment)
		
	def angles(self):
		# Basic Trig on Right Triangles
		if self.right == True:
			self.smlhyp = self.sides[0]/self.sides[2]
			self.angle0 = math.degrees(math.asin(self.smlhyp))
			self.angle1 = 90 - self.angle0
			self.angle2 = 90
			return '[Angles: %.4f, %.4f, %.4f]' % (self.angle0, self.angle1, self.angle2)
		# Law of Cosine for the largest angle, Law of Sine for the middle, 180 in triangle for last
		else:
			self.angle2 = math.degrees(math.acos(((self.sides[2]**2-self.sides[0]**2-self.sides[1]**2)/(-2*self.sides[0]*self.sides[1]))))
			self.angle1 = math.degrees(math.asin(math.sin(math.radians(self.angle2))*self.sides[1]/self.sides[2]))
			self.angle0 = 180-self.angle2-self.angle1
			return '[Angles: %.4f, %.4f, %.4f]' % (self.angle0, self.angle1, self.angle2)
		
	def area(self):
		#Heron's Formula
		self.s 		= sum(self.sides)/2
		self.Area 	= math.sqrt(self.s*(self.s-self.sides[0])*(self.s-self.sides[1])*(self.s-self.sides[2]))
		return '[Area: \t %.4f square units]' % self.Area
		
	startmessage 	= 'Beginning Test...'
	endmessage		= '...Testing Complete'
	
			
if __name__=='__main__':
	print(Triangle.startmessage)
	#X = Triangle(4,3,5)
	#X = Triangle(8,6,5)
	X = Triangle(323,156,202)
	print(X)
	print(X.angles())
	print(X.area())
	#print(Y)
	#print(Y.angles()) 
	#print(Z)
	#print(Z.angles())
	print(Triangle.endmessage)
