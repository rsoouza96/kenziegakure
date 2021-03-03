# from jutsu_model import Jutsu

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

    def learn_jutsu(self, Jutsu):
        self.jutsu_list.append(Jutsu.__dict__)
        return f'O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {Jutsu.jutsu_name}'

# Criação de uma instância da classe Jutsu
rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)

# Criação de uma instância da classe Ninja
naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')

#Chamada do método learn_jutsu
res = naruto.learn_jutsu(rasengan)