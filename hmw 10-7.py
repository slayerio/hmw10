countries = [
    {'name': 'Israel', 'population': 9.3, 'birth': 1948},
    {'name': 'United States', 'population': 331.9, 'birth': 1776},
    {'name': 'Japan', 'population': 125.8, 'birth': 660},
    {'name': 'Australia', 'population': 25.7, 'birth': 1901},
    {'name': 'Canada', 'population': 38.0, 'birth': 1867}
    ]
# a
over_30mil = list(filter(lambda x: x['population'] > 30, countries))
print(over_30mil)
# b
after_1800 = list(filter(lambda x: x['birth'] > 1800, countries))
print(after_1800)
# c
only_names = list(map(lambda x: x['name'], countries))
print(only_names)
# d
birth_year = list(map(lambda x: x['birth'], countries))
print(birth_year)
# e
sorted_birth = sorted(countries, key=lambda x: x['birth'])
print(sorted_birth)
# f
sorted_population = sorted(countries, key=lambda x: x['population'])
print(sorted_population)