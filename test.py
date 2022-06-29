# -*- coding: utf-8 -*-
import main as test

standart_action = 15000
standart_duration = 1
standart_weight = 75
standart_height = 180
standart_length_pool = 25
standart_count_pool = 40


class TestOutput:

    def __init__(self, action : int, duration : int, weight : int, height : int, length_pool : int, count_pool : int) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.height = height
        self.length_pool = length_pool
        self.count_pool = count_pool

    def start_test(self) -> None:
        self.test_tranning()
        self.test_swimming()
        self.test_sport_walking()
        self.test_running()

    def test_tranning(self) -> AssertionError:
        """Проверка вычислений класса Tranning."""
        tranning = test.Tranning(self.action, self.duration, self.weight)
        assert self.get_bool_accuracy(tranning.get_distance(), 9.75), 'Неверно вычисляется дистанция в классе Tranning'
        assert self.get_bool_accuracy(tranning.get_mean_speed(), 9.75), 'Неверно вычисляется средняя скорость в классе Tranning'

    def test_swimming(self) -> AssertionError:
        """Проверка вычислений класса Swimming."""
        swimming = test.Swimming(self.action, self.duration, self.weight, self.length_pool, self.count_pool)
        assert self.get_bool_accuracy(swimming.get_spent_calories(), (swimming.get_mean_speed() + 1.1) * 2 * self.weight), ''
        assert self.get_bool_accuracy(swimming.get_mean_speed(), self.length_pool * self.count_pool / 1000 / self.duration), ''

    def test_sport_walking(self) -> AssertionError:
        """Проверка вычислений класса SportsWalking."""
        sport_walking = test.SportsWalking(self.action, self.duration, self.weight, self.height)
        assert self.get_bool_accuracy(sport_walking.get_spent_calories(), (0.035 *
                                      self.weight + (sport_walking.get_mean_speed() ** 2 // self.height) *
                                      0.029) * self.duration), ''

    def test_running(self) -> AssertionError:
        """Проверка вычислений класса Running."""
        running = test.Running(self.action, self.duration, self.weight)
        assert self.get_bool_accuracy(running.get_spent_calories(), ((18 * running.get_mean_speed() - 20) *
                self.weight) / 1000 * self.duration), ''

    def get_bool_accuracy(self, current, standart, accuracy = 0.01):
        return abs((current / standart) - 1) < accuracy

if __name__ == '__main__':
    TestOutput(standart_action,
               standart_duration,
               standart_weight,
               standart_height,
               standart_length_pool,
               standart_count_pool).start_test()