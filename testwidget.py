import sys, pygame
from pygame.locals import *
import os
# Tillåter ANSI format file.txt att översätta svenska bokstäver åäö, kolla rad 45 codecs.
import codecs

os.getcwd()
os.chdir("C:\\Users\\map\\map\\map")
RES = 800, 500

# Huvud programmet startar
pygame.init()
screen = pygame.display.set_mode(RES)
background_day = pygame.image.load("yellow grapes.png").convert()
pygame.display.set_caption("Quiz")
font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 30)
black = 0,100,0
white = 255,255,255
cyan = 0,255,255
yellow = 255,255,0
purple = 255,0,255
green = 0,255,0
red = 255,0,0
slut_spel = False


class Quiz(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white,white,white,white]

        #läser filen
        f = open(filename, "r")
        quiz_data = f.readlines()
        f.close()
        codecs.open('pythonQuiz.txt', encoding='utf-8')

        #räknar och rensar fil data
        for text_line in quiz_data:
            self.data.append(text_line.strip())
            self.total += 1

    def show_fråga(self):
        screen.blit(background_day, (0, 0))
        print_text(font1, 210, 7, "QUIZ SPEL")
        print_text(font2, 110, 500-20, "Tryck på knapparna (1-4) för att svara", white)
        print_text(font2, 505, 5, "POÄNG", purple)
        print_text(font2, 550, 25, str(self.score), purple)


        #ger rätt svar från filen
        self.correct = int(self.data[self.current+5])
        
        #display frågan
        fråga = self.current // 6 + 1
        print_text(font1, 5, 80, "FRÅGA " + str(fråga))
        print_text(font2, 20, 120, self.data[self.current], yellow)

        # korrekt svar text
        if self.scored:
            self.colors = [white,white,white,white]
            self.colors[self.correct-1] = green
            print_text(font1, 230, 380, "KORREKT!", green)
            print_text(font2, 170, 420, "Tryck På Enter För Att Fortsätta", green)
        elif self.failed:
            self.colors = [white,white,white,white]
            self.colors[self.wronganswer-1] = red
            self.colors[self.correct-1] = green
            print_text(font1, 220, 380, "FEL!", red)
            print_text(font2, 170, 420, "Tryck På Enter För Att Fortsätta", red)

        #display svar
        print_text(font1, 5, 170, "SVAR")
        print_text(font2, 20, 210, "1 - " + self.data[self.current+1], self.colors[0])
        print_text(font2, 20, 240, "2 - " + self.data[self.current+2], self.colors[1])
        print_text(font2, 20, 270, "3 - " + self.data[self.current+3], self.colors[2])
        print_text(font2, 20, 300, "4 - " + self.data[self.current+4], self.colors[3])

    def handle_input(self,number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.wronganswer = number
# spela igen funktion, tryck j för ja tryck n för nej
    def spela_igen(self,char):
        if char == 'j':
            self.current = 0
        if char == 'n':
            sys.exit()
# nästa fråga funktion
    def nästa_fråga(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white,white,white,white]
            self.current += 6
            if self.current >= self.total:
                return True
            else:
                return False

    def spelet_är_över(self):
        screen.blit(background_day, (0, 0))
        print_text(font1, 100, 100, "SPELET ÄR ÖVER", white)
        print_text(font2, 20, 240, "Vill Du Spela Igen? (J/N)", white)

def print_text(font, x, y, text, color=(255,255,255), shadow=True):
    if shadow:
        imgText = font.render(text, True, (0,0,0))
        screen.blit(imgText, (x-2,y-2))
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    

#ladda upp filen med frågor/svar
quiz = Quiz("pythonquiz.txt")

#för frågor loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                  quiz.handle_input(1)
            elif event.key == pygame.K_2:
                quiz.handle_input(2)
            elif event.key == pygame.K_3:
                quiz.handle_input(3)
            elif event.key == pygame.K_4:
                quiz.handle_input(4)
            elif event.key == pygame.K_RETURN:
                slut_spel = quiz.nästa_fråga()
            if slut_spel:
                quiz.spelet_är_över()
                quiz.current = 0
                if event.key == pygame.K_j:
                    slut_spel = False
                elif event.key == pygame.K_n:
                    sys.exit()    

    if not slut_spel:
        screen.fill((0,0,200))
        quiz.show_fråga()
    
    #updatera display
    pygame.display.update()
