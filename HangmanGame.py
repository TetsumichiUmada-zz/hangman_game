"""
--------------------------------------------------------
HangmanGame.py Ver.1

Author: Tetsumichi Umada

Requirements:
	python 2.xx
	pygame
--------------------------------------------------------
"""

import pygame
import random
from pygame.locals import *

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
RED =   (255,   0,   0)

# set up for screen ........
pygame.init()
SIZE = [800, 500]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hangman Game")

# set text file for vocaburary list
fileName = "VocabHungmanGame.txt"

clock = pygame.time.Clock()

# functions for drawing the hung man body --------------------------------------------------------------------
# Measurement for body
SCAFFOLD_HEIGHT = 365;
BEAM_LENGTH = 145;
ROPE_LENGTH = 20;
HEAD_RADIUS = 36;
BODY_LENGTH = 145;
ARM_OFFSET_FROM_HEAD = 30;
UPPER_ARM_LENGTH = 74;
LOWER_ARM_LENGTH = 42;
HIP_WIDTH = 35;
LEG_LENGTH = 110;
FOOT_LENGTH = 30;


def drawScaffold(self):
	scaffoldTopX = self.get_width()/2 - UPPER_ARM_LENGTH;
	scaffoldTopY = self.get_height()/2 - BODY_LENGTH - HEAD_RADIUS * 2 - ROPE_LENGTH;
	scaffoldBottomY = scaffoldTopY + SCAFFOLD_HEIGHT;
	pygame.draw.line(self, BLACK, [scaffoldTopX, scaffoldTopY], [scaffoldTopX, scaffoldBottomY], 3)
	beamRightX = scaffoldTopX + BEAM_LENGTH;
	pygame.draw.line(self, BLACK, [scaffoldTopX, scaffoldTopY], [beamRightX, scaffoldTopY], 3)
	ropeBottomY = scaffoldTopY + ROPE_LENGTH;
	pygame.draw.line(self, BLACK, [beamRightX, scaffoldTopY], [beamRightX, ropeBottomY], 3)
# End of drawScaffold(self)

def drawHead(self):
	xPosition = self.get_width()/2 - UPPER_ARM_LENGTH + BEAM_LENGTH;
	yPosition = self.get_height()/2 - BODY_LENGTH - HEAD_RADIUS;
	pygame.draw.circle(self, BLACK, [xPosition, yPosition], HEAD_RADIUS, 3)
# End of drawHead(self)

def drawBody(self):
	xPosition = self.get_width()/2 + UPPER_ARM_LENGTH/2 + HEAD_RADIUS
	yTop = self.get_height()/2 - BODY_LENGTH
	yBottom = yTop + BODY_LENGTH;
	pygame.draw.line(self, BLACK, [xPosition, yTop], [xPosition, yBottom], 3)
# Eed of drawBody(self)

def drawLeftArm(self):
	armStartX = self.get_width()/2 + UPPER_ARM_LENGTH/2 + HEAD_RADIUS
	armEndX = self.get_width()/2 + UPPER_ARM_LENGTH/2 + HEAD_RADIUS - UPPER_ARM_LENGTH
	upperArmHeightY = self.get_height()/2 - BODY_LENGTH + ARM_OFFSET_FROM_HEAD
	pygame.draw.line(self, BLACK, [armStartX, upperArmHeightY], [armEndX, upperArmHeightY], 3)
	lowerArmEndY = upperArmHeightY + LOWER_ARM_LENGTH
	pygame.draw.line(self, BLACK, [armEndX, upperArmHeightY], [armEndX, lowerArmEndY], 3)
#End of drawLeftArm(self)

def drawRightArm(self):
	armStartX = self.get_width()/2 + UPPER_ARM_LENGTH/2 + HEAD_RADIUS
	armEndX = self.get_width()/2 + UPPER_ARM_LENGTH/2 + HEAD_RADIUS + UPPER_ARM_LENGTH
	upperArmHeightY = self.get_height()/2 - BODY_LENGTH + ARM_OFFSET_FROM_HEAD
	pygame.draw.line(self, BLACK, [armStartX, upperArmHeightY], [armEndX, upperArmHeightY], 3)
	lowerArmEndY = upperArmHeightY + LOWER_ARM_LENGTH
	pygame.draw.line(self, BLACK, [armEndX, upperArmHeightY], [armEndX, lowerArmEndY], 3)
# End of drawRightArm(self)

