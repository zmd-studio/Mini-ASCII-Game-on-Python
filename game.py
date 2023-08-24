import os
import time

# Определение размеров экрана
WIDTH = 80
HEIGHT = 20

# Инициализация позиции ниндзя
ninja_x = WIDTH // 2
ninja_y = HEIGHT - 1

# Инициализация списка зомби
zombies = [[10, 5], [20, 3], [30, 7]]

# Основной игровой цикл
while True:
    # Очистка экрана
    os.system('cls' if os.name == 'nt' else 'clear')

    # Отрисовка игрового поля
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == ninja_x and y == ninja_y:
                print("@", end="")
            elif [x, y] in zombies:
                print("Z", end="")
            else:
                print(".", end="")
        print()

    # Обработка ввода игрока
    key = input("Введите команду (a - влево, d - вправо): ")

    # Обновление позиции ниндзя
    if key == "a":
        ninja_x -= 1
    elif key == "d":
        ninja_x += 1

    # Перемещение зомби
    for zombie in zombies:
        zombie[1] += 1

    # Удаление зомби, которые дошли до нижней границы
    zombies = [zombie for zombie in zombies if zombie[1] < HEIGHT]

    # Проверка столкновений
    if [ninja_x, ninja_y] in zombies:
        print("Игра окончена!")
        break

    # Задержка для плавной анимации
    time.sleep(0.1) 
