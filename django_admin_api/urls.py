
from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index),
    path('/<app_label>/<model_name>/', views.ModelView.as_view()),
    path('/<app_label>/<model_name>/items/', views.ItemsView.as_view()),
    path('/<app_label>/<model_name>/<pk>/', views.ItemView.as_view()),
    path('/<app_label>/<model_name>/<pk>/<field_name>/', views.autocomplete),
    path('/signin', views.signin),
    path('/signout', views.signout),
    path('/info', views.info),
]

