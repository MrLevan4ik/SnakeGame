import pygame as pg  # подключение библиотек
import random

#import buttons

pg.init()  # включение пайгейма

version = "1.0.0"  # Версия игры
author = "LEVAN"  # Автор игры
lang = "en" # язык ru или en 

block_size = 20  # размер одного блока

screen = pg.display.set_mode((block_size * 40, block_size * 30))  # создание окошка
pg.display.set_caption(f"Snake {version}")

cheat_mode = False

if cheat_mode == True:
    pg.display.set_caption(f"Snake {version}, cheat={cheat_mode}")

fps = 5  # Кол-во кадров в секунду
clock = pg.time.Clock()  # специальный счётчик для фпс

# начальные координаты для змейки
start_x = 3 * block_size
start_y = 4 * block_size

snake = []  # создаём пустой список, куда потом положим блоки змейки

# Как будет работать змейка
for i in range(1, 4):
    new_block = [start_x + block_size * i, start_y]
    snake.append(new_block)

direction = "right"  # направление, в котором движемся

image_mode = True

if image_mode == True:
    # загрузка текстур змейки
    body = pg.image.load("body.png")
    body = pg.transform.scale(body, (block_size, block_size))

    head = pg.image.load("head.png")
    head = pg.transform.scale(head, (block_size, block_size))

background = pg.image.load("background.png")
background = pg.transform.scale(background, (screen.get_width(), screen.get_height()))

# далее создаются случайные координаты для яблока
apple_x = random.randrange(0, screen.get_width(), block_size)
apple_y = random.randrange(0, screen.get_height(), block_size)

apple = pg.image.load("apple.png")
apple = pg.transform.scale(apple, (block_size, block_size))

box_img = pg.image.load("7ed121b3244e921baf6203dd4f67939e.png")
box_img = pg.transform.scale(box_img, (block_size, block_size))

box_x = random.randrange(0, screen.get_width(), block_size)
box_y = random.randrange(0, screen.get_height(), block_size)

box_nam = 0

f1 = pg.font.Font(None, 30)

play = True  # Статус игры

pause = False  # Статус паузы

if play == True and pause == False:
    print(f"SnakeGame play={play}, pause={pause}, version: {version}, author: {author}")

count = 0

for i in range(150):
    count+=15

while True:

    # делаем так, чтобы окошко закрывалось нормально
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:  # проверяем, что нажимаем на клавиатуру
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                direction = "left"
            if event.key == pg.K_w or event.key == pg.K_UP:
                direction = "up"
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                direction = "right"
            if event.key == pg.K_s or event.key == pg.K_DOWN:
                direction = "down"
            if event.key == pg.K_r and cheat_mode == False:
                cheat_mode = True
            if event.key == pg.K_r and cheat_mode == True:
                cheat_mode = False
            if event.key == pg.K_EQUALS and cheat_mode == True:
                fps += 1
            if event.key == pg.K_MINUS and cheat_mode == True:
                fps -= 1
            if event.key == pg.K_SPACE and play == True:
                pause = not pause
            if event.key == pg.K_SPACE and play == False:
                play = True

                # начальные координаты для змейки
                start_x = 3 * block_size
                start_y = 4 * block_size
                snake = []  # создаём пустой список, куда потом положим блоки змейки

                for i in range(1, 4):
                    new_block = [start_x + block_size * i, start_y]
                    snake.append(new_block)

                direction = "right"  # направление, в котором движемся

                fps = 5

                apple_x = random.randrange(0, screen.get_width(), block_size)
                apple_y = random.randrange(0, screen.get_height(), block_size)

    if pause:
        continue

    if fps == 6:
        screen.blit(box_img, (box_x, box_y))
        if box_x == snake[-1][0] and box_y == snake[-1][1]:
            fps = 7
            box_nam+=1

        if box_nam > 0:
            continue



    # проверка на смерть змейки
    if snake[-1] in snake[:-1] or \
            snake[-1][0] + block_size == 0 or \
            snake[-1][1] + block_size == 0 or \
            snake[-1][0] == screen.get_width() or snake[-1][1] == screen.get_height():
        play = False
        if lang == "ru":
            text_ru = f1.render("ВЫ ПРОИГРАЛИ", True, pg.Color("black"))
            screen.blit(text_ru, text_ru.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)))
            text1_ru = f1.render("Длина змейки: " + str(len(snake)), True, pg.Color("black"))
            screen.blit(text1_ru, text1_ru.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 40)))
            text2_ru = f1.render("Нажмите на пробел чтобы перезапустить", True, pg.Color("black"))
            screen.blit(text2_ru, text2_ru.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 80)))
            pg.display.flip()
            clock.tick(fps)
            continue  # начинаем цикл заново без того, что написано ниже
        elif lang == "en":
            text_en = f1.render("YOU LOSE", True, pg.Color("black"))
            screen.blit(text_en, text_en.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)))
            text1_en = f1.render("Snake length: " + str(len(snake)), True, pg.Color("black"))
            screen.blit(text1_en, text1_en.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 40)))
            text2_en = f1.render("Press spacebar to restart", True, pg.Color("black"))
            screen.blit(text2_en, text2_en.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 80)))
            pg.display.flip()
            clock.tick(fps)
            continue  # начинаем цикл заново без того, что написано ниже



    # в зависимости от выбранного направления, меняем блок головы змейки
    if direction == "left":
        old_block = snake[-1]
        new_block = [old_block[0] - block_size, old_block[1]]
        snake.append(new_block)

    if direction == "right":
        old_block = snake[-1]
        new_block = [old_block[0] + block_size, old_block[1]]
        snake.append(new_block)

    if direction == "down":
        old_block = snake[-1]
        new_block = [old_block[0], old_block[1] + block_size]
        snake.append(new_block)

    if direction == "up":
        old_block = snake[-1]
        new_block = [old_block[0], old_block[1] - block_size]
        snake.append(new_block)

    if apple_x == snake[-1][0] and apple_y == snake[-1][1]:
        apple_x = random.randrange(0, screen.get_width(), block_size)
        apple_y = random.randrange(0, screen.get_height(), block_size)
        fps += 1
    else:
        del snake[0]

    if len(snake) == count:
        fps = 12

    screen.blit(background, (0, 0))  # отрисовка фона

    # отрисовка змейки, если есть картинки
    if image_mode == True:
        for snake_block in snake:
            screen.blit(body, (snake_block[0], snake_block[1]))

        # отрисовка головы
        screen.blit(head, (snake[-1][0], snake[-1][1]))
    else:  # отрисовка змейки, если нет картинок
        for snake_block in snake:
            pg.draw.rect(screen, pg.Color("green"), (snake_block[0], snake_block[1], block_size, block_size))

    screen.blit(apple, (apple_x, apple_y))

    # вывод счёта
    if lang == "ru":
        text3_ru = f1.render("Счёт: " + str(len(snake)), True, pg.Color("black"))
        screen.blit(text3_ru, (0, 0))
        counter_ru = f1.render("Скорость: " + str(fps), True, pg.Color("black"))
        screen.blit(counter_ru, (0, 20))
    elif lang == "en":
        text3_en = f1.render("Check: " + str(len(snake)), True, pg.Color("black"))
        screen.blit(text3_en, (0, 0))
        counter_en = f1.render("Speed: " + str(fps), True, pg.Color("black"))
        screen.blit(counter_en, (0, 20))

    pg.display.flip()  # отрисовывает кадр, обязательная строчка после всех команд отрисовки
    clock.tick(fps)  # счётчик для фпс

