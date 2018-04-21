from django.db import models

class Example(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField()
  completed = models.BooleanField(default=False)

  def to_json(self):
    return {
      'id': self.id,
      'title': self.title,
      'text': self.text,
      'completed': self.completed ,
    }


  def __str__(self):
    return self.title