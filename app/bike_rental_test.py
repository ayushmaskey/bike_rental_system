import unittest
from datetime import datetime, timedelta
from bike_rental import BikeRental
from customer import Customer

class BikeRentalTest(unittest.TestCase):

	def test_bike_rental_displays_corrent_stock(self):

		shop1 = BikeRental()
		shop2 = BikeRental(10)
		self.assertEqual(shop1.display_stock(), 0 )
		self.assertEqual(shop2.display_stock(), 10 )


	def test_rentBikeOnHourlyBasis(self):
		shop = BikeRental(10)
		self.assertEqual(shop.rentBikeOnHourlyBasis(-1), None )
		self.assertEqual(shop.rentBikeOnHourlyBasis(0), None )
		self.assertEqual(shop.rentBikeOnHourlyBasis(11), None )

		now = datetime.now()
		self.assertEqual(shop.rentBikeOnHourlyBasis(1).hour, now.hour)
		self.assertEqual(shop.rentBikeOnHourlyBasis(2).minute, now.minute)
		self.assertEqual(shop.rentBikeOnHourlyBasis(3).second, now.second)

	def test_rentBikeOnDailyBasis(self):
		shop = BikeRental(10)
		self.assertEqual(shop.rentBikeOnDailyBasis(-1), None )
		self.assertEqual(shop.rentBikeOnDailyBasis(0), None )
		self.assertEqual(shop.rentBikeOnDailyBasis(11), None )

		now = datetime.now()
		self.assertEqual(shop.rentBikeOnDailyBasis(1).hour, now.hour)
		self.assertEqual(shop.rentBikeOnDailyBasis(2).minute, now.minute)
		self.assertEqual(shop.rentBikeOnDailyBasis(3).second, now.second)

	def test_rentBikeOnWeeklyBasis(self):
		shop = BikeRental(10)
		self.assertEqual(shop.rentBikeOnWeeklyBasis(-1), None )
		self.assertEqual(shop.rentBikeOnWeeklyBasis(0), None )
		self.assertEqual(shop.rentBikeOnWeeklyBasis(11), None )

		now = datetime.now()
		self.assertEqual(shop.rentBikeOnWeeklyBasis(1).hour, now.hour)
		self.assertEqual(shop.rentBikeOnWeeklyBasis(2).minute, now.minute)
		self.assertEqual(shop.rentBikeOnWeeklyBasis(3).second, now.second)

	def test_returnBike_for_invalid_rentalBasis(self):
		shop = BikeRental(10)
		customer = Customer()

		customer.rentalTime = datetime.now()
		customer.bikes = 3

		#invalid rental basis: can only be 1 2 & 3 ( i  think, looking at if statment in return bike)
		customer.rentalBasis = 7

		request = customer.returnBike()
		self.assertEqual(shop.returnBike(request), 0)


	def test_returnBike_for_invalid_rentalTime(self):
    	# create a shop and a customer
		shop = BikeRental(10)
		customer = Customer()

		# let the customer not rent a bike a try to return one.
		request = customer.returnBike()
		self.assertIsNone(shop.returnBike(request))

		# manually check return function with error values
		self.assertIsNone(shop.returnBike((0,0,0)))



	def test_returnBike_for_invalid_numOfBikes(self):
		shop = BikeRental(10)
		customer = Customer()

		customer.rentalTime = datetime.now()
		customer.rentalBasis = 1

		#invalid number of bikes
		customer.bikes = 0

		request = customer.returnBike()
		self.assertEqual(shop.returnBike(request), None)
		self.assertIsNone( shop.returnBike(request) )

	def test_returnBike_for_valid_credential(self):
		#create shop and 6 customers
		shop = BikeRental(50)
		customer1 = Customer()
		customer2 = Customer()
		customer3 = Customer()
		customer4 = Customer()
		customer5 = Customer()
		customer6 = Customer()

		customer1.rentalBasis = 1 #hourly
		customer2.rentalBasis = 1
		customer3.rentalBasis = 2 #daily
		customer4.rentalBasis = 2
		customer5.rentalBasis = 3 #weekly
		customer6.rentalBasis = 3

		customer1.bikes = 1
		customer2.bikes = 5	#eligible for 30% discount
		customer3.bikes = 2
		customer4.bikes = 8
		customer5.bikes = 15
		customer6.bikes = 30

		customer1.rentalTime = datetime.now() + timedelta(hours = -4)
		customer2.rentalTime = datetime.now() + timedelta(hours = -23)
		customer3.rentalTime = datetime.now() + timedelta(days = -4)
		customer4.rentalTime = datetime.now() + timedelta(days = -13)
		customer5.rentalTime = datetime.now() + timedelta(weeks = -6)
		customer6.rentalTime = datetime.now() + timedelta(weeks = -12)

		request1 = customer1.returnBike()
		request2 = customer2.returnBike()
		request3 = customer3.returnBike()
		request4 = customer4.returnBike()
		request5 = customer5.returnBike()
		request6 = customer6.returnBike()

		#check if bill is correct
		self.assertEqual( shop.returnBike(request1), 20 )
		self.assertEqual( shop.returnBike(request2), 402.5 )
		self.assertEqual( shop.returnBike(request3), 160 )
		self.assertEqual( shop.returnBike(request4), 2080 )
		self.assertEqual( shop.returnBike(request5), 5400 )
		self.assertEqual( shop.returnBike(request6), 21600 )

if __name__ == "__main__":
	unittest.main()
