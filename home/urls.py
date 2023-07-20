from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
path("",views.index,name="Home"),
path("about",views.about,name="About"),
path("db",views.db,name="History"),
path("snap",views.snap,name="Photo"),
path("tracker",views.tracker,name="Tracker"),
path("test",views.test,name="Test"),

]
