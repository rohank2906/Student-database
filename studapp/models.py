from django.db import models

class Student(models.Model):
    stdid=models.CharField(max_length=20)
    stdname=models.CharField(max_length=20)
    stdemail=models.EmailField()
    stdcontact=models.CharField(max_length=10)

    class Meta:
        db_table="student"


    def __str__(self):
        return self.stdname