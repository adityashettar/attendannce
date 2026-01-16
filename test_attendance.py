from attendance import Attendance

def test_attendance_eligibility():
    attendance = Attendance(100, 80)
    assert attendance.check_eligibility() == "Eligible"
