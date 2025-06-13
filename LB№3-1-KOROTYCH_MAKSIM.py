from datetime import date, datetime

class Person:
    def __init__(self, surname, first_name, birth_date_str, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname

        # Розбір рядка "YYYY-MM-DD" у об'єкт datetime.date
        year, month, day = map(int, birth_date_str.strip().split('-'))
        self.birth_date = date(year, month, day)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"
