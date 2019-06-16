class Customer:

	def __init__(self):
		"""constructor to instantiate customer object"""
		self.bikes = 0
		self.rentalBasis = 0
		self.rentalTime = 0
		self.bill = 0

	def requestBike(self):
		"""Customer request bike to rent"""
		bikes = input("How many bikes would you like to rent?")

		try:
			bikes = int(bikes)
		except ValueError:
			print("Thats not a positive integer")
			return -1

		if bikes < 1:
			print('rent atleast one bike')
		else:
			self.bikes = bikes

		return self.bikes


	def returnBike(self):
		"""customer return bike to shop"""
		if self.rentalBasis and self.rentalTime and self.bikes:
			return self.rentalTime, self.rentalBasis, self.bikes
		else:
			return 0,0,0
