from django.db import models

PRIORITY_OPTION_LOW = 3
PRIORITY_OPTION_MEDIUM = 2
PRIORITY_OPTION_HIGH = 1

PRIORITY_OPTIONS = (
    (PRIORITY_OPTION_LOW, 'Low'),
    (PRIORITY_OPTION_MEDIUM, 'Regular'),
    (PRIORITY_OPTION_HIGH, 'High'),
)


class List(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    created_by = models.ForeignKey('auth.User')
    assigned_to = models.ForeignKey('auth.User')
    due_date = models.DateField()


class Task(models.Model):
    title = models.CharField(max_length=100)
    list = models.ForeignKey('List')
    created_date = models.DateField()
    due_date = models.DateField()
    completed = models.BooleanField()
    completed_date = models.DateField()
    created_by = models.ForeignKey('auth.User')
    assigned_to = models.ForeignKey('auth.User')
    note = models.TextField()
    priority = models.IntegerField()


class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    task = models.ForeignKey('Task')
    date = models.DateField()
    body = models.TextField()
