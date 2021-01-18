#!/usr/bin/env python3

from random import randrange
import random
import pygame, sys
from pygame.locals import *
import string

pygame.font.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#dimensiuni pentru fereastra de Menu si Bambilici
WIDTH = 600
HEIGHT = 400

#dimensiuni pentru fereastra de Hangman si Piatra-Hartie-Foarfeca
WIDTH_H = 1300
HEIGHT_H = 700


class GameObject:
    def __init__(self, position):
        self.position = position

    def input(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Menu(GameObject):
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Menu')

        #butoanele de accesare ale paginilor jocurilor
        self.bambilici_rect = pygame.Rect(100, 100, 100, 80)
        self.hangman_rect = pygame.Rect(250, 200, 100, 80)
        self.piatra_hartie_foarfeca_rect = pygame.Rect(400, 300, 100, 80)

        self.color = pygame.Color('lightblue3')


    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #la deschiderea unei noi ferestre cea curenta se inchide
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.bambilici_rect.collidepoint(event.pos):
                    bambilici = Bambilici()
                    bambilici.run()
                    pygame.quit()
                    sys.exit()
                if self.hangman_rect.collidepoint(event.pos):
                    hangman = Hangman()
                    hangman.run()
                    pygame.quit()
                    sys.exit()
                if self.piatra_hartie_foarfeca_rect.collidepoint(event.pos):
                    piatra_hartie_foarfeca = PiatraHartieFoarfeca()
                    piatra_hartie_foarfeca.run()
                    pygame.quit()
                    sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
    def update(self):
        pass

    def draw(self):
        self.window.fill(WHITE)

        #fonturi
        self.font = pygame.font.SysFont(None, 50)
        self.games_font = pygame.font.SysFont(None, 30)

        #titlul
        self.img = self.font.render('Nostalgia Games', True, BLACK)
        self.window.blit(self.img, (150, 20))


        #butoanele pentru fiecare joc cat si o prezentare a jocurilor
        pygame.draw.rect(self.window, self.color, self.bambilici_rect)
        self.button_b = self.games_font.render('Bambilici', True, BLACK)
        self.window.blit(self.button_b, (self.bambilici_rect.x, self.bambilici_rect.y + 30))

        self.description_b = self.games_font.render('Un clasic al copilariei', True, BLACK)
        self.window.blit(self.description_b, (self.bambilici_rect.x + 120, self.bambilici_rect.y + 30))


        pygame.draw.rect(self.window, self.color, self.hangman_rect)
        self.button_h = self.games_font.render('Hangman', True, BLACK)
        self.window.blit(self.button_h, (self.hangman_rect.x, self.hangman_rect.y + 30))

        self.description_h = self.games_font.render('O reinventare', True, BLACK)
        self.window.blit(self.description_h, (60, self.hangman_rect.y + 30))
        self.description_h = self.games_font.render('a jocului', True, BLACK)
        self.window.blit(self.description_h, (400, self.hangman_rect.y + 30))


        pygame.draw.rect(self.window, self.color, self.piatra_hartie_foarfeca_rect)
        self.button_t = self.games_font.render('P - H - F', True, BLACK)
        self.window.blit(self.button_t, (self.piatra_hartie_foarfeca_rect.x + 10, self.piatra_hartie_foarfeca_rect.y + 30))
        self.description_t = self.games_font.render('Piatra - Hartie - Foarfeca', True, BLACK)
        self.window.blit(self.description_t, (150, self.piatra_hartie_foarfeca_rect.y + 30))

        pygame.display.update()

        pygame.time.Clock().tick(60)

        

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()


class PiatraHartieFoarfeca(GameObject):
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH_H, HEIGHT_H))
        pygame.display.set_caption('Piatra Hartie Foarfeca')
        
        #loc pe fereastra la care raportam celelate puncte
        self.input_rect = pygame.Rect(130, 100, 100, 100)

        self.base_font = pygame.font.Font(None, 32)
        self.big_font = pygame.font.Font(None, 50)
        self.ultra_big_font = pygame.font.Font(None, 100)

        #atribuim o culoare pentru fiecare button, deoarece acestea
        #isi schimba culoare in urma interactiunii cu ele
        #cel al jucatorului devine verde
        #cel al programului devine rosu
        self.color = pygame.Color('lightblue3')
        self.color1 = self.color
        self.color1_bot = self.color
        self.color2 = self.color
        self.color2_bot = self.color
        self.color3 = self.color
        self.color3_bot = self.color
        self.text_player = "USER"
        self.text_bot = "BOT"

        #putem apasa un button doar o singura data
        self.active = True

        #in final outputul se rezuma la compararea a trei stari
        #codificate 0, 1 si 2
        self.ai_choice = ''
        self.player_choice = ''

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #apasarea unui button se inregistreaza in variabila mai sus mentionata
            #dupa care utilizatorul nu mai poate interactiona cu butoanele
            #tot aici, in urma apasarii unui button programul da un raspuns
            #prin alegerea aleatoare a unui output dintre cele 3 stari
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.active == True:
                    if self.button_h_player.collidepoint(event.pos):
                        self.player_choice = 0
                        self.color1 = GREEN
                        self.active = False
                        self.ai_choice = randrange(2)
                        if self.ai_choice == 0:
                            self.color1_bot = RED
                        elif self.ai_choice == 1:
                            self.color2_bot = RED
                        else:
                            self.color3_bot = RED
                    elif self.button_p_player.collidepoint(event.pos):
                        self.player_choice = 1
                        self.color2 = GREEN
                        self.active = False
                        self.ai_choice = randrange(2)
                        if self.ai_choice == 0:
                            self.color1_bot = RED
                        elif self.ai_choice == 1:
                            self.color2_bot = RED
                        else:
                            self.color3_bot = RED
                    elif self.button_f_player.collidepoint(event.pos):
                        self.player_choice = 2
                        self.color3 = GREEN
                        self.active = False
                        self.ai_choice = randrange(2)
                        if self.ai_choice == 0:
                            self.color1_bot = RED
                        elif self.ai_choice == 1:
                            self.color2_bot = RED
                        else:
                            self.color3_bot = RED

            #la inchiderea ferestrei revenim in pagina de menu
            #indeplineste atat functionalitatea de resetare a jocului
            #cat si revenire pe pagina de menu
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu = Menu()
                    menu.run()
                    pygame.quit()
                    sys.exit()

    def update(self):
        pass

    def draw(self):
        self.window.fill(BLACK) 
        # o interfata contine imaginea sugestiva cu una din cele 3 optiuni ale jocului
        # buttonul din stanga corespunde playerului, in timp ce buttonul din dreapta
        # corespunde calculatorului, iar coloratia lor va specifica care a fost selectat

        #interfata pentru hartie
        hartie = pygame.image.load("hartie")
        hartie = pygame.transform.scale(hartie, (250, 250))
        self.window.blit(hartie, self.input_rect)

        self.button_h_player = pygame.Rect(self.input_rect.x, self.input_rect.y + 300, 100, 100)
        pygame.draw.rect(self.window, self.color1, self.button_h_player)
        text_surface = self.big_font.render(self.text_player, True, BLACK)
        self.window.blit(text_surface, (self.button_h_player.x + 2, self.button_h_player.y + 35))

        self.button_h_ai = pygame.Rect(self.input_rect.x + 150, self.input_rect.y + 300, 100, 100)
        pygame.draw.rect(self.window, self.color1_bot, self.button_h_ai)
        text_surface = self.big_font.render(self.text_bot, True, BLACK)
        self.window.blit(text_surface, (self.button_h_ai.x + 15, self.button_h_ai.y + 35))

        #interfata pentru piatra
        piatra = pygame.image.load("piatra.jpeg")
        piatra = pygame.transform.scale(piatra, (250, 250))
        self.window.blit(piatra, (self.input_rect.x + 400, self.input_rect.y))

        self.button_p_player = pygame.Rect(self.input_rect.x + 400, self.input_rect.y + 300, 100, 100)
        pygame.draw.rect(self.window, self.color2, self.button_p_player)
        text_surface = self.big_font.render(self.text_player, True, BLACK)
        self.window.blit(text_surface, (self.button_p_player.x + 2, self.button_p_player.y + 35))

        self.button_p_ai = pygame.Rect(self.input_rect.x + 550, self.input_rect.y + 300, 100, 100)
        pygame.draw.rect(self.window, self.color2_bot, self.button_p_ai)
        text_surface = self.big_font.render(self.text_bot, True, BLACK)
        self.window.blit(text_surface, (self.button_p_ai.x + 15, self.button_p_ai.y + 35))

        #interfata pentru foarfeca
        foarfeca = pygame.image.load("foarfeca.png")
        foarfeca = pygame.transform.scale(foarfeca, (250, 250))
        self.window.blit(foarfeca, (self.input_rect.x + 800, self.input_rect.y))

        self.button_f_player = pygame.Rect(self.input_rect.x + 800, self.input_rect.y + 300, 100, 100)
        pygame.draw.rect(self.window, self.color3, self.button_f_player)
        text_surface = self.big_font.render(self.text_player, True, BLACK)
        self.window.blit(text_surface, (self.button_f_player.x + 2, self.button_f_player.y + 35))

        self.button_f_ai = pygame.Rect(self.input_rect.x + 950, self.input_rect.y + 300, 100, 100)
        pygame.draw.rect(self.window, self.color3_bot, self.button_f_ai)
        text_surface = self.big_font.render(self.text_bot, True, BLACK)
        self.window.blit(text_surface, (self.button_f_ai.x + 15, self.button_f_ai.y + 35))


        #dupa ce alegerile au fost facute se stabileste mesajul pe care il afisam pe fereastra si care semnifica rezultatul jocului
        #victorie
        if (self.player_choice == 0 and self.ai_choice == 1) or (self.player_choice == 1 and self.ai_choice == 2) or (self.player_choice == 2 and self.ai_choice == 0):
            text_surface = self.ultra_big_font.render("You win", True, GREEN)
            self.window.blit(text_surface, (500, 550))
        #infrangere
        elif (self.player_choice == 0 and self.ai_choice == 2) or (self.player_choice == 1 and self.ai_choice == 0) or (self.player_choice == 2 and self.ai_choice == 1):
            text_surface = self.ultra_big_font.render("You lose", True, RED)
            self.window.blit(text_surface, (500, 550))
        #egalitate
        elif (self.player_choice == 0 and self.ai_choice == 0) or (self.player_choice == 1 and self.ai_choice == 1) or (self.player_choice == 2 and self.ai_choice == 2):
            text_surface = self.ultra_big_font.render("DRAW", True, WHITE)
            self.window.blit(text_surface, (500, 550))

        

        pygame.display.update()

        pygame.time.Clock().tick(60)

        

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw() 

