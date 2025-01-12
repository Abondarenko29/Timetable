from django.db import models
import teacher_subject.models as ts


# Create your models here.
class Class(models.Model):
    class Letter(models.TextChoices):
        A = "A", "А"
        B = "B", "Б"
        W = "W", "В"
        G = "G", "Г"
        MA = "MA", "МА"
        MB = "MB", "МБ"
        MW = "MW", "МВ"
        MG = "MG", "МГ"

    number = models.IntegerField(null=False, blank=False)
    letter = models.CharField(max_length=2, choices=Letter.choices,
                              null=False, blank=False)
    organiser = models.ForeignKey(ts.Teacher, on_delete=models.SET_NULL,
                                  blank=False, null=True)  # Класний керівник

    def __str__(self):
        return f"{self.number}-{self.letter}"


class Student(models.Model):
    class Group(models.TextChoices):
        ONE = "ONE", "1"
        TWO = "TWO", "2"

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthday_day = models.DateField(null=True)
    clas = models.ForeignKey(Class, null=False, blank=False,
                             on_delete=models.CASCADE)
    group = models.CharField(max_length=3, choices=Group.choices)

    def __str__(self):
        return f"{self.name} {self.surname}"
