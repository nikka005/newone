from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name="home"),
    path('deposite', views.deposite,name="deposite"),
    path('join', views.join,name="join"),
    path('login', views.login_user,name="login"),
    path('profile', views.profile,name="profile"),
    path('rank', views.rank,name="rank"),
    path('', views.signup,name="signup"),
    path('vote', views.vote,name="vote"),
    path('withdraw', views.withdraw,name="withdraw"),
    path('logout',views.logoutpage,name="logout")
]