def drawLeftLeg(self):
	hipStartX = self.get_width()/2 + UPPER_ARM_LENGTH/2 + HEAD_RADIUS
	hipEndX = hipStartX - HIP_WIDTH
	hipHeightY = self.get_height()/2
	pygame.draw.line(self, BLACK, [hipStartX, hipHeightY], [hipEndX, hipHeightY], 3)
	leftLegY = hipHeightY + LEG_LENGTH
	pygame.draw.line(self, BLACK, [hipEndX, hipHeightY], [hipEndX, leftLegY], 3)
# End of drawLeftLeg(self)

def drawRightLeg(self):
	hipStartX = self.get_width()/2 + UPPER_ARM_LENGTH/2 + HEAD_RADIUS
	hipEndX = hipStartX + HIP_WIDTH
	hipHeightY = self.get_height()/2
	pygame.draw.line(self, BLACK, [hipStartX, hipHeightY], [hipEndX, hipHeightY], 3)
	leftLegEndY = hipHeightY + LEG_LENGTH
	pygame.draw.line(self, BLACK, [hipEndX, hipHeightY], [hipEndX, leftLegEndY], 3)
# End of drawRightLeg(self)

def drawLeftFoot(self):
	footStartX = self.get_width()/2 + UPPER_ARM_LENGTH/2 + HEAD_RADIUS - HIP_WIDTH
	footEndX = footStartX - FOOT_LENGTH
	footHeightY = self.get_height()/2 + LEG_LENGTH
	pygame.draw.line(self, BLACK, [footStartX, footHeightY], [footEndX, footHeightY], 3)
# End of drawLeftFoot(self)

def drawRightFoot(self):
	footStartX = self.get_width()/2 + UPPER_ARM_LENGTH/2 + HEAD_RADIUS + HIP_WIDTH
	footEndX = footStartX + FOOT_LENGTH
	footHeightY = self.get_height()/2 + LEG_LENGTH
	pygame.draw.line(self, BLACK, [footStartX, footHeightY], [footEndX, footHeightY], 3)
# End of drawRightFoot()

def drawHangMan(screen, guessCounter, word):
	if guessCounter == 8:
		drawHead(screen)

	if guessCounter == 7:
		drawHead(screen)
		drawBody(screen)

	if guessCounter == 6:
		drawHead(screen)
		drawBody(screen)
		drawLeftArm(screen)

	if guessCounter == 5:
		drawHead(screen)
		drawBody(screen)
		drawLeftArm(screen)
		drawRightArm(screen)

	if guessCounter == 4:
		drawHead(screen)
		drawBody(screen)
		drawLeftArm(screen)
		drawRightArm(screen)
		drawLeftLeg(screen)

	if guessCounter == 3:
		drawHead(screen)
		drawBody(screen)
		drawLeftArm(screen)
		drawRightArm(screen)
		drawLeftLeg(screen)
		drawRightLeg(screen)

	if guessCounter == 2:
		drawHead(screen)
		drawBody(screen)
		drawLeftArm(screen)
		drawRightArm(screen)
		drawLeftLeg(screen)
		drawRightLeg(screen)
		drawLeftFoot(screen)

	if guessCounter == 1:
		drawHead(screen)
		drawBody(screen)
		drawLeftArm(screen)
		drawRightArm(screen)
		drawLeftLeg(screen)
		drawRightLeg(screen)
		drawLeftFoot(screen)
		drawRightFoot(screen)

		# print text: game over .............................................................
		font = pygame.font.SysFont(None, 70)
		title = font.render("Game Over", True, BLUE)
		xPosition = (screen.get_width() - title.get_width()) / 2
		yPosition = ((screen.get_height() - title.get_height()) /2 ) - title.get_height()
		screen.blit(title, [xPosition, yPosition])

		message = "The word was: " + word
		answer = font.render(message, True, BLUE)
		xPoint = (screen.get_width() - answer.get_width()) / 2
		yPoint = ((screen.get_height() - answer.get_height()) /2 )
		screen.blit(answer, [xPoint, yPoint])


# End of drawHangMan

# End of hang man body parts --------------------------------------------------

