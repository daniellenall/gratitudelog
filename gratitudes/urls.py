from django.urls import path
from . import views

app_name = "gratitudes"

urlpatterns = [
    path('new/', views.createnew, name="createnew"),
    path('delete/<int:id>', views.delete, name="delete"),

]