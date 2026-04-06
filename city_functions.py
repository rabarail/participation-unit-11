""""Author: Rajani Baraili
Date: 04-05-2026
Purpose:function returns formatted city and country name as readable string """

"""Return a formatted string in the format of 'City, Country – population xxx'."""


def input_city_country():
        city_name = input("Enter the name of the city: ")
        country_name = input("Enter the name of the country: ")
        population = input("Enter the population (optional): ")

        def city_country(city, country, population=None):
            result = f"{city.name}, {country.name}"
            if population is not None:
                result += f", {population}"
            return result

input_city_country()
    



  


    