from .ninja_model import Ninja

class Jounin(Ninja):
    ninja_level = "Jounin"
    def __init__(self, name: str, clan: str, village: str, proficiency: dict, is_in_mission: bool = False):
        super().__init__(name, clan, village, ninja_level=self.ninja_level)
        self.proficiency = proficiency
        self.is_in_mission = is_in_mission

    def list_best_proficiency(self):
        largest_value = max(self.proficiency, key=lambda k: self.proficiency[k])
        return f'Kakashi demonstra maior proficiência em {largest_value}'

    def start_mission(self):
        if self.is_in_mission:
            return f'O ninja {self.name} {self.clan} já está em uma missão'
        else:
            self.is_in_mission = True
            return f'O ninja {self.name} {self.clan} saiu em missão'

    def return_from_mission(self):
        if not self.is_in_mission:
            self.is_in_mission = False
            return f'O ninja {self.name} {self.clan} não está em nenhuma missão no momento'
        else:
            return f'O ninja {self.name} {self.clan} retornou em segurança da missão'