import unittest

from django.forms import DateField
from django.test import TestCase
from hotel.models import Room, Reserve


class RoomModelTest(unittest.TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_room_number(self):
        room = Room.objects.get(id=1)
        self.assertEqual(room.number, 2)

    def test_room_price(self):
        room = Room.objects.get(id=1)
        self.assertEqual(room.price, 150)

    def test_room_number_seats(self):
        room = Room.objects.get(id=1)
        self.assertEqual(room.number_seats, )


class ReserveModelTest(unittest.TestCase):

    @classmethod
    def setUpTestData(cls):
        Reserve.objects.create(user=1, room=1, start_date=DateField.auto_now, end_date=DateField.auto_now)

    def test_reserve_user(self):
        reserve = Reserve.objects.get(id=1)
        self.assertEqual(reserve.user, 2)

    def test_reserve_room(self):
        reserve = Reserve.objects.get(id=1)
        self.assertEqual(reserve.room, 2)

    def test_reserve_start_date(self):
        reserve = Reserve.objects.get(id=1)
        self.assertEqual(reserve.start_date, DateField.auto_now)

    def test_reserve_end_date(self):
        reserve = Reserve.objects.get(id=1)
        self.assertEqual(reserve.end_date, DateField.auto_now)


