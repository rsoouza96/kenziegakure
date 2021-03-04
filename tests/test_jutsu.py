from src.models.jutsu_model import Jutsu

def test_jutsu():
    rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
    result = rasengan.__dict__
    expected = {
        'jutsu_name': 'Rasengan',
        'jutsu_type': 'Vento',
        'jutsu_level': 'A',
        'jutsu_damage': 20,
        'chakra_spend': 100
    }
    assert result == expected

def test_jutsu_positive_chakra():
    rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, 55)
    result = rasengan.__dict__
    expected = {
        'jutsu_name': 'Rasengan',
        'jutsu_type': 'Vento',
        'jutsu_level': 'A',
        'jutsu_damage': 20,
        'chakra_spend': 55
    }
    assert result == expected

def test_jutsu_positive_rank_not_in_list():
    rasengan = Jutsu('Rasengan', 'Vento', 'z', 20, 55)
    result = rasengan.__dict__
    expected = {
        'jutsu_name': 'Rasengan',
        'jutsu_type': 'Vento',
        'jutsu_level': 'Unranked',
        'jutsu_damage': 20,
        'chakra_spend': 55
    }
    assert result == expected

def test_jutsu_positive_rank_not_in_list_and_negative_chakra():
    rasengan = Jutsu('Rasengan', 'Vento', 'z', 20, 100)
    result = rasengan.__dict__
    expected = {
        'jutsu_name': 'Rasengan',
        'jutsu_type': 'Vento',
        'jutsu_level': 'Unranked',
        'jutsu_damage': 20,
        'chakra_spend': 100
    }
    assert result == expected