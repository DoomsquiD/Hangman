# Python Hangman Graphics using TKinter canvas

from tkinter import *

class Hangman:

	def __init__(self):
	
		window = Tk()
		window.title("Hangman")
		
		self.width = 640
		self.height = 480
		self.canvas = Canvas(window, bg = "white", width = self.width, \
		height = self.height)
		self.canvas.pack()
		
		frame = Frame(window)
		frame.pack()
		
		Label(frame, text = "Guess a letter: ").pack(side = LEFT)
		self.entry = Entry(frame, width = 4)
		self.entry.pack(side = TOP)
		
		frame1 = Frame(window)
		frame1.pack()
		
		btNewWord = Button(frame1, text = "New Word", command = self.newWord)
		btNewWord.pack(side = LEFT)
		
		btCheckLetter = Button(frame1, text = "Check Letter", command = self.checkLetter)
		btCheckLetter.pack(side = LEFT)
		
		btCheckIncorrect = Button(frame1, text = "[test incorrect letter]", command = self.incorrect)
		btCheckIncorrect.pack(side = RIGHT)
		
		self.setupGame()
	
		window.mainloop()
		
	def setupGame(self):
	
		self.count = 0
		
		self.canvas.create_line(40, 350, 170, 350, width = 3)
		self.canvas.create_line(105, 350, 105, 100, width = 3)
		self.canvas.create_line(105, 100, 220, 100, width = 3)
		
	def newWord(self):
	
		print("New Word here")
		self.canvas.delete("all")
		self.setupGame()
		
	def checkLetter(self):
	
		letterGuess = self.entry.get()
		if len(letterGuess) > 1: letterGuess = letterGuess[:1]
		print("Your letter is", letterGuess)
		
	def incorrect(self):
		
		if self.count == 0:
		
			# Head oval
			self.canvas.create_oval(190, 130, 250, 190, width = 3)
			self.count += 1
			
		elif self.count == 1:
		
			# Body line
			self.canvas.create_line(220, 270, 220, 190, width = 3)
			self.count += 1
			
		elif self.count == 2:
		
			# Left arm line
			self.canvas.create_line(220, 200, 180, 240, width = 3)
			self.count += 1
			
		elif self.count == 3:
		
			# Right arm line
			self.canvas.create_line(220, 200, 260, 240, width = 3)
			self.count += 1
			
		elif self.count == 4:
		
			# Left leg line
			self.canvas.create_line(220, 270, 180, 310, width = 3)
			self.count += 1
			
		elif self.count == 5:
		
			# Right leg line
			self.canvas.create_line(220, 270, 260, 310, width = 3)
			self.count += 1
			
		elif self.count == 6:
		
			self.gameOver()
			
	def gameOver(self):
	
		# Noose line
		self.canvas.create_line(220, 99, 220, 130, width = 3)
		
		self.canvas.create_text(320, 50, text = "Game Over!", font = ("Purisa", 30))
		
Hangman()