class Hangman(GameObject):
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH_H, HEIGHT_H))
        pygame.display.set_caption('Spanzuratoarea')

        self.text = ''
        self.guess_me = ''

        self.base_font = pygame.font.Font(None, 32)
        self.ultra_big_font = pygame.font.Font(None, 100)

        self.input_rect = pygame.Rect(200, 200, 140, 32)

        self.color_active = RED
        self.color_passive = pygame.Color('grey15')
        self.color = self.color_passive
        

        # cuvantul este citit dintr-un fisier unde se afla cuvinte pe prima linie separate prin spatii albe
        with open("hangman_input.txt") as file:
            lines = file.readlines()

        words = lines[randrange(len(lines))].strip("\n")
        words = words.split()
        
        self.guess_me = words[randrange(len(words))]
        print(self.guess_me)

        #lista de tupluri (litera, casuta litera, ne/ghicit)
        self.letters= []

        for i in range(len(self.guess_me)):
            self.letters.append( (self.guess_me[i], pygame.Rect(10 + 100 * i, 100, 50 , 50), False) )
    
        alphabet_list = list(string.ascii_lowercase)

        #randurile de litere pe care utilizatorul le va apasa pentru a ghici
        #lista formata din tupluri de forma (litera, casuta litera, culoare)
        self.alphabet_buttons_row1 = []
        self.alphabet_buttons_row2 = []
        self.alphabet_buttons_row3 = []
        for i in range(len(alphabet_list)):
            if 0 <= i < len(alphabet_list) / 3:
                 self.alphabet_buttons_row1.append( (alphabet_list[i], pygame.Rect(10 + 100 * i, 500, 50, 50), self.color) )
            if len(alphabet_list) / 3 <= i < 2 * len(alphabet_list) / 3:
                 self.alphabet_buttons_row2.append( (alphabet_list[i], pygame.Rect(60 + 100 * (i - 9), 550, 50, 50), self.color) )
            if 2 * len(alphabet_list) / 3 < i <= len(alphabet_list) :
                 self.alphabet_buttons_row3.append( (alphabet_list[i], pygame.Rect(110 + 100 * (i - 18), 600, 50, 50), self.color) )

        #putem sa ghicim atata timp cat nu am completat spanzuratoarea
        self.active = True
        self.count = 0

                

    def input(self):
        #pentru inchiderea meniului
        for event in pygame.event.get():
            #activarea buttonului de inchidere
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #prin escape revenim la pagina anterioara (de menu)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu = Menu()
                    menu.run()
                    pygame.quit()
                    sys.exit()

            # de vreme ce tuplurile sunt imutabile si listele nu, cream un nou tuplu(cu campul modificat), 
            # pe care sa il adaugam la indicele tuplului vechi
            if event.type == MOUSEBUTTONDOWN and self.active == True:
                
                #daca casuta contine litera din cuvant aceasta va deveni verde
                #in caz contrar aceasta va deveni rosie
                
                #daca jucatorul apasa pe o litera, se verifica daca aceasta este in cod si i se modifica
                #variabila de afisare din tuplu
                     
                #prima linie
                for i in range(len(self.alphabet_buttons_row1)):
                    if self.alphabet_buttons_row1[i][1].collidepoint(event.pos):
                        if self.alphabet_buttons_row1[i][0] in self.guess_me:
                            for j in range(len(self.letters)):
                                if self.alphabet_buttons_row1[i][0] == self.letters[j][0]:
                                    aux_tuple = (self.letters[j][0], self.letters[j][1], True)
                                    self.letters[j] = aux_tuple
                            aux_tuple = (self.alphabet_buttons_row1[i][0], self.alphabet_buttons_row1[i][1], GREEN)
                            self.alphabet_buttons_row1[i] = aux_tuple
                        else:
                            self.count += 1
                            aux_tuple = (self.alphabet_buttons_row1[i][0], self.alphabet_buttons_row1[i][1], RED)
                            self.alphabet_buttons_row1[i] = aux_tuple


                #a doua linie    
                for i in range(len(self.alphabet_buttons_row2)):
                    if self.alphabet_buttons_row2[i][1].collidepoint(event.pos):
                        if self.alphabet_buttons_row2[i][0] in self.guess_me:
                            for j in range(len(self.letters)):
                                if self.alphabet_buttons_row2[i][0] == self.letters[j][0]:
                                    aux_tuple = (self.letters[j][0], self.letters[j][1], True)
                                    self.letters[j] = aux_tuple
                            aux_tuple = (self.alphabet_buttons_row2[i][0], self.alphabet_buttons_row2[i][1], GREEN)
                            self.alphabet_buttons_row2[i] = aux_tuple
                        else:
                            self.count += 1
                            aux_tuple = (self.alphabet_buttons_row2[i][0], self.alphabet_buttons_row2[i][1], RED)
                            self.alphabet_buttons_row2[i] = aux_tuple

                # a treia linie
                for i in range(len(self.alphabet_buttons_row3)):
                    if self.alphabet_buttons_row3[i][1].collidepoint(event.pos):
                        if self.alphabet_buttons_row3[i][0] in self.guess_me:
                            for j in range(len(self.letters)):
                                if self.alphabet_buttons_row3[i][0] == self.letters[j][0]:
                                    aux_tuple = (self.letters[j][0], self.letters[j][1], True)
                                    self.letters[j] = aux_tuple
                            aux_tuple = (self.alphabet_buttons_row3[i][0], self.alphabet_buttons_row3[i][1], GREEN)
                            self.alphabet_buttons_row3[i] = aux_tuple
                        else:
                            self.count += 1
                            aux_tuple = (self.alphabet_buttons_row3[i][0], self.alphabet_buttons_row3[i][1], RED)
                            self.alphabet_buttons_row3[i] = aux_tuple

                


    def update(self):
        pass

    def draw(self):
        self.window.fill(BLACK)

        #desenarea casutelor cu literele cuvantului, afisam litera in aceasta doar daca ea
        #a fost ghicita
        for i in range(len(self.letters)):
            pygame.draw.rect(self.window, self.color, self.letters[i][1])
            text_surface = self.base_font.render(self.letters[i][0],True, WHITE)
            if self.letters[i][2] == True:
                self.window.blit(text_surface, (self.letters[i][1].x + 20, self.letters[i][1].y + 15))

        #afisarea casutelor cu literele din alfabet pe care utilizatorul le va folosi sa ghiceasca cuvantul
        for i in range(len(self.alphabet_buttons_row1)):
            pygame.draw.rect(self.window, self.alphabet_buttons_row1[i][2], self.alphabet_buttons_row1[i][1])
            text_surface = self.base_font.render(self.alphabet_buttons_row1[i][0], True, WHITE)
            self.window.blit(text_surface, (self.alphabet_buttons_row1[i][1].x + 20, self.alphabet_buttons_row1[i][1].y + 15))

        for i in range(len(self.alphabet_buttons_row2)):
            pygame.draw.rect(self.window, self.alphabet_buttons_row2[i][2], self.alphabet_buttons_row2[i][1])
            text_surface = self.base_font.render(self.alphabet_buttons_row2[i][0], True, WHITE)
            self.window.blit(text_surface, (self.alphabet_buttons_row2[i][1].x + 20, self.alphabet_buttons_row2[i][1].y + 15))

        for i in range(len(self.alphabet_buttons_row3)):
            pygame.draw.rect(self.window, self.alphabet_buttons_row3[i][2], self.alphabet_buttons_row3[i][1])
            text_surface = self.base_font.render(self.alphabet_buttons_row3[i][0], True, WHITE)
            self.window.blit(text_surface, (self.alphabet_buttons_row3[i][1].x + 20, self.alphabet_buttons_row3[i][1].y + 15))
 

        # desenarea partilor omului, acestea apar treptat
        #in functie de cate incercari gresite avem
        # capul si corpul
        if self.count >= 1:
            pygame.draw.circle(self.window, WHITE, [1120, 200], 40, 0)
            pygame.draw.line(self.window, WHITE, [1120, 240], [1120, 490], 5)
        
        # mainile
        if self.count >= 2:
            pygame.draw.line(self.window, WHITE, [1120, 290], [1020, 370], 5)
            pygame.draw.line(self.window, WHITE, [1120, 290], [1220, 370], 5)
        
        # picioarele
        if self.count >= 3:
            self.active = False
            pygame.draw.line(self.window, WHITE, [1120, 490], [1020, 610], 5)
            pygame.draw.line(self.window, WHITE, [1120, 490], [1220, 610], 5)
            
            
        #stabilim conditia de victorie daca toate literele au fost afisate
        #si daca contorul de incercari este mai mic decat maximul permis(3)
        #atat in cazul victoriei cat si al esecului afisam un mesaj sugestiv
        win_condition = True
        if self.count < 3:
            for i in range(len(self.letters)):
                if self.letters[i][2] != True:
                    win_condition = False
        else:
            text_surface = self.ultra_big_font.render("You lose", True, RED)
            self.window.blit(text_surface, (200, 300))

        if win_condition == True and self.count < 3:
            text_surface = self.ultra_big_font.render("You win", True, GREEN)
            self.window.blit(text_surface, (200, 300))
            self.active = False

        pygame.display.update()
        pygame.time.Clock().tick(60)

        

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()