def introWindow():
	intro = True

	screen.fill(WHITE)

	font = pygame.font.SysFont(None, 55)
	title = font.render("Hangman Game", True, BLACK)
	xPosition = (screen.get_width() - title.get_width()) / 2

	yPosition = ((screen.get_height() - title.get_height()) /2 ) - title.get_height()
	screen.blit(title, [xPosition, yPosition])

	messageFont = pygame.font.SysFont(None, 30)
	message = messageFont.render("Hit Enter to Play", False, BLACK)
	x = (screen.get_width() - message.get_width()) / 2
	y = yPosition + title.get_height()
	screen.blit(message, [x, y])

	pygame.display.update()

	while intro:
		for event in pygame.event.get():
			if (event.type == KEYDOWN) and (event.key == pygame.K_RETURN):
				playGame()

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		clock.tick(20)

# END of introWindow():



def gameWin(word):
	intro = True

	screen.fill(WHITE)


	congratsImage = pygame.image.load ("congrats.png")
	congratsImage = pygame.transform.scale(congratsImage, (608, 500))
	imageRect = congratsImage.get_rect()
	screen.blit(congratsImage, imageRect)

	font = pygame.font.SysFont(None, 65)
	title = font.render("Congratulations, you win!", True, BLACK)
	xPosition = (screen.get_width() - title.get_width()) / 2
	yPosition = ((screen.get_height() - title.get_height()) /2 ) - title.get_height()
	screen.blit(title, [xPosition, yPosition])

	message = "The word was: " + word
	answer = font.render(message, True, BLACK)
	xPoint = (screen.get_width() - answer.get_width()) / 2
	yPoint = ((screen.get_height() - answer.get_height()) /2 )
	screen.blit(answer, [xPoint, yPoint])


	directionFont = pygame.font.SysFont(None, 30)
	direction = directionFont.render("Hit Enter to Play again", False, BLACK)
	x = (screen.get_width() - direction.get_width()) / 2
	y = yPosition + 3 * title.get_height()
	screen.blit(direction, [x, y])

	pygame.display.update()

	while intro:
		for event in pygame.event.get():
			# print(event)
			if (event.type == KEYDOWN) and (event.key == pygame.K_RETURN):
				# print ("Enter is hitted")
				# print ("you are in game win")
				playGame()

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


		clock.tick(20)

# End of gameOver()


# pick a word  ----------------------------------------------------------------
# Read a file and pick a word for a game
def pickWord(fileName):
	file = open(fileName, "r")
	wordList = file.read().splitlines()
	file.close()

	size = len(wordList)
	index = random.randint(0, size - 1)
	pickedWord =  wordList[index]

	### Debug: check the randomly picked word
	# print (pickedWord)

	return pickedWord
# End of pickWord()

# Create a hidden word.........................................
def numOfLetters(word):
	result = ""
	for num in range(len(word)):
		result = result + "-"

	return result
# END of numOfLetters(word):


def playGame():
	# initializing a word...  --------------------------------------
	guessCounter = 9
	incorrectLetters = ""

	word = pickWord(fileName)
	hiddenWord = numOfLetters(word)

	playing = True

	while playing:
		screen.fill(WHITE)

		# handling key events.............................................................
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.unicode.isalpha():
					key = event.unicode.upper()  # change to upper cases

					# check characters if it is in the word
					if key in word:
						for idx in range(len(word)):
							if key == word[idx]:
								hiddenWord = hiddenWord[:idx] + key + hiddenWord[(idx + 1):]

					# check if input ch is in incorrect letters...
					else:
						if key not in incorrectLetters:
							guessCounter = guessCounter - 1
							incorrectLetters += key

							if guessCounter == 1:
								playing = False

			if (playing == False) and (event.key == pygame.K_RETURN):
				playing = True

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


		# Display hidden word  .....................................................
		basicfont = pygame.font.SysFont(None, 48)
		text = basicfont.render(hiddenWord, True, BLACK)
		xPosition = screen.get_width()/2 - UPPER_ARM_LENGTH
		yPosition = screen.get_height() - HEAD_RADIUS * 2.5
		screen.blit(text, [xPosition, yPosition])

		# Display incorrect letter   ................................................
		font = pygame.font.SysFont(None, 25)
		incorrectNote = font.render(incorrectLetters, True, BLACK)
		shape = incorrectNote.get_rect()
		shape.x = screen.get_width()/2 - UPPER_ARM_LENGTH
		shape.y = screen.get_height() - HEAD_RADIUS * 1.5


		screen.blit(incorrectNote, shape)
		drawScaffold(screen)
		drawHangMan(screen, guessCounter, word)

		# winning......................
		if word == hiddenWord:
			gameWin(word)

		pygame.display.flip()

# END of playGame()


# Main function
def main():
	introWindow()
	playGame()

# END of main


if __name__ == "__main__":
	main()
