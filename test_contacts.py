import unittest
from contacts_manager import validate_phone, validate_email

class TestContacts(unittest.TestCase):

    def test_validate_phone(self):
        self.assertEqual(validate_phone("9876543210")[0], True)
        self.assertEqual(validate_phone("123")[0], False)

    def test_validate_email(self):
        self.assertTrue(validate_email("test@gmail.com"))
        self.assertFalse(validate_email("invalid-email"))

if __name__ == "__main__":
    unittest.main()