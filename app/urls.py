from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(success_url = 'success'), name='signup'),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
    path('success',views.success,name='success')

]