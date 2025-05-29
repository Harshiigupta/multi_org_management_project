from django.contrib import admin
from django.urls import path, include
#from . import views 


#from django.views.generic import RedirectView
#from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', RedirectView.as_view(url='/organizations/', permanent=False), name='root_redirect'),
    path('admin/', admin.site.urls),
    path('', include('organization.urls')),
   # path('', views.home),
    

]


