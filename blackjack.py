import pygame
import sys
import random
import time

#General Pygame  Setup
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen_width, screen_height = screen_width-5, screen_height-50
speed = 244 #fps
fpsControl = pygame.time.Clock()

#Image Assets
table = pygame.image.load("./Assets/table.jpg")
table = pygame.transform.scale(table, (1920, 1050))
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
            create_card()
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



class dealer_card(object):
    def reveal(self):
        pass

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
        card_value, card_picked = player_card.create_card()
        self.drawn_cards.append(card_picked)
        self.player_value = self.player_value + int(card_value)
        self.drawn_cards_positions.append(self.current_x) #X
        self.drawn_cards_positions.append(self.current_y)  #Y      
        self.card_animation()
        self.x = 200
        self.y = 430
        self.current_x = self.current_x + 220

        
        

    def main(self):
        card_area = pygame.Rect(190, 420, 370, 630)
        test_area = pygame.Rect(419, 707,623, 917)
        self.screen.blit(table, (0, 0))

        self.draw_a_card()
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
                            pass
                        


            pygame.display.flip()
            fpsControl.tick(speed)
        pygame.quit()
        sys.exit()

    def card_animation(self):
        final_x, final_y = self.drawn_cards_positions[-2], self.drawn_cards_positions[-1]
        displacement_x = ((final_x - self.x) / 100) * 2
        displacement_y = ((final_y - self.y) / 100) * 2
        counter = 0
        pos_counter = 0
        while counter != 51:
            self.screen.blit(table, (0, 0))
            self.screen.blit(hidden_card, (int(self.x), self.y))
            recurring_cards = self.drawn_cards[:-1]
            for x in recurring_cards:
                reveal_card = pygame.image.load(".//Assets//Revealed Card//" + x + ".png")
                reveal_card = pygame.transform.scale(reveal_card, (180, 200))
                pos_x, pos_y = self.drawn_cards_positions[pos_counter], self.drawn_cards_positions[pos_counter + 1]
                self.screen.blit(reveal_card, (pos_x, pos_y))
                pos_counter + 2  
            self.x = self.x + displacement_x
            self.y = self.y  + displacement_y
            pygame.display.update()
            counter = counter + 1
        time.sleep(0.1)
        reveal_card = pygame.image.load(".//Assets//Revealed Card//" + self.drawn_cards[-1] + ".png")
        reveal_card = pygame.transform.scale(reveal_card, (180, 200))
        self.screen.blit(reveal_card, (final_x, final_y))
                                     
##
##    def player_state_checker(self):
##        if self.player_state == 0:
##            pass
##        elif self.player_state == 1:
##            self.screen.blit(hidden_card, (870, 710))
##        elif self.player_state == 2:
##            self.screen.blit(hidden_card, (870, 710))
##            self.screen.blit(hidden_card, (1090, 710))
##        else:
##            self.screen.blit(hidden_card, (870, 710))
##            self.screen.blit(hidden_card, (1090, 710))
##            self.screen.blit(hidden_card, (1310, 710))
##        
##
##    def computer_draw_card(self):
##        if self.computer_state == 0:
##            while self.x <= 875:
##                self.screen.blit(table, (0, 0))
##                self.player_state_checker()
##                self.screen.blit(hidden_card, (int(self.x), int(self.y)))
##                self.x = self.x + 13.4
##                self.y = self.y -5.92
##                pygame.display.update()
##            ##type here
##        elif self.computer_state == 1:
##            while self.x <= 1095:
##                self.screen.blit(table, (0, 0))
##                self.player_state_checker()
##                self.screen.blit(hidden_card, (870, 135))
##                self.screen.blit(hidden_card, (int(self.x), self.y))
##                self.x = self.x + 17.8
##                self.y = self.y - 5.92
##                pygame.display.update()
##        else:
##            while self.x <= 1315:
##                self.screen.blit(table, (0, 0))
##                self.player_state_checker()
##                self.screen.blit(hidden_card, (870, 135))
##                self.screen.blit(hidden_card, (1090, 135))
##                self.screen.blit(hidden_card, (int(self.x), self.y))
##                self.x = self.x + 22.2
##                self.y = self.y - 5.92
##                pygame.display.update()
##        self.computer_state = self.computer_state + 1

app()
