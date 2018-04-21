from django.conf.urls import url

from api import views

urlpatterns = [
    url('examples/', views.example_list),
    url('examples/<int:example_id>/', views.example_detail),
]