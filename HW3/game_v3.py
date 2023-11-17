"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    # Записываем в переменную количество попыток
    count = 0
    # Устанавливаем границы интервала, в котором будет осуществляться поиск числа
    a = 1
    b = 100
    predict_number = b
    # Cоздаем бесконечный цикл
    while True:
        # Добавляем 1 к счетчику попыток
        count += 1
        # Проверяем условие, если исходное число больше предсказанноего, то
        if number > predict_number:
            # Присваиваем новые значения переменным, чтобы уменьшить интервал возможных чисел.
            a = predict_number
            predict_number = int((a + b) / 2)
        # Проверяем условие, если исходное число меньше предсказанноего, то
        elif number < predict_number:
            # Присваиваем новые значения переменным, чтобы уменьшить интервал возможных чисел.
            b = predict_number
            predict_number = int((a + b) / 2)
        # Если число угадали, выходим из цикла
        if number == predict_number:
            break

            # Ваш код заканчивается здесь

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)