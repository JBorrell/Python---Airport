import unittest
from airport.airport import Airport


class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()

    def tearDown(self):
        pass
