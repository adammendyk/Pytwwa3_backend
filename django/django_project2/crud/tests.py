from django.test import TestCase

from .models import Message

# Create your tests here.

class MessageTestCase(TestCase):
    def setUp(self):
        m1 = Message.objects.create(
            name = "Jan Kołodziej",
            email = "jan@kołodziej.com",
            priority = 4,
            category = "question",
            subject = "Kto to?",
            body = "Puste",
        )
        m2 = Message.objects.create(
            name = "Ewa Kowal",
            email = "ewa@kowal.com",
            priority = 9,
            category = "other",
            subject = "Co to?",
            body = "Bla bla",
        )
        m3 = Message.objects.create(
            name = "Adam Bartnik",
            email = "adam@bartnik.com",
            priority = 43,
            category = "question",
            subject = "Gdzie?",
            body = "Lorem ipsum lorem",
        )

    # Testowanie modelu
    def test_create_object(self):
        length = len(Message.objects.all())
        self.assertEqual(length, 3)

    def test_valid_message(self):
        m = Message.objects.get(id=1)
        self.assertTrue(m.is_valid_message())

    def test_invalid_message(self):
        m = Message.objects.filter(name="Adam Bartnik").first()
        self.assertFalse(m.is_valid_message())

    def test_increase_priority(self):
        m = Message.objects.get(id=2)
        p = m.priority
        m.increase_priority()
        self.assertEqual(p+1, m.priority)
