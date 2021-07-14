from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# from .models import users
from .models import CustomUser


class userTests(TestCase):
    def setUp(self):
        self.users = get_user_model().objects.create_user(
            username="Hamza", email="hamza.qah@gmail.com", password="pwd"
        )

    def test_user_creation(self):
        email = self.users.email
        self.assertEquals(self.users.__str__(), "Hamza")
        self.assertEquals(self.users.email.__str__(), "hamza.qah@gmail.com")

    def test_duplicates(self):
        try:
            self.user = get_user_model().objects.create_user(
                username="Hamza", email="hamza.qah@gmail.com", password="pwd"
            )
        except:
            print("Resgistration falied!")
