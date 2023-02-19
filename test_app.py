import unittest
import app

class TestUsernameAndId(unittest.TestCase):



    def test_username_and_id_2(self):
        result = app.check_username_and_id("Sami123", "1704111")
        self.assertEqual(result, "Invalid username")
 

    def test_username_and_id_3(self):
        result = app.check_username_and_id("", "1704110")
        self.assertEqual(result, "Username cannot be empty")

    def test_username_and_id_4(self):
        result = app.check_username_and_id("Irfan Pavel", "")
        self.assertEqual(result, "ID cannot be empty")

    def test_username_and_id_1(self):
        result = app.check_username_and_id("Irfan Pavel", "1704110")
        self.assertEqual(result, "Successful Login")

    # def test_username_and_id_5(self):
    #     result = app.check_username_and_id("", "")
    #     self.assertEqual(result, "Both cannot be empty")

if __name__ == '__main__':
    unittest.main()
