from tkinter import *
import math

fields = ('side1', 'side2', 'side3')

def sidesort(entries):
	s1 = float(entries['side1'].get())
	s2 = float(entries['side2'].get())
	s3 = float(entries['side3'].get())
	sides = sorted([s1, s2, s3])
	return sides

	
def categorize(entries):
	#s1 = float(entries['side1'].get())
	#s2 = float(entries['side2'].get())
	#s3 = float(entries['side3'].get())
	#sides = sorted([s1, s2, s3])
	
	sides = sidesort(entries)
	right, acute, obtuse = False, False, False
	tricomment = None
	
	if sides[0] + sides[1] <= sides[2]:
		print('Error: This is not a triangle')
	else:
		product 	= sides[0]**2 + sides[1]**2
		bproduct 	= sides[2]**2
		
		if product == bproduct:
			right = True
			tricomment = 'Right'
		elif product < bproduct:
			obtuse = True
			tricomment = 'Obtuse'
		else:
			acute = True
			tricomment = 'Acute'
			
	res.configure(text='This triangle is: %s' % tricomment)
	#print(sides)
			
def area(entries):
	sides = sidesort(entries)
	# Heron's Formula
	s 		= sum(sides)/2
	Area 	= math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2]))
	res.configure(text='[Area: \t %.4f square units]' % Area)
	print('[Area: \t %.4f square units]' % Area)
	
def angles(entries):
	# Basic Trig on Right Triangles
	#if right == True:
	#	smlhyp = sides[0]/sides[2]
	#	angle0 = math.degrees(math.asin(smlhyp))
	#	angle1 = 90 - angle0
	#	angle2 = 90
	#	return '[Angles: %.4f, %.4f, %.4f]' % (angle0, angle1, angle2)
	# Law of Cosine for the largest angle, Law of Sine for the middle, 180 in triangle for last
	#else:
	sides = sidesort(entries)
	angle2 = math.degrees(math.acos(((sides[2]**2-sides[0]**2-sides[1]**2)/(-2*sides[0]*sides[1]))))
	angle1 = math.degrees(math.asin(math.sin(math.radians(angle2))*sides[1]/sides[2]))
	angle0 = 180-angle2-angle1
	comment= '[Angles: %.2f, %.2f, %.2f]' % (angle0, angle1, angle2)
	res.configure(text=comment)
	print(comment)
	
def makeform(root, field):
	entries={}
	for field in fields:
		row = Frame(root)
		lab = Label(row, width=5, text=field+': ', anchor=W)
		ent = Entry(row)
		ent.insert(0,'0')
		row.pack(side=TOP,fill=X, padx=5, pady=5)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT,expand=YES,fill=X)
		entries[field] = ent
	return entries	

if __name__=='__main__':
	root = Tk()
	Label(root, text='Triangle Calculator').pack(side=TOP)
	ents = makeform(root, fields)
	root.bind('<Return>',(lambda event, e=ents: fetch(e)))
	#b1 = Button(root, text='Area',command=(lambda e=ents:final_balance(e))).pack()
	#b3 = Button(root, text='Quit', command=root.quit)
	#Label(root, text='Side 1: ').pack()
	#Label(root, text='Side 2: ').pack()
	#Label(root, text='Side 3: ').pack()
	#ent1 = Entry(root).pack()
	#ent2 = Entry(root).pack()
	#ent3 = Entry(root).pack()
	res = Label(root)
	res.pack()
	b1 = Button(root,text='Type of Triangle',command=(lambda e=ents:categorize(e)))
	b2 = Button(root,text='Area',command=(lambda e=ents:area(e)))
	b3 = Button(root,text='Angles',command=(lambda e=ents:angles(e)))
	b4 = Button(root,text='Quit',command=root.quit)
	padxx=5
	b1.pack(side=LEFT,padx=padxx)
	b2.pack(side=LEFT,padx=padxx)
	b3.pack(side=LEFT,padx=padxx)
	b4.pack(side=LEFT,padx=padxx)
	
	root.mainloop()
	
	
	
	
	
	