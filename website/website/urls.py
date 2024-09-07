"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from signup.views import register
from login.views import login_view
from django.contrib.auth import views as auth_views
from django.urls import path
from login.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", register),
    path("login/", login_view),
    path("forget/", login_view),
    path('', include('django.contrib.auth.urls')),


    #path('password_reset/', include('password_reset.urls', namespace='password_reset')),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),name='password_reset_form'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error")
]
