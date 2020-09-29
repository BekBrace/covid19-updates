'The COVID19 Library in Python 3.6 '
from covid import Covid
covid = Covid()
Poland = covid.get_status_by_country_name('poland')
data = {key: Poland[key]
        for key in Poland.keys() and {'confirmed', 'active', 'deaths', 'recovered'}}
# print(data)

# Display the names of the countries
countries = covid.list_countries()
# print(countries)

# Get the COVID-19 related information for all the countries
# print(covid.get_data())

# Get the covid-19 related information by country ID
egypt = covid.get_status_by_country_id(54)
poland = covid.get_status_by_country_id(137)
russia = covid.get_status_by_country_id(141)
japan = covid.get_status_by_country_id(88)

print(f'Stats for Egypt: {egypt}')
print(f'Stats for Poland: {poland}')
print(f'Stats for Russia: {russia}')
print(f'Stats for Japan: {japan}')
