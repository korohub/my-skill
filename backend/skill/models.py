from django.db import models

# Create your models here.

class Skill(models.Model):
    SkillId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Slug = models.CharField(max_length=200, null=True)
    StartDate = models.IntegerField()
    EndDate = models.IntegerField()
    Level = models.CharField(max_length=30, null=True)
    devops = models.CharField(max_length=5, null=True)

class Details(models.Model):
    DetailId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Slug = models.CharField(max_length=200, null=True)
    StartDate = models.IntegerField()
    EndDate = models.IntegerField()
    Description = models.CharField(max_length=900, null=True)
    