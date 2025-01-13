from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    class Role(models.TextChoices):
        HEAD_TEACHER = "HEAD_TEACHER", "директор"
        HELP_HEAD_TEACHER = "HELP_HEAD_TEACHER", "зауч"
        USUALLY_TEACHER = "USUALLY_TEACHER", "просто вчитель"

    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    third_name = models.CharField(max_length=255, null=False, blank=False)
    birthday_day = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=30, null=False, blank=False,
                            choices=Role.choices, default=Role.USUALLY_TEACHER)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.third_name}"
