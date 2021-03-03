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