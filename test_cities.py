

def test_city_country():
    result = test_city_country("Santiago", "Chile")
    assert result == "Santiago, Chile"
    result += test_city_country({city.name},{country.name}, population=5000000)


