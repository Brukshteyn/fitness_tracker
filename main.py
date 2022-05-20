from typing import Tuple, List


class InfoMessage:

    MESSAGE = '''
    Тип тренировки: {tranning_type}; 
    Длительность: {duration} ч;
    Дистанция: {distance} км;
    Ср. скорость: {speed} км/ч;
    Потрачено ккал: {calories}'''

    def __init__(self,
                 tranning_type : str,
                 duration : float,
                 distance : float,
                 speed : float,
                 calories : float) -> None:
        self.tranning_type = tranning_type
        self.duration = round(duration, 3)
        self.distance = round(distance, 3)
        self.speed = round(speed, 3)
        self.calories = round(calories, 3)

    def get_info_message(self) -> str:
        return self.MESSAGE.format(tranning_type = self.tranning_type,
                                   duration = self.duration,
                                   distance = self.distance,
                                   speed = self.speed,
                                   calories = self.calories)


class Tranning:

    M_IN_KM = 1000
    LEN_STEP = 0.65
    NAME_TRANNING = 'noname'

    def __init__(self, action : int, duration : int, weight : int) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        return (self.action * self.LEN_STEP) / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        pass

    def show_training_info(self) -> InfoMessage:
        return InfoMessage(tranning_type = self.NAME_TRANNING,
                           duration = self.duration,
                           distance = self.get_distance(),
                           speed = self.get_mean_speed(),
                           calories = self.get_spent_calories())


class Swimming(Tranning):

    LEN_STEP = 1.38
    NAME_TRANNING = 'Плавание'

    def __init__(self, action : int, duration : int, weight : int, length_pool : int, count_pool : int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 2
        return (self.get_mean_speed() + 1.1) * coeff_calorie_1 * self.weight

    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration


class SportsWalking(Tranning):

    NAME_TRANNING = 'Спортивная ходьба'

    def __init__(self, action : int, duration : int, weight : int, height : int) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        return (coeff_calorie_1 * self.weight + (self.get_mean_speed() ** 2 // self.height) * coeff_calorie_2) * self.duration


class Running(Tranning):

    NAME_TRANNING = 'Бег'

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        return ((coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2 ) *self.weight) / self.M_IN_KM * self.duration


def main(tranning: Tranning) -> None:
    info = tranning.show_training_info()
    print(info.get_info_message())

def read_package(tranning_type : str,  package : List[int]) -> Tranning:
    if tranning_type == 'RUN':
        return Running(action = package[0],
                       duration = package[1],
                       weight = package[2])
    if tranning_type == 'SWM':
        return Swimming(action = package[0],
                        duration = package[1],
                        weight = package[2],
                        length_pool = package[3],
                        count_pool = package[4]
                        )
    if tranning_type == 'WLK':
        return SportsWalking(action = package[0],
                             duration = package[1],
                             weight = package[2],
                             height = package[3])

if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)


