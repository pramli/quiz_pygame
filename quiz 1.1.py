import pygame
from pygame_functions import *


pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
light_red = (255, 102, 102)
green = (0, 200, 0)
light_green = (144, 238, 144)
blue = (0, 100, 250)
light_blue = (100, 200, 255)
yellow = (255, 255, 0)
light_yellow =(255, 250, 205)

display_width = 1200
display_height = 700

button_width = 100
button_height = 50



correct_answer_sound = pygame.mixer.Sound("my_man.wav")
wrong_answer_sound = pygame.mixer.Sound("nope.wav")
pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play(1)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("pop quiz")
icon = pygame.image.load("pq.bmp")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
fps = 30

smallfont = pygame.font.SysFont("leelawadeeuisemilight", 40)
medfont = pygame.font.SysFont("leelawadeeuisemilight", 100)
largefont = pygame.font.SysFont("leelawadeeuisemilight", 120)


points = 0

def score(points):
    text = smallfont.render("score:  " + str(points), True, red)
    gameDisplay.blit(text, [0,0])


def text_objects(text, color, size):
    global textSurface
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "med":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def correct_answer():
    global points
    points += 10
    gameDisplay.fill(light_blue)
    question_message("correct!", blue, 0, size="med")
    pygame.display.update()
    pygame.mixer.Sound.play(correct_answer_sound)
    pygame.time.delay(1500)

def wrong_answer():
    gameDisplay.fill(light_red)
    question_message("wrong answer :(", red, -0, size="med")
    pygame.display.update()
    pygame.mixer.Sound.play(wrong_answer_sound)
    pygame.time.delay(1500)

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + buttonwidth/2), buttony + buttonheight/2)
    gameDisplay.blit(textSurf, textRect)

def intro_message(msg, color, y_displace=0, size = "small"):
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/3, display_height/3])
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def question_message(msg, color, y_displace=0, size="small"):
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/3, display_height/3])
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def answer_button(text, color, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "answer_1":
                correct_answer()
                question_2()
            if action == "answer_2":
                wrong_answer()
                question_2()
            if action == "answer_3":
                wrong_answer()
                question_2()
            if action == "answer_4":
                wrong_answer()
                question_2()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def question_1():
    q1 = True
    while q1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)

        # pygame.draw.rect(gameDisplay, light_blue, (50, 120, 1100, 300))
        question_message("question number 1: ", blue, -160, size="med")
        question_message("what color is the sky?", blue, -20, size="med")

        wordbox = makeTextBox(10, 80, 300, 0, "enter your answer", 10, 40)
        showTextBox(wordbox)
        entry = textBoxInput(wordbox)

        answer_button("it's blue", black, 50, 500, 200, 100, blue, light_blue, action= "answer_1")
        answer_button("it's yellow", black, 350, 500, 200, 100, yellow, light_yellow, action= "answer_2")
        answer_button("it's green", black, 650, 500, 200, 100, green, light_green, action= "answer_3")
        answer_button("it's red", black, 950, 500, 200, 100, red, light_red, action="answer_4")

        score(points)
        pygame.display.update()
        clock.tick(8)



def answer_button_2(text, color, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "answer_1":
                wrong_answer()
                question_3()
            if action == "answer_2":
                correct_answer()
                question_3()
            if action == "answer_3":
                wrong_answer()
                question_3()
            if action == "answer_4":
                wrong_answer()
                question_3()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def question_2():
    q2 = True
    while q2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        # pygame.draw.rect(gameDisplay, light_yellow, (50, 120, 1100, 300))
        question_message("question number 2: ", yellow, -160, size="med")
        question_message("what color is the sun?", yellow, -20, size="med")

        answer_button_2("it's blue", black, 50, 500, 200, 100, blue, light_blue, action= "answer_1")
        answer_button_2("it's yellow", black, 350, 500, 200, 100, yellow, light_yellow, action= "answer_2")
        answer_button_2("it's green", black, 650, 500, 200, 100, green, light_green, action= "answer_3")
        answer_button_2("it's red", black, 950, 500, 200, 100, red, light_red, action="answer_4")

        score(points)
        pygame.display.update()
        clock.tick(8)

def answer_button_3(text, color, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "answer_1":
                wrong_answer()
                question_4()
            if action == "answer_2":
                wrong_answer()
                question_4()
            if action == "answer_3":
                correct_answer()
                question_4()
            if action == "answer_4":
                wrong_answer()
                question_4()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def question_3():
    q3 = True
    while q3:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        # pygame.draw.rect(gameDisplay, light_green, (50, 120, 1100, 300))
        question_message("question number 3: ", green, -160, size="med")
        question_message("what color is the grass?", green, -20, size="med")

        answer_button_3("it's blue", black, 50, 500, 200, 100, blue, light_blue, action= "answer_1")
        answer_button_3("it's yellow", black, 350, 500, 200, 100, yellow, light_yellow, action= "answer_2")
        answer_button_3("it's green", black, 650, 500, 200, 100, green, light_green, action= "answer_3")
        answer_button_3("it's red", black, 950, 500, 200, 100, red, light_red, action="answer_4")

        score(points)
        pygame.display.update()
        clock.tick(8)

def answer_button_4(text, color, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "answer_1":
                wrong_answer()
                end_screen()
            if action == "answer_2":
                wrong_answer()
                end_screen()
            if action == "answer_3":
                wrong_answer()
                end_screen()
            if action == "answer_4":
                correct_answer()
                end_screen()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def question_4():
    q4 = True
    while q4:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        # pygame.draw.rect(gameDisplay, light_red, (50, 120, 1100, 300))
        question_message("question number 4: ", red, -160, size="med")
        question_message("what color is an apple?", red, -20, size="med")

        answer_button_4("it's blue", black, 50, 500, 200, 100, blue, light_blue, action="answer_1")
        answer_button_4("it's yellow", black, 350, 500, 200, 100, yellow, light_yellow, action="answer_2")
        answer_button_4("it's green", black, 650, 500, 200, 100, green, light_green, action="answer_3")
        answer_button_4("it's red", black, 950, 500, 200, 100, red, light_red, action="answer_4")

        score(points)
        pygame.display.update()
        clock.tick(8)



def button(text, color, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "play":
                pygame.time.delay(1000)
                question_1()


    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)



def intro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        gameDisplay.fill(white)
        # new_box = textinput.TextInput()
        # user_answer = new_box.get_text()
        # if user_answer == "blue".lower():
        #     points +=3
        #     question_2()
        # else:
        #     question_1()
        intro_message("welcome to pop quiz", red, -60, size="large")
        intro_message("click the correct answer to win points", green, 60, size="small")


        button("play", black, 300, 500, 200, 100, blue, light_blue, action="play")
        button("quit", black, 700, 500, 200, 100, blue, light_blue, action="quit")

        score(points)
        pygame.display.update()
        clock.tick(8)

def end_screen():
    end_screen = True
    while end_screen:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    end_screen = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        gameDisplay.fill(white)
        intro_message("no more questions :(", blue, -220, size="med")
        intro_message("you scored " + str(points) + " points", red, -120, size="med")
        intro_message("do you wish to play again?", green, -20, size="med")


        button("yes", black, 300, 500, 200, 100, blue, light_blue, action="play")
        button("no", black, 700, 500, 200, 100, blue, light_blue, action="quit")


        pygame.display.update()
        clock.tick(8)



def game_loop():

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True


        gameDisplay.fill(white)

        # score(points)
        pygame.display.update()



    pygame.quit()
    quit()

intro()
game_loop()