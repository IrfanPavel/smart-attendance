import unittest
import os
import pandas as pd
from app import add_attendance

class TestAddAttendance(unittest.TestCase):
    def setUp(self):
        self.test_file = 'Attendance/Attendance-test.csv'
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        with open(self.test_file, 'w') as f:
            f.write("Name,Roll,Time\n")

    def test_add_attendance(self):
        # Test case 1: add attendance for a new user
        add_attendance("John_123456")
        df = pd.read_csv(self.test_file)
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[1]['Name'], 'John')
        self.assertEqual(df.iloc[1]['Roll'], 123456)

        # Test case 2: add attendance for an existing user
        add_attendance("John_123456")
        df = pd.read_csv(self.test_file)
        self.assertEqual(len(df), 3)
        self.assertEqual(df.iloc[2]['Name'], 'John')
        self.assertEqual(df.iloc[2]['Roll'], 123456)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
