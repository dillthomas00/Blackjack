import pygame

pygame.init()
info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h
screen_width,screen_height = screen_width-5,screen_height-100
screen = pygame.display.set_mode((screen_width, screen_height))

#General Colours if needed
green = (50, 205, 50)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
                        
##    pygame.draw.rect(screen, green, pygame.Rect(100, 0, screen_width - 200, screen_height / 2))
##    pygame.draw.circle(screen, green, (int(screen_width / 2), 300), 750)


    table = pygame.image.load("table.png")
    table = pygame.transform.scale(table, (1920, 950))
    screen.blit(table, (0, 0))
##    deck = pygame.image.load("deck.png")
##    deck = pygame.transform.scale(deck, (250, 175))
##    screen.blit(deck, (150, 25))
##
##    card = pygame.image.load("card.png")
##    card = pygame.transform.scale(card, (175, 250))
##    screen.blit(card, (150, 225))

      
  pygame.display.flip()


pygame.quit()
quit


