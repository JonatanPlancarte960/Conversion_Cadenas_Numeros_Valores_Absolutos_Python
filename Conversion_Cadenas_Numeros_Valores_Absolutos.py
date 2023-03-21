first_planet_input = input('Enter the distance between the sun and the first planet in KM: ')
second_planet_input = input('Enter the distance between the sun and the second planet in KM: ')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = first_planet - second_planet

print(abs(distance_km))