import pygame
import sys
import random
import time

# General Pygame  Setup
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen_width, screen_height = screen_width-5, screen_height-50
fpsControl = pygame.time.Clock()
# Image Asset
hidden_card = pygame.image.load(".//Assets//card.png")
hidden_card = pygame.transform.scale(hidden_card, (180, 200))
# Card Variables
card_numbers = ["A", "2", "3", "4", "5",
                "6", "7", "8", "9", "10", "J", "K", "Q"]
card_types = ["S", "C", "D", "H"]
ace_state = 0

# Creates a new card for the main application


class card(object):
    def create_card():
        selected_card = card_numbers[random.randint(0, 12)]
        selected_card_type = card_types[random.randint(0, 3)]
        card_picked = selected_card + selected_card_type
        if "S" in card_picked:
            card_value = card_picked.replace("S", "")
        elif "C" in card_picked:
            card_value = card_picked.replace("C", "")
        elif "D" in card_picked:
            card_value = card_picked.replace("D", "")
        else:
            card_value = card_picked.replace("H", "")
        if card_value == "A":
            card_value = 1
        elif card_value == "J" or card_value == "K" or card_value == "Q":
            card_value = 10
        return card_value, card_picked

# Application Start Menu


class start_menu():
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.animation_state = 1
        self.animation_reverse = False
        self.main()

    def main(self):
        self.instruction_state_boolean = False
        instructions_state = 1
        game_menu = pygame.image.load(".//Assets//Start Menu//Game Menu.png")
        self.animated_background = pygame.image.load(
            ".//Assets//Start Menu//frame" + str(self.animation_state) + ".jpg")
        self.animated_background = pygame.transform.scale(
            self.animated_background, (1920, 1080))
        x1, y1, x2, y2 = 830, 310, 1120, 370
        self.play_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        x1, y1, x2, y2 = 830, 410, 1120, 470
        self.instructions_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        x1, y1, x2, y2 = 830, 589, 1120, 640
        self.exit_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        self.instruction_exit_area = pygame.Rect(0, 0, 0, 0)
        self.backwards_area = pygame.Rect(0, 0, 0, 0)
        self.forwards_area = pygame.Rect(0, 0, 0, 0)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.blit(self.animated_background, (0, 0))
        self.screen.blit(self.background, (0, 0))
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button.
                        if self.play_area.collidepoint(event.pos):
                            app()
                        elif self.instructions_area.collidepoint(event.pos):
                            instructions_state = self.instructions(
                                instructions_state)
                        elif self.backwards_area.collidepoint(event.pos):
                            instructions_state = self.instructions_update(
                                instructions_state, -1)
                        elif self.forwards_area.collidepoint(event.pos):
                            instructions_state = self.instructions_update(
                                instructions_state, 1)
                        elif self.instruction_exit_area.collidepoint(event.pos):
                            self.main()
                        elif self.exit_area.collidepoint(event.pos):
                            done = True

            self.menu_animation(game_menu)
            self.screen.blit(game_menu, (int(screen_width / 2.35), 50))
            try:
                if self.instruction_state_boolean == True:
                    self.screen.blit(self.instructions_menu,
                                     (int(screen_width / 3.75), 200))
            except:
                pass
            pygame.display.flip()
            fpsControl.tick(60)
        pygame.quit()
        sys.exit()

    def menu_animation(self, game_menu):
        if self.animation_reverse == False:
            try:
                self.animation_state = self.animation_state + 1
                self.animated_background = pygame.image.load(
                    ".//Assets//Start Menu//frame" + str(self.animation_state) + ".jpg")
            except pygame.error:
                self.animation_reverse = True
        else:
            try:
                self.animation_state = self.animation_state - 1
                self.animated_background = pygame.image.load(
                    ".//Assets//Start Menu//frame" + str(self.animation_state) + ".jpg")
            except pygame.error:
                self.animation_reverse = False
        self.animated_background = pygame.transform.scale(
            self.animated_background, (1920, 1080))
        self.background.blit(self.animated_background, (0, 0))
        self.screen.blit(self.background, (0, 0))

    def instructions(self, instructions_state):
        self.instruction_state_boolean = True
        self.instructions_menu = pygame.image.load(
            ".//Assets//Start Menu//Instructions//frame" + str(instructions_state) + ".png")
        x1, y1, x2, y2 = 845, 800, 1135, 850  # Exit
        self.instruction_exit_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        x1, y1, x2, y2 = 1160, 800, 1200, 850  # back one
        self.backwards_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        x1, y1, x2, y2 = 1280, 800, 1320, 850  # forward one
        self.forwards_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        return instructions_state

    def instructions_update(self, instructions_state, instructions_position):
        try:
            self.instructions_menu = pygame.image.load(
                ".//Assets//Start Menu//Instructions//frame" + str(instructions_state + instructions_position) + ".png")
            instructions_state = instructions_state + instructions_position
        except pygame.error:
            self.instructions_menu = pygame.image.load(
                ".//Assets//Start Menu//Instructions//frame" + str(instructions_state) + ".png")
        return instructions_state


