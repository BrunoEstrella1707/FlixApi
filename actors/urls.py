from django.contrib import admin
from django.urls import path
from actors.views import ActorCreateListView, ActorRetriveUpdateDestroyView


urlpatterns = [
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetriveUpdateDestroyView.as_view(), name='actor-detail-view'),
]