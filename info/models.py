from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    experience = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    parents_phone = models.CharField(max_length=13)
    telegram = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
