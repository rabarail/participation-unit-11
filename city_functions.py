""""Author: Rajani Baraili
Date: 04-05-2026
Purpose:function returns formatted city and country name as readable string """

"""Return a formatted string in the format of 'City, Country – population xxx'."""
def city_country(city, country):
    result = f"{city.name}, {country.name}"

    if city.population:
        result += f" – population {city.population}"
        return result
    
    
  


    