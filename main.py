class InfoMessage:


    def __init__(self,
                 training_type : str,
                 duration : float,
                 distance : float,
                 speed : float,
                 calories : float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories


class Tranning:

    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self, action : int, duration : float, weight : float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        return (self.action * self.LEN_STEP) / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        pass

    def show_training_info(self) -> None:
        pass


class Swimming(Tranning):

    LEN_STEP = 1.38

    def __init__(self, length_pool : int, count_pool : int):
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 2
        return (self.get_mean_speed() + 1.1) * coeff_calorie_1 * self.weight

    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration


class SportsWalking(Tranning):


    def __init__(self, height : int) -> None:
        self.height = height

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        return (coeff_calorie_1 * self.weight + (self.get_mean_speed() ** 2 // self.height) * coeff_calorie_2) * self.duration


class Running(Tranning):


    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        return ((coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2 ) *self.weight) / self.M_IN_KM * self.duration


if __name__ == '__main__':
    pass

