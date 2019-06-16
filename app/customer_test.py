
import unittest
from customer import Customer
from datetime import datetime

class CustomerTest(unittest.TestCase):

	def test_return_bike_with_valid_input(self):
		customer = Customer()

		now = datetime.now()
		customer.rentalBasis = 1
		customer.rentalTime = now
		customer.bikes = 4

		self.assertEqual( customer.returnBike(), (now, 1, 4) )


	def test_return_bike_with_invalid_input(self):
		customer = Customer()

		customer.rentalBasis = 1
		customer.bikes = 0

		#invalid rental times
		customer.rentalTime = 0

		self.assertEqual(customer.returnBike(), (0,0,0) )

if __name__ == "__main__":
	unittest.main()