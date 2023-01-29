from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
<<<<<<< HEAD
    path('signin', views.signin, name='signin'),
    path('logout', views.signin, name='logout'),
    path('settings', views.settings, name='settings'),
]
=======
]
>>>>>>> 40a2cc41111b1e0a6b7d4c13d991628edb41a284
