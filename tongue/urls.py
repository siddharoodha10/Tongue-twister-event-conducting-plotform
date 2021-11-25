from django.urls import path
from . import views
urlpatterns=[
path("",views.display, name="display"),
path("submit",views.submit,name="submit"),
path("result",views.result),
path("table",views.table),
]