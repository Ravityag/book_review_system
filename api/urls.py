from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [

    path('register/', Cr_user.as_view(), name='register'),
    path('cr_auth', Cr_auth.as_view(), name='cr_auth'),
    path('cr_book', Cr_book.as_view(), name='cr_book'),
    path('cr_review', Cr_review.as_view(), name='cr_review'),
    path('token/', LoginApi.as_view(), name='token'),
    path('profile', UserProfileView.as_view(), name='profile'),

    path('authors/<int:id>', ListAuthors.as_view(), name="authors"),
    path('authors/', ListAuthors.as_view(), name="authors"),

]