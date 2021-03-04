from .jutsu_model import Jutsu

class Ninja:
    def __init__(self, name: str, clan: str, village: str, ninja_level: str = 'Unranked', jutsu_list: list = [],
                 health_pool: int = 100, chakra_pool: int = 100, concious: bool = True):
        self.name = name
        self.ninja_level = ninja_level
        self.clan = clan
        self.village = village
        self.jutsu_list = jutsu_list
        self.health_pool = health_pool
        self.chakra_pool = chakra_pool
        self.concious = concious

    def learn_jutsu(self, jutsu:dict):
        self.jutsu_list.append(jutsu.__dict__)
        return f'O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {jutsu.jutsu_name}'

    @staticmethod
    def check_health(ninja_to_check:dict):
        if ninja_to_check['health_pool'] <= 0:
            ninja_to_check['health_pool'] = 0
            ninja_to_check['concious'] = False
        return ninja_to_check['concious']

    def cast_jutsu(self, jutsu:dict, adversary:dict):
        if adversary['concious'] == False:
            return False
        else:
            if jutsu in self.jutsu_list and self.chakra_pool >= jutsu['chakra_spend']:
                adversary['health_pool'] -= jutsu['jutsu_damage']
                self.chakra_pool -= jutsu['chakra_spend']
                adversary['health_pool']
                return True
        return False
