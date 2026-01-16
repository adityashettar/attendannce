class Attendance:
    def __init__(self, classes_held, classes_attended):
        self.classes_held = classes_held
        self.classes_attended = classes_attended

    def calculate_percentage(self):
        if self.classes_held == 0:
            return 0
        return (self.classes_attended / self.classes_held) * 100

    def check_eligibility(self):
        return "Eligible" if self.calculate_percentage() >= 75 else "Not Eligible"


if __name__ == "__main__":
    held = int(input("Enter classes held: "))
    attended = int(input("Enter classes attended: "))

    attendance = Attendance(held, attended)
    print(f"Attendance Percentage: {attendance.calculate_percentage():.2f}%")
    print(attendance.check_eligibility())
