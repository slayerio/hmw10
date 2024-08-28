dict_israel = {
    'name': 'Israel',
    'birth': 1948,
    'population_millions': 9.3,
    'capital': 'Jerusalem',
    'language': 'Hebrew',
    'cities': ['Jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
    'currency': 'ILS',
    'area_Kilometer': 22145,
    'gdp_billion': 450}

print(dict_israel)
# a
print(dict_israel.get('capital'))
# b
print(dict_israel.keys())
# c
print([c.upper() for c in dict_israel.keys()])
# d
print(dict_israel.values())
# e (the str(c) is because not all the values in the dict are strings )
print([len(str(c)) for c in dict_israel.values()])
# f
print(dict_israel.items())
# g
dict_israel_copy = dict_israel.copy()
# h
dict_israel_copy.clear()
# i
new_dict = (dict.fromkeys(dict_israel), None)
print(new_dict)
# j
del dict_israel['currency']
print(dict_israel)
# k
area = dict_israel.pop('area_Kilometer')
print(dict_israel)
# l
dict_israel.update({'population_millions': 9.4, 'Soccer': 'sport_national'})
print(dict_israel)