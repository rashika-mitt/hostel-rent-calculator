rent = int(input("Total amount of RENT of flat ="))
food = int(input("Total amount of FOOD ="))
electricity_spend = int(input("Total amount of ELECTRICITY BILL ="))
charge_per_unit = int(input("CHARGE PER UNIT ="))
person = int(input("Total number of PERSON ="))

total_electricity = electricity_spend * charge_per_unit

output = (rent + food + total_electricity) // person

print(f"Each Person will pay {output}")