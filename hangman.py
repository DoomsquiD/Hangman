# Python Hangman Final Project
#
# CIT 144
#
# Created by Evan Strobel, Bryan Boone, and Aaron Tucker

from tkinter import *  
import random  

class Hangman:  # creates main class

	def __init__(self):  # initial function and GUI
	
		window = Tk()
		window.title('Hangman')
		window.configure(bg = 'white')
		
		self.width = 640
		self.height = 480
		self.canvas = Canvas(window, bg = 'white', highlightthickness = 0, width = self.width, 
		height = self.height)
		self.canvas.pack()
		
		frame = Frame(window, bg = 'white')
		frame.pack()
		
		Label(frame, text = 'Guess a letter: ', bg = 'white').pack(side = LEFT)
		self.entry = Entry(frame, width = 4)
		self.entry.pack(side = TOP)
		
		self.frame1 = Frame(window)
		self.frame1.pack()
		
		btNewWord = Button(self.frame1, text = 'New Word', command = self.newWord)
		btNewWord.pack(side = LEFT)
		
		self.btCheckLetter = Button(self.frame1, text = 'Check Letter', command = self.letterGuess)
		self.btCheckLetter.pack(side = LEFT)
		
		self.setupGame()
	
		window.mainloop()
		
	def setupGame(self):  # function that sets up each game
	
		self.count = 0
		
		self.canvas.create_line(40, 350, 170, 350, width = 3)
		self.canvas.create_line(105, 350, 105, 100, width = 3)
		self.canvas.create_line(105, 100, 220, 100, width = 3)
		
		self.currentWord = self.createRandomWord() # sets currentWord to random word
		self.entry.delete(0, 'end')  # clears entry box
		self.btCheckLetter.config(state = NORMAL)  # enables check letter button
		
		# creates lists used:
		self.guessWord = []
		self.letterStorage = []
		self.incorrectStorage = []
		
		for character in self.currentWord: # adds a blank for every letter in current word
			self.guessWord.append("_")
		
		self.canvas.create_text(320, 415, text = self.guessWord, font = ('Purisa', 30),
		tag = 'word')  # writes blanks to canvas
		
	def createRandomWord(self): # returns random word from list
		
		strWord = ''
		
		lstWords = ['banjo', 'azure', 'absurd', 'awkward', 'blitz',
					'espionage', 'dwarves', 'galaxy', 'glyph',
					'lucky', 'microwave', 'jumbo', 'oxygen',
					'puppy', 'sphinx', 'strength', 'quiz',
					'python', 'voodoo', 'wyvern', 'zombie',
					'wizard', 'pajama', 'vodka', 'mnemonic', 'lion', 
					'umbrella', 'window', 'computer', 'glass', 
					'juice', 'chair', 'desktop',
					'laptop', 'dog', 'cat', 'lemon', 
					'cable', 'mirror', 'hat', 'smoke', 'virus',
					'processor', 'flux', 'gorilla', 'industrial',
					'spine', 'warlock', 'wind', 'ocean', 'taco',
					'storm', 'circuit', 'halloween', 'boiler', 'squid',
					'agave', 'caffiene', 'jellyfish', 'turbine']
					
		random.shuffle(lstWords)
		strWord = lstWords[1]
		return(strWord)
		
	def newWord(self): # clears canvas and sets up new game
	
		self.canvas.delete('all')
		self.setupGame()
		
	def incorrect(self): # prints incorrect letters and draws body
	
		self.canvas.delete('incorrect')
		self.canvas.create_text(460, 230, text = self.incorrectStorage, font = ('Purisa', 16),
		fill = 'maroon', tag = 'incorrect')
		
		if self.count == 0:
			
			self.canvas.create_oval(190, 130, 250, 190, width = 3) # Head oval
			self.count += 1
			
		elif self.count == 1:
		
			self.canvas.create_line(220, 270, 220, 190, width = 3) # Body line
			self.count += 1
			
		elif self.count == 2:
		
			self.canvas.create_line(220, 200, 180, 240, width = 3) # Left arm line
			self.count += 1
			
		elif self.count == 3:
		
			self.canvas.create_line(220, 200, 260, 240, width = 3) # Right arm line
			self.count += 1
			
		elif self.count == 4:
		
			self.canvas.create_line(220, 270, 180, 310, width = 3) # Left leg line
			self.count += 1
			
		elif self.count == 5:
			
			self.canvas.create_line(220, 270, 260, 310, width = 3) # Right leg line
			self.count += 1
			
		elif self.count == 6:
		
			self.gameOver()
			
	def printUsed(self): # lets user know that the letter has already been guessed
	
		self.canvas.create_text(320, 360, text = 'You have already guessed that letter!',
		font = ('Purisa', 10), tag = 'msg')
			
	def gameOver(self): # shows game over screen
	
		self.btCheckLetter.config(state = DISABLED) # disables check letter button
		
		self.canvas.create_line(220, 99, 220, 130, width = 3) # Noose line
		
		self.canvas.create_text(320, 50, text = 'Game Over!', fill = 'red', 
		font = ('Purisa', 30))
		
		self.canvas.delete('word')
		self.canvas.create_text(320, 415, text = self.currentWord, fill = 'red',
		font = ('Purisa', 30), tag = 'word')
		
	def gameWin(self): # shows game won screen
	
		self.btCheckLetter.config(state = DISABLED) # disables check letter button
		self.canvas.delete("msg")
		self.canvas.create_text(320, 50, text = "You win!", fill = 'green',
		font = ("Purisa", 30))

	def letterGuess(self): # checks if letter from entry box is in word
	
		self.canvas.delete("msg")
		guess = self.entry.get() # gets input from entry box
		
		if guess.isalpha(): # checks if entry is a letter from a to z
		
			guess = guess.lower() # sets entry to lowercase so it matches word
		
			self.entry.delete(0, 'end') # clears entry box
		
			if not guess in self.letterStorage: # checks if letter has been guessed already
		
				if guess in self.currentWord:  #checks if letter is in word
				
					self.letterStorage.append(guess) # adds letter to list of letters guessed
				
					for x in range(0, len(self.guessWord)): # adds guessed letter to correct place in current word
				
						if self.currentWord[x] == guess:
							self.guessWord[x] = guess
						
						self.canvas.delete("word")
						
						self.canvas.create_text(320, 415, text = self.guessWord, 
						font = ("Purisa", 30), tag = "word")
					
				else: # adds letter to guessed and incorrect lists
			
					self.letterStorage.append(guess)
					self.incorrectStorage.append(guess)
					self.incorrect()
				
			else:
				self.printUsed()
			
			if not '_' in self.guessWord: # once all letters guessed, shows game won screen
				self.gameWin()
		
		else: # warns user if character entered is not letter
		
			self.canvas.delete('msg')
			self.canvas.create_text(320, 360, text = "Enter a letter from a to z!" ,
			font = ("Purisa", 10), tag = "msg")
			
Hangman()
