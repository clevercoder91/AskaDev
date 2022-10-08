from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import secrets
class Tags(models.Model):
	tag = models.CharField(max_length=255)
	bg_color = models.CharField(max_length=12)
	def __str__(self):
		return str(self.tag)

	class Meta:
		db_table = 'Tag'
# Creating a model for questions which will be asked by users and will be answered by other users
class Question(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	question = models.TextField()
	tags = models.ManyToManyField(Tags)
	url = models.CharField(max_length=32)
	asked_on = models.DateTimeField(default=timezone.now)
	answers = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)

# Creating a model for answers which will be given by users to the questions asked by other users
class Answer(models.Model):
	answered_by = models.ForeignKey(User,on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.TextField()
	url = models.CharField(max_length=32)
	answered_at = models.DateTimeField(default=timezone.now)
	likes = models.IntegerField(default=0)
	
# Creating a model for likes which will be given by users to the answers
class AnswerLiker(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	liked = models.BooleanField(default=False)

# Creating a model for likes which will be given by users to the questions
class Liker(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	liked = models.BooleanField(default=False)