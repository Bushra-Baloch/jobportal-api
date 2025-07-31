from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('company', 'Company'),
        ('applicant', 'Applicant'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Job(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'company'})
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'applicant'})
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.title}"
