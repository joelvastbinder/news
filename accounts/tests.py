from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234"
        )
        first_pass = User.objects.last().password.split('$')
        hasher = first_pass[0]
        salt = first_pass[1]

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password('testpass1234'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testsuperpass1234"
        )
        first_pass = User.objects.last().password.split('$')
        hasher = first_pass[0]
        salt = first_pass[1]

        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertTrue(admin_user.check_password('testsuperpass1234'))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


