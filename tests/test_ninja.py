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

def test_check_health():
    naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
    result = Ninja.check_health(naruto.__dict__)
    expected = True
    assert result == expected

def test1_check_health():
    naruto = Ninja('Naruto', 'Uzumaki', 'Konoha', 'Unranked', [], -15)
    result = Ninja.check_health(naruto.__dict__)
    expected = False
    assert result == expected

def test_cast_jutsu():
    rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
    naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
    naruto.learn_jutsu(rasengan)
    sasuke = Ninja('Sasuke', 'Uchiha', 'Konoha')
    result = naruto.cast_jutsu(rasengan.__dict__, sasuke.__dict__)
    expected = True
    assert result == expected

def test2_cast_jutsu():
    rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, 220)
    naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
    naruto.learn_jutsu(rasengan)
    sasuke = Ninja('Sasuke', 'Uchiha', 'Konoha')
    result = naruto.cast_jutsu(rasengan.__dict__, sasuke.__dict__)
    expected = False
    assert result == expected

def test3_cast_jutsu():
    rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
    naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
    naruto.learn_jutsu(rasengan)
    sasuke = Ninja('Sasuke', 'Uchiha', 'Konoha', 'Unranked', [], -15)
    result = naruto.cast_jutsu(rasengan.__dict__, sasuke.__dict__)
    expected = True
    assert result == expected