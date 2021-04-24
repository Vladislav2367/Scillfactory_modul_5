import numpy as np


# noinspection PyUnusedLocal
def game_core_v3(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости
    от того, больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    a = 1  # Первоначальная нижняя граница
    b = 1001  # Первоначальная верхняя граница
    c = 1.001  # Коэффициент влияющий на число итераций
    predict = np.random.randint(a, b)
    print('Predict: ', predict, ',  game_core(number): ', number)
    while number != predict:  # цикл рассчета
        count += 1
        if number - predict > 0:
            a1 = a
            a = (number - predict) / c
            predict = a + predict
        elif number - predict < 0:
            b1 = b
            b = (number - predict) / c
            predict = b + predict
        elif number == predict:
            break
    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

score_game(game_core_v3)