# Main Application
class app():
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.x = 200
        self.y = 430
        self.player_drawn_cards = []
        self.player_value = 0
        self.computer_drawn_cards = []
        self.drawn_cards_positions = []
        self.computer_value = 0
        self.current_x = 430
        self.current_y = 710
        self.main()

    def main(self):
        table = pygame.image.load(".//Assets//table.jpg")
        table = pygame.transform.scale(table, (1920, 1050))
        x1, y1, x2, y2 = 190, 420, 300, 630
        self.card_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        x1, y1, x2, y2 = 430, 460, 840, 600
        self.stand_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        self.play_again_area = pygame.Rect(0, 0, 0, 0)
        self.exit_area = pygame.Rect(0, 0, 0, 0)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.blit(table, (0, 0))
        self.screen.blit(self.background, (0, 0))
        self.player_draw_a_card()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button.
                        if self.card_area.collidepoint(event.pos):
                            self.player_draw_a_card()
                        elif self.stand_area.collidepoint(event.pos):
                            self.card_area = pygame.Rect(0, 0, 0, 0)
                            self.stand_area = pygame.Rect(0, 0, 0, 0)
                            self.player_stick()
                        elif self.play_again_area.collidepoint(event.pos):
                            self.__init__()
                        elif self.exit_area.collidepoint(event.pos):
                            start_menu()
            pygame.display.flip()
            fpsControl.tick(60)
        pygame.quit()
        sys.exit()

    def player_draw_a_card(self):
        card_value, card_picked = card.create_card()
        self.player_drawn_cards.append(card_picked)
        self.player_value = self.player_value + int(card_value)
        self.drawn_cards_positions.append(self.current_x)  # X
        self.drawn_cards_positions.append(self.current_y)  # Y
        self.card_animation(self.player_drawn_cards)
        self.x = 200
        self.y = 430
        self.current_x = self.current_x + 220
        for x in self.player_drawn_cards:
            if "A" in x:
                if self.player_value <= 10:
                    self.player_value = self.player_value + 11
        if self.player_value <= 15:
            self.player_draw_a_card()
        elif self.player_value > 21:
            self.gamestate_handler("Player bust")

    def card_animation(self, drawn_cards):
        final_x, final_y = self.drawn_cards_positions[-2], self.drawn_cards_positions[-1]
        displacement_x = ((final_x - self.x) / 100) * 2
        displacement_y = ((final_y - self.y) / 100) * 2
        counter = 0
        while counter != 51:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(hidden_card, (int(self.x), int(self.y)))
            self.x = self.x + displacement_x
            self.y = self.y + displacement_y
            pygame.display.update()
            counter = counter + 1
        time.sleep(0.1)
        reveal_card = pygame.image.load(
            ".//Assets//Revealed Card//" + drawn_cards[-1] + ".png")
        reveal_card = pygame.transform.scale(reveal_card, (180, 200))
        self.background.blit(reveal_card, (final_x, final_y))
        self.screen.blit(self.background, (0, 0))

    def player_stick(self):
        self.current_x = 430
        self.current_y = 135
        ace_state = 0
        self.computer_draw_a_card()
        amt_player_cards = int(len(self.player_drawn_cards) / 2)
        amt_computer_cards = int(len(self.computer_drawn_cards) / 2)
        print(self.player_value)
        print(self.player_drawn_cards)
        print(self.computer_drawn_cards)
        print(self.computer_value)

        if self.computer_value > 21:
            self.gamestate_handler("Dealer bust")
        elif amt_player_cards > 4:
            self.gamestate_handler("You win")
        elif amt_computer_cards > 4 or self.computer_value >= self.player_value:
            self.gamestate_handler("You lose")
        else:
            self.gamestate_handler("You win")

    def computer_draw_a_card(self):
        card_value, card_picked = card.create_card()
        self.computer_drawn_cards.append(card_picked)
        self.computer_value = self.computer_value + int(card_value)
        self.drawn_cards_positions.append(self.current_x)  # X
        self.drawn_cards_positions.append(self.current_y)  # Y
        self.card_animation(self.computer_drawn_cards)
        self.x = 200
        self.y = 430
        self.current_x = self.current_x + 220
        for x in self.computer_drawn_cards:
            if "A" in x:
                if self.computer_value >= 10:
                    self.computer_value = self.computer_value + 11
        if self.computer_value <= 16:
            self.computer_draw_a_card()

    def gamestate_handler(self, filename):
        self.card_area = pygame.Rect(0, 0, 0, 0)
        self.stand_area = pygame.Rect(0, 0, 0, 0)
        x1, y1, x2, y2 = 720, 515, 1200, 675
        self.play_again_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        x1, y1, x2, y2 = 720, 705, 1200, 800
        self.exit_area = pygame.Rect(x1, y1, (x2-x1), (y2-y1))
        gamestate = pygame.image.load(
            ".//Assets//Game State//" + filename + ".jpg")
        gamestate = pygame.transform.scale(gamestate, (1920, 1050))
        self.screen.blit(gamestate, (0, 0))


start_menu()
