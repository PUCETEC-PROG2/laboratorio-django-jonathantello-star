from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),

    path("trainers/", views.trainers, name="trainers"),
    path("trainers/<int:trainer_id>/", views.trainer, name="trainer"),
]
