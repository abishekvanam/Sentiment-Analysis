from django.urls import path, include
from . import views
urlpatterns = [
	path('tweet/', views.print_tweets, name = 'print_tweets'),
	path('alltweets/',views.all_tweets, name = 'alltweets'),
	path('',views.positive, name = 'positive'),
	path('negative/',views.negative, name = 'negative'), 
]
