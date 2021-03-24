from django.urls import path
from account.api.views import (
    api_create_account_view,
    api_detail_account_view
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register/', api_create_account_view, name="register"),
    path('login/', obtain_auth_token, name='login'),
    path('get', api_detail_account_view, name="get")
]
