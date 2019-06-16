import datetime

class BikeRental:

	def __init__(self, stock=0):
		"""Constructor to instantiate bike rental shop"""
		self.stock = stock;


	def display_stock(self):
		"""display the bikes currently available"""
		print("We currently have {} bike(s) available to rent".format(self.stock))
		return self.stock

	def rentBikeOnHourlyBasis(self, n):
		"""Rents n bikes on hourly basis"""
		if n <= 0: 
			print("Number of bikes should be positive")
			return None
		elif n > self.stock:
			print("We only have {} bikes(s) available".format(self.stock))
			return None
		else:
			now = datetime.datetime.now()
			print("You have rented {} bike(s) on hourly basis today @ {}:{}.".format(n, now.hour, now.minute))
			print("You will be charged $5 for each hour per bike")
			print("We hope you enjoy your ride")
			self.stock -= n
			return now

	def rentBikeOnDailyBasis(self, n):
		"""Rents n bikes on daily basis"""
		if n <= 0: 
			print("Number of bikes should be positive")
			return None
		elif n > self.stock:
			print("We only have {} bikes(s) available".format(self.stock))
			return None
		else:
			now = datetime.datetime.now()
			print("You have rented {} bike(s) on daily basis today @ {}:{}.".format(n, now.hour, now.minute))
			print("You will be charged $20 for each hour per bike")
			print("We hope you enjoy your ride")
			self.stock -= n
			return now

	def rentBikeOnWeeklyBasis(self, n):
		"""Rents n bikes on weekly basis"""
		if n <= 0: 
			print("Number of bikes should be positive")
			return None
		elif n > self.stock:
			print("We only have {} bikes(s) available".format(self.stock))
			return None
		else:
			now = datetime.datetime.now()
			print("You have rented {} bike(s) on weekly basis today @ {}:{}.".format(n, now.hour, now.minute))
			print("You will be charged $60 for each hour per bike")
			print("We hope you enjoy your ride")
			self.stock -= n
			return now

	def returnBike(self, request):
		"""
		1. Accept a rented bike
		2. replenish the inventory
		3. return bill
		"""

		rentalTime, rentalBasis, numOfBikes = request
		bill = 0

		if rentalTime and rentalBasis and numOfBikes:
			self.stock += numOfBikes
			now = datetime.datetime.now()
			rentalPeriod = now - rentalTime

			if rentalBasis == 1:
				bill = round(rentalPeriod.seconds / 3600 ) * 5 * numOfBikes
			elif rentalBasis == 2:
				bill = round(rentalPeriod.days) * 20 * numOfBikes
			elif rentalBasis == 3:
				bill = round(rentalPeriod.days / 7 ) * 60 * numOfBikes
			else:
				print("Rental basis can be 1 2 or 3")

			print("bill before discount: {}".format(bill))

			#family discount
			if (3 <= numOfBikes <= 5):
				print("You are eligible for family rental promotio of 30% discount coz {} bikes".format(numOfBikes))
				bill = bill * 0.7

			print("You bill is ${}".format(bill))
			return bill

		else: 
			print("This is not our bike")
			return None
