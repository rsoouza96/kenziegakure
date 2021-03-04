from src.models.jounin_model import Jounin
from src.models.ninja_model import Ninja

def test_jounin():
    kakashi_proficiency = {'taijutsu': 7, 'ninjutsu': 8, 'genjutsu': 4}
    kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
    result = kakashi.__dict__

    expected = {
        'name': 'Kakashi',
        'ninja_level': 'Jounin',
        'clan': 'Hatake',
        'village': 'Konoha',
        'proficiency': {'taijutsu': 7, 'ninjutsu': 8, 'genjutsu': 4},
        'jutsu_list': [],
        'health_pool': 100,
        'chakra_pool': 100,
        'concious': True,
        'is_in_mission': False
    }

    assert result == expected

def test_list_best_proficiency():
    kakashi_proficiency = {'taijutsu': 7, 'ninjutsu': 8, 'genjutsu': 4}
    kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
    result = kakashi.list_best_proficiency()

    expected = 'Kakashi demonstra maior proficiência em ninjutsu'

    assert result == expected

def test_list_best_proficiency_draw():
    kakashi_proficiency = {'taijutsu': 8, 'ninjutsu': 8, 'genjutsu': 4}
    kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
    result = kakashi.list_best_proficiency()

    expected = 'Kakashi demonstra maior proficiência em taijutsu'

    assert result == expected

def test_start_mission_not_in_mission():
    kakashi_proficiency = {'taijutsu': 8, 'ninjutsu': 8, 'genjutsu': 4}
    kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
    result = kakashi.start_mission()
    expected = 'O ninja Kakashi Hatake saiu em missão'

    assert result == expected

def test_start_mission_in_mission():
    kakashi_proficiency = {'taijutsu': 8, 'ninjutsu': 8, 'genjutsu': 4}
    kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
    kakashi.start_mission()
    result = kakashi.start_mission()
    expected = 'O ninja Kakashi Hatake já está em uma missão'

    assert result == expected

def test_return_from_mission_not_in_mission():
    kakashi_proficiency = {'taijutsu': 8, 'ninjutsu': 8, 'genjutsu': 4}
    kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
    result = kakashi.return_from_mission()
    expected = 'O ninja Kakashi Hatake não está em nenhuma missão no momento'

    assert result == expected

def test_return_from_mission_in_mission():
    kakashi_proficiency = {'taijutsu': 8, 'ninjutsu': 8, 'genjutsu': 4}
    kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
    kakashi.start_mission()
    result = kakashi.return_from_mission()
    expected = 'O ninja Kakashi Hatake retornou em segurança da missão'

    assert result == expected
