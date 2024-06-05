from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [

    path('cr_user/', Cr_user.as_view(), name='cr_user'),
    path('cr_auth', Cr_auth.as_view(), name='cr_auth'),
    path('cr_book', Cr_book.as_view(), name='cr_book'),
    path('cr_review', Cr_review.as_view(), name='cr_review'),
    path('loginapi', LoginApi.as_view(), name='loginapi'),
    path('profile', UserProfileView.as_view(), name='profile'),
]