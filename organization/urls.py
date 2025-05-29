
                   ####  1  start  ###
# from django.urls import path
# from . import views
# #from django.shortcuts import redirect
# from django.contrib.auth import views as auth_views


# urlpatterns = [
#     path('organizations/', views.organization_list, name='organization_list'),
#     path('organizations/create/', views.organization_create, name='organization_create'),
#     path('users/', views.user_list, name='user_list'),
#     path('users/create/', views.user_create, name='user_create'),
#     path('users/<int:user_id>/assign-role/', views.assign_role, name='assign_role'),
#     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

#     path('dashboard/', views.dashboard, name='dashboard'),
#     # path('', views.home),
# ]


                
                     ###     2   ###



# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views
# from django.shortcuts import redirect

# urlpatterns = [
#     path('organizations/', views.organization_list, name='organization_list'),
#     path('organizations/create/', views.organization_create, name='organization_create'),
#     path('users/', views.user_list, name='user_list'),
#     path('users/create/', views.user_create, name='user_create'),
#     path('users/<int:user_id>/assign-role/', views.assign_role, name='assign_role'),
#     path('login/', auth_views.LoginView.as_view(template_name='organization/login.html'), name='login'),
#     path('dashboard/', views.dashboard, name='dashboard'),

#     # Add this line:
#     path('', lambda request: redirect('login')),  # or use 'dashboard'
# ]


                      ###  3   redirect step by step    ###



from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Redirect root path to dashboard
    path('', views.dashboard, name='dashboard'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='organization/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Organizations
    path('organizations/', views.organization_list, name='organization_list'),
    path('organizations/create/', views.organization_create, name='organization_create'),

    # Users
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/assign-role/', views.assign_role, name='assign_role'),
]
