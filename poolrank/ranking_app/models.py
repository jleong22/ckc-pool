from django.db import models
from django.contrib.auth.models import User

class Ranking(models.Model):
	rating = models.DecimalField(max_digits=21, decimal_places=15)
	num_wins = models.IntegerField()
	num_matches = models.IntegerField()
	user = models.ForeignKey('User')

class Match(models.Model):
	winner_id = models.IntegerField()
	looser_id = models.IntegerField()
	date = models.DateField(auto_now=False, auto_now_add=True)
	is_verified = models.BooleanField()
