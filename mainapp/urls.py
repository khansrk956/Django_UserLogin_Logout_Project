from django.urls import path
from mainapp import views
from django.contrib.auth import views as auth_views
"""
URL configuration for authentication project.
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    # Password Change.
    path('password_change/',auth_views.PasswordChangeView.as_view(), name='password_change'), 
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]