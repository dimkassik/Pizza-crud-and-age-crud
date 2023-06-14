from django.db import models
from datetime import datetime

class Person(models.Model):
    iin = models.CharField(max_length=12, unique=True)

    @property
    def age(self):
        return self.calculate_age()

    def calculate_age(self):
        if not self.iin or len(self.iin) != 12:
            return 0

        if self.iin[0] == '2' or self.iin[0] == '1' or self.iin[0] == '0':
            year = 2000 + int(self.iin[:2])
        else:
            year = 1900 + int(self.iin[:2])
        month = int(self.iin[2:4])
        day = int(self.iin[4:6])
        c_year = datetime.now().year
        age = c_year - year
        if month > datetime.now().month or (month == datetime.now().month and day > datetime.now().day):
            age -= 1
        return age