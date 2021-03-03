from src.models.ninja_model import Ninja
from src.models.jutsu_model import Jutsu

def test_ninja():
    naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
    result = naruto.__dict__
    expected = {
        'name': 'Naruto',
        'ninja_level': 'Unranked',
        'clan': 'Uzumaki',
        'village': 'Konoha',
        'jutsu_list': [],
        'health_pool': 100,
        'chakra_pool': 100,
        'concious': True
    }

    assert result == expected

def test_ninja_jutsu():
    rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
    naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
    result = naruto.learn_jutsu(rasengan)
    expected = "O ninja Naruto Uzumaki acabou de aprender um novo jutsu: Rasengan"

    assert result == expected