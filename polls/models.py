from django.db import models


class Question(models.Model):
    def __str__(self):
        return self.text

    text = models.CharField(max_length=256)
    date = models.DateTimeField("Publication date")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(max_length=256)
    votes = models.IntegerField(default=0)