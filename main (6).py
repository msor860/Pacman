import pygame, sys
import os
import random
import time

#note: fix directions, maybe fix collision and image rect as well

player_lives = 3 
score = 0

WIDTH = 800
HEIGHT = 500
#controls how often the gameDisplay should refresh. In our case, it will refresh every 1/12th
FPS = 60

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption('Pacman')
#setting game display size
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACK = (1, 1, 1)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
ORANGE = (255, 150, 0)
MAZE = (70,111,148)

gameDisplay.fill(BACK)
score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
lives_icon = pygame.image.load('Images/Pac-Man.png')

playGame = 1 #change to 0 later
difficulty = 0 # Easy = 0, Normal = 1, Hard = 2
phase = 0 # Attack = 0, Corners = 1, Scatter = 2
end = False # Playing = False, Done = True
scatter = False

left = False # 1
right = False # 2
up = False # 3
down = False # 4
lastKey = 0

pacBigX = 17
pacBigY = 17

class Pacman(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('Images/Pac-Man.png')
    self.rect = self.image.get_rect()
    self.image = pygame.transform.scale(self.image, (pacBigX, pacBigY))
    self.x = WIDTH/1.8
    self.y = HEIGHT/1.345
    self.speed = 0.2
    self.left = pygame.transform.rotate(self.image, 0)
    self.right = pygame.transform.rotate(self.image, 180)
    self.up = pygame.transform.rotate(self.image, 270)
    self.down = pygame.transform.rotate(self.image, 90)
    self.mask = pygame.mask.from_surface(self.image)

  def draw(self):
    gameDisplay.blit(self.image, (self.x, self.y))

class Maze(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("Images/PacMaze3.png").convert_alpha()
    #default bg size = 224, 256
    self.image = pygame.transform.scale(self.image, (380.8,435.2))
    self.rect = self.image.get_rect(center = (400,400))
    #mask = pygame.mask.from_threshold(bg, pygame.Color(MAZE), (1, 1, 1, 255))
    #bg_image = bg.convert()
    #bg_image.set_colorkey(BLACK)
    self.mask = pygame.mask.from_surface(self.image)
    #mask.invert()
    
class Ghosts():
  def __init__(self):
    self.speed = Pacman.speed * 1.2
  #print("info for all ghosts")

class Blinky(Ghosts):
  #Red Ghost: Chases the player (Upper Right)
  print()

class Inky(Ghosts):
  #Blue Ghost: During Chase mode, his target is a bit complex. His target is 
  #relative to both Red and Pac-Man, where the distance Red is from Pink's 
  #target is doubled to get Blue's target. (Lower Right)
  print()

class Pinky(Ghosts):
  #Pink Ghost: Chases the spot 2 dots in front of the player (Upper Left)
  print()

class Clyde(Ghosts):
  #Orange Ghost: Chases the player until 8 dots away, then does corners behavior (Lower Left)
  print()

class Pellet():
  print()

class Fruit(Pellet):
  print()

class PowerUp(Pellet):
  print()

if playGame == 1:
  pacman = Pacman()
  pacmanGroup  = pygame.sprite.GroupSingle(pacman)
  maze = Maze()
  mazeGroup = pygame.sprite.GroupSingle(maze)
  while True:
    collide = False
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          left = True
          down = False
          right = False
          up = False
        elif event.key == pygame.K_DOWN:
          left = False
          down = True
          right = False
          up = False
        elif event.key == pygame.K_RIGHT:
          left = False
          down = False
          right = True
          up = False
        elif event.key == pygame.K_UP:
          left = False
          down = False
          right = False
          up = True
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          left = False
        elif event.key == pygame.K_DOWN:
          down = False
        elif event.key == pygame.K_RIGHT:
          right = False
        elif event.key == pygame.K_UP:
          up = False
    if left == True:
      pacman.rotation = 0
      #pacman.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Images/Pac-Man.png'), (pacBigX, pacBigY)), 0)
      pacman.image = pacman.left
      pacman.x -= pacman.speed
    elif down == True:
      pacman.rotation = 90
      #pacman.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Images/Pac-Man.png'), (pacBigX, pacBigY)), 90)
      pacman.image = pacman.down
      pacman.y += pacman.speed
    elif right == True:
      pacman.rotation = 180
      #pacman.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Images/Pac-Man.png'), (pacBigX, pacBigY)), 180)
      pacman.image = pacman.right
      pacman.x += pacman.speed
    elif up == True:
      pacman.rotation = 270
      #pacman.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Images/Pac-Man.png'), (pacBigX, pacBigY)), 270)
      pacman.image = pacman.up
      pacman.y -= pacman.speed
    pacman.rect.center = (pacman.x + pacBigX/2, pacman.y + pacBigY/2)
    gameDisplay.fill(BACK)
    if pygame.sprite.spritecollide(pacmanGroup.sprite,mazeGroup,False):
      if pygame.sprite.spritecollide(pacmanGroup.sprite,mazeGroup,False,pygame.sprite.collide_mask):
        gameDisplay.fill('red')
        gameDisplay.blit(maze.image, (WIDTH/3, HEIGHT/10))
        pacman.draw()
    #print(collide)
    # if collide == True:
    #   gameDisplay.fill(RED)
    # else:
    #   gameDisplay.fill(BACK)
    gameDisplay.blit(maze.image, (WIDTH/3, HEIGHT/10))
    maze.rect.center = (WIDTH/3, HEIGHT/10)
    pacman.mask = pygame.mask.from_surface(pacman.image)
    #overlap = mask.overlap(pacman.mask, (pacman.x,pacman.y))
    #if overlap:
    #  print(overlap)
    #else:
    #  print("B")
    #if pygame.sprite.spritecollideany(pacman, mask):
      #print("yay it works")
    pacman.draw()
    pygame.display.update()
  if difficulty == 0:
    while end == False and scatter == False:
      phase = 1
      time.sleep(15)
      phase = 0
      time.sleep(15)
    if scatter == True:
      time.sleep(20)
      scatter = False
  elif difficulty == 1:
    while end == False and scatter == False:
      phase = 0
      time.sleep(22.5)
      phase = 1
      time.sleep(7.5)
    if scatter == True:
      time.sleep(15)
      scatter = False
  else:
    while end == False and scatter == False:
      phase = 1
    if scatter == True:
      time.sleep(10)
      scatter = False
  
#if pygame.sprite.spritecollideany(pacman, ghosts):

#color collision: https://stackoverflow.com/questions/60914717/color-collision-detection-in-pygame
  
      
  
'''events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          pacman.rotation = 0
          pacman.image = pygame.transform.rotate(pygame.image.load('Images/Pac-Man.png'), 0)
          pacman.x -= pacman.speed
        elif event.key == pygame.K_DOWN:
          pacman.rotation = 90
          pacman.image = pygame.transform.rotate(pygame.image.load('Images/Pac-Man.png'), 90)
          pacman.y += pacman.speed
        elif event.key == pygame.K_RIGHT:
          pacman.rotation = 180
          pacman.image = pygame.transform.rotate(pygame.image.load('Images/Pac-Man.png'), 180)
          pacman.x += pacman.speed
        elif event.key == pygame.K_UP:
          pacman.rotation = 270
          pacman.image = pygame.transform.rotate(pygame.image.load('Images/Pac-Man.png'), 270)
          pacman.y -= pacman.speed'''