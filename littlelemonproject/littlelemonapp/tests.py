from django.test import TestCase
from .models import Booking, Menu
from datetime import date

class BookingModelTest(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create(
            first_name="John Doe",
            reservation_date=date.today(),
            reservation_slot=10,
        )

    def test_booking_str(self):
        self.assertEqual(str(self.booking), "John Doe")

    def test_booking_fields(self):
        self.assertEqual(self.booking.first_name, "John Doe")
        self.assertEqual(self.booking.reservation_date, date.today())
        self.assertEqual(self.booking.reservation_slot, 10)
