x = 0
while x <= 5:
    print(x)
    x = x+1

counties = ("Arapahoe", "Denver", "Jefferson")
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4, 5]
for num in range(5):
    print(num)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(county, voters)
    

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:

     print(county_dict['registered_voters'])

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters.")

