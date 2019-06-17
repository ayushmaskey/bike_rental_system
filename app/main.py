
from bike_rental import BikeRental
from customer import Customer


def main():
	shop = BikeRental(100)
	customer = Customer()

	while True:
		print("""
			===== bike rental shop =======
			1. Display available
			2. Request a bike on hourly basis $5
			3. Request a bike on daily basis $20
			4. Request a bike on weekly basis $60
			5. Return a bike
			6. Exit
			""")

		choice = input("Enter choice:")

		try:
			choice = int(choice)
		except ValueError:
			print("Not an int")
			continue

		if choice == 1:
			shop.display_stock()
		elif choice == 2:
			customer.rentalTime = shop.rentBikeOnHourlyBasis( customer.requestBike() )
			customer.rentalBasis = 1
		elif choice == 3:
			customer.rentalTime = shop.rentBikeOnDailyBasis( customer.requestBike() )
			customer.rentalBasis = 2
		elif choice == 4:
			customer.rentalTime = shop.rentBikeObWeeklyBasis( customer.requestBike() )
		elif choice == 5:
			customer.bill = shop.returnBike( customer.returnBike() )
			customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0
		elif choice == 6:
			break
		else:
			print("invalid input. enter number betweek 1 and 6")

		print("Thank you")


if __name__ == "__main__":
	main()