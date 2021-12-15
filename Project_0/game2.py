"""Игра угадай число
Компьютер сам загадывает и сам его угадывает
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем случайное число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # счетчик попыток
    max_number = 101 # верхняя граница поиска числа
    min_number = 1 # нижняя граница поиска числа
    
    while True:
        count += 1 
        mid_number = int((max_number + min_number)/2) # среднее между нижней и верхней границей
        predict_number = np.random.randint(min_number, max_number) # предполагаемое число
        
        if predict_number > number:
            if predict_number < mid_number: 
                max_number = predict_number # смещение верхней границы
            if predict_number == mid_number:
                max_number = mid_number # смещение верхней границы
                
        if predict_number < number:
            if predict_number > mid_number:
                min_number = predict_number # смещение нижней границы
            if predict_number == mid_number:
                min_number = mid_number # смещение нижней границы
                
        if number == predict_number:
            break  # выход из цикла если угадали
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
    score_game(random_predict)
