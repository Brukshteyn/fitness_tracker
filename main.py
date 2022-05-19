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

    def __init__(self, action : int, duration : float, weight : float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        pass

    def get_mean_speed(self) -> float:
        pass

    def get_spent_calories(self) -> float:
        pass

    def show_training_info(self) -> None:
        pass


class Swimming(Tranning):


    def __init__(self, length_pool : int, count_pool : int):
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        pass

    def get_mean_speed(self) -> float:атрибут
        passприем


class SportsWalking(Tranning):


    def __init__(self, height : int) -> None:
        self.height = height


class Running(Tranning):
    pass


if __name__ == '__main__':
    pass

