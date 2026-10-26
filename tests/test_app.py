
import unittest
from app import app

class AttendanceTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_attendance_page(self):
        response = self.client.get('/attendance')
        self.assertEqual(response.status_code, 200)

    def test_submit_attendance(self):
        response = self.client.post('/success', data={
            'student_id': '101',
            'student_name': 'Varnika',
            'subject_name': 'DevOps',
            'attendance_date': '2026-10-26',
            'status': 'Present'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Attendance Marked Successfully', response.data)

if __name__ == '__main__':
    unittest.main()
