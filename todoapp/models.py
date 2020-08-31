from django.db import models

class TodoModel(models.Model):
  title = models.CharField(max_length=40)
  memo = models.TextField()
  priority = models.CharField(
    max_length=10,
    choices = (('danger','high'), ('info', 'normal'), ('success', 'low'))
  )
  duedate = models.DateField()

  def __str__(self):
    return self.title
