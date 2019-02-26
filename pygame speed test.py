import pygame
import sys
import random
import time

#General Pygame  Setup
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen_width, screen_height = screen_width-5, screen_height-50
speed = 60 #fps
fpsControl = pygame.time.Clock()
font = pygame.font.Font(None, 36)

#Image Asset
hidden_card = pygame.image.load("./Assets/card.png")
hidden_card = pygame.transform.scale(hidden_card, (180, 200))

#Card Variables
card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]
card_types = ["S", "C", "D", "H"]
duplicates = []

class player_card(object):
    def create_card():
        selected_card = card_numbers[random.randint(0, 12)]
        selected_card_type = card_types[random.randint(0, 3)]
        card_picked = selected_card + selected_card_type
        if card_picked in duplicates:
            player_card.create_card()
        else:
            duplicates.append(card_picked)
            if "S" in card_picked:
                card_value = card_picked.replace("S","")
            elif "C" in card_picked:
                card_value = card_picked.replace("C","")
            elif "D" in card_picked:
                card_value = card_picked.replace("D","")
            else:
                card_value = card_picked.replace("H", "")
                
            if card_value == "A":
                card_value = 11
            elif card_value == "J" or card_value == "K" or card_value == "Q":
                card_value = 10
            return card_value, card_picked



##class dealer_card(object):
##    def reveal(self):
##        pass

# Main Application
class app():
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.x = 200
        self.y = 430
        self.player_state = 0
        self.computer_state = 0

        self.drawn_cards = []
        self.drawn_cards_positions = []
        self.player_value = 0
        self.computer_value = 0

        self.current_x = 430
        self.current_y = 710
        self.main()

    def draw_a_card(self):
        try:
            card_value, card_picked = player_card.create_card()
        except TypeError: #Calls the function again because a duplicate occoured
            card_value, card_picked = player_card.create_card()
        self.drawn_cards.append(card_picked)
        self.player_value = self.player_value + int(card_value)
        self.drawn_cards_positions.append(self.current_x) #X
        self.drawn_cards_positions.append(self.current_y)  #Y      
        self.card_animation()
        self.x = 200
        self.y = 430
        self.current_x = self.current_x + 220
        if self.player_value <= 15:
            self.draw_a_card()
        elif self.player_value > 21:
            # need to reset the game
            time.sleep(0.1)
            self.__init__()


    def main(self):
        table = pygame.image.load("./Assets/table.jpg")
        table = pygame.transform.scale(table, (1920, 1050))

        
        card_area = pygame.Rect(190, 420, 370, 630)
        stand_area = pygame.Rect(430, 460, 840, 600)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        self.background.blit(table, (0,0))
        self.screen.blit(self.background, (0,0))

        self.draw_a_card()
        print (self.drawn_cards)
        print ("Player value" , self.player_value)


        
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button.
                        #print (event.pos)
                        if card_area.collidepoint(event.pos):
                            self.draw_a_card()
                        elif stand_area.collidepoint(event.pos):
                            print ("Stick")
                            card_area = pygame.Rect(0,0,0,0)
            pygame.display.flip()
            fpsControl.tick(speed)
        pygame.quit()
        sys.exit()

    def card_animation(self):
        final_x, final_y = self.drawn_cards_positions[-2], self.drawn_cards_positions[-1]
        displacement_x = ((final_x - self.x) / 100) * 2
        displacement_y = ((final_y - self.y) / 100) * 2
        counter = 0
        while counter != 51:
            self.screen.blit(self.background, (0,0))
            self.screen.blit(hidden_card, (int(self.x), int(self.y)))
            self.x = self.x + displacement_x
            self.y = self.y  + displacement_y
            pygame.display.update()
            counter = counter + 1
        time.sleep(0.1)
        reveal_card = pygame.image.load(".//Assets//Revealed Card//" + self.drawn_cards[-1] + ".png")
        reveal_card = pygame.transform.scale(reveal_card, (180, 200))
        self.background.blit(reveal_card, (final_x, final_y))
        self.screen.blit(self.background, (0,0))

app()