class Bambilici(GameObject):
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Bambilici')
        
        #textul pe care il introduce jucatorul
        self.text = ''
        #textul pe care il proceseaza programul
        self.text_b= ''
        self.base_font = pygame.font.Font(None, 32)
        self.big_font = pygame.font.Font(None, 50)

        #dreptunghiul in care vom introduce inputul
        self.input_rect = pygame.Rect(150, 150, 140, 32)
        self.color_active = pygame.Color('lightblue3')
        self.color_passive = pygame.Color('grey15')
        self.color = self.color_passive
        #variabila cu care decidem daca se accepta input sau nu
        self.active = False

        #o alegere a fost facuta asa ca programul trebuie sa ofere un raspuns
        self.choice = False
        #cazul in care inputul nu este considerat valid 
        self.invalid_input = False

    def input(self):
        #pentru inchiderea meniului
        for event in pygame.event.get():
            #activarea buttonului de inchidere
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_rect.collidepoint(event.pos):
                    self.text = ""
                    self.active = True
                    self.choice = False
                    self.invalid_input = False
            
            #programul va procesa inputul si va verifica daca acesta este
            #numeric, in cazul in care acesta este il va procesa si va returna
            #numarul imediat mai mare, astfel nefiind posibil sa castigi acest joc
            #in cazul in care inputul nu este numeric utilizatorul este instiintat
            #in legatura cu asta
            if event.type == KEYDOWN:
                if self.active == True:
                    if event.key == K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.key == K_TAB:
                        self.active = False
                        if self.text.isnumeric():
                            self.choice = True
                            self.text_b = str(int(self.text) + 1)
                        else:
                            self.invalid_input = True
                    else :
                        self.text += event.unicode
                else:
                    if event.key == K_ESCAPE:
                        menu = Menu()
                        menu.run()
                        pygame.quit()
                        sys.exit()

    def update(self):
        pass

    def draw(self):
        self.window.fill(BLACK)

        #cand putem scrie in dreptunghi ne dorim sa aiba o alta culoare
        #fata de atunci cand nu putem scrie
        if self.active:
            self.color = self.color_active
        else :
            self.color = self.color_passive
        #dreptunghiul in care scriem
        pygame.draw.rect(self.window, self.color, self.input_rect, 2)

        #textul propriu-zis scris in dreptunghi
        text_surface = self.base_font.render(self.text, True, WHITE)
        self.window.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

        #dreptunghiul isi actualizeaza parametrul width pentru a putea "imbraca" textul
        self.input_rect.w = text_surface.get_width() + 10

        #texte pentru a crea introduce utilizatorul in joc
        title = self.big_font.render('Bun venit in lumea lui Bambilici!', True, WHITE)
        self.window.blit(title, (40, 10))

        text_surface = self.base_font.render('Gandeste-te la un numar mai mare ', True, WHITE)
        self.window.blit(text_surface, (100, 50))
        text_surface = self.base_font.render('decat cel la care ma gandesc eu!!!', True, WHITE)
        self.window.blit(text_surface, (150, 80))

        text_surface = self.base_font.render('Alege ;) ', True, WHITE)
        self.window.blit(text_surface, (self.input_rect.x - 100, self.input_rect.y + 5))

        #in urma detectarii unui inpui, programul va afisa un output in fereastra
        if self.choice == True:
            text_surface = self.base_font.render('Bambilici: ', True, WHITE)
            self.window.blit(text_surface, (self.input_rect.x  + 150, self.input_rect.y + 5))

            text_surface = self.base_font.render(self.text_b, True, WHITE)
            self.window.blit(text_surface, (self.input_rect.x  + 270, self.input_rect.y + 5))

        #de vreme ce nu putem castiga acest joc, avem un singur prompt de outcome
        if self.choice == True:
            text_surface = self.big_font.render('HAHAHAHA ! ', True, RED)
            self.window.blit(text_surface, (150, 200))
            text_surface = self.big_font.render('Bambilici ramane de  ', True, RED)
            self.window.blit(text_surface, (100, 250))
            text_surface = self.big_font.render('NEINVINS !!!! ', True, RED)
            self.window.blit(text_surface, (150, 300))
        #afisare pentru cazul in care inputul este invalid
        elif self.invalid_input == True:
            text_surface = self.big_font.render('HAHAHAHA ! ', True, RED)
            self.window.blit(text_surface, (150, 200))
            text_surface = self.big_font.render('Nu stii nici macar', True, RED)
            self.window.blit(text_surface, (100, 250))
            text_surface = self.big_font.render('ce este un numar natural', True, RED)
            self.window.blit(text_surface, (150, 300))
        
        pygame.display.update()
        pygame.time.Clock().tick(60)

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()



if __name__ == "__main__":
    menu = Menu()
    menu.run()