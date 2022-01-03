from django.urls import path
from AppLogin import views

app_name = "AppLogin"

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit'),
]
