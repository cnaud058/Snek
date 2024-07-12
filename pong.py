import pygame
from random import random
 
pygame.init()
screen = pygame.display.set_mode((500, 500))
 
player1 = 200 # holds the y position of player1
player2 = 200 # holds the y position of player2
 
ball = [240, 240] # holds x, y of the ball's position
vel = [10*random()-5, 10*random()-5] # holds x, y of the ball's velocity
 
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    player1 -= 10
  if keys[pygame.K_s]:
    player1 += 10
  if keys[pygame.K_UP]:
    player2 -= 10
  if keys[pygame.K_DOWN]:
    player2 += 10

  # To program a computer opponent, you can add the code here
    
  
  # Adjust the position of the ball according to its velocity  

  ball[0] += vel[0]
  ball[1] += vel[1]
  
  # Adjust the ball's velocity if it hits the top or bottom
  
  if ball[1] < 0:
    vel[1] = abs(vel[1])
  if ball[1] + 20 > 500:
    vel[1] = -abs(vel[1])
  
  # Detect when the ball hits a player
  
  if ball[0] - 20 <= 50 <= ball[0] + 20 and ball[1] - 100 <= player1 <= ball[1] + 20:
    vel[0] = abs(vel[0])
  if ball[0] - 20 <= 430 <= ball[0] + 20 and ball[1] - 100 <= player2 <= ball[1] + 20:
    vel[0] = -abs(vel[0])

    
  # Adjust the player's position if it leaves the screen

  if player1 < 0:
    player1 = 0
  if player1 > 400:
    player1 = 400
    
  if player2 < 0:
    player2 = 0
  if player2 > 400:
    player2 = 400

  screen.fill(0x000000)
  pygame.draw.rect(screen, 0xffffff, [50, player1, 20, 100])
  pygame.draw.rect(screen, 0xffffff, [430, player2, 20, 100])
  pygame.draw.rect(screen, 0xffffff, ball + [20, 20])
  pygame.display.flip()
  pygame.time.wait(1000//60)
