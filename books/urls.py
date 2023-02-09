from django.urls import path

# Local
from .views import BookListView

urlpatterns = [
    path("", BookListView.as_view(), name="home"),

]
