from django.contrib import admin
from . import models


# Register your models here.
from .models import(
	Tweets,
	HashTags,
	Mentions
	)

admin.site.register(Tweets)
admin.site.register(HashTags)
admin.site.register(Mentions)