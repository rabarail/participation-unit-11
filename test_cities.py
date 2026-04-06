

def test_city_country():
    result = test_city_country("Santiago", "Chile")
    assert result == "Santiago, Chile"
"""Test with just city and country."""
def test_city_country_population():
    result = test_city_country("Santiago", "Chile", population=5000000)
    assert result == "Santiago, Chile, - population 5000000"  
"""Test with city, country, and population."""


