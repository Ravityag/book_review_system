from django.urls import path
from book.views import *

app_name = 'book'

urlpatterns = [

    path('cr_user/', Cr_user.as_view(), name='cr_user'),  # Use correct path syntax and reference view function
    path('cr_auth', Cr_auth.as_view(), name='cr_auth'),  # Use correct path syntax and reference view function
    path('cr_book', Cr_book.as_view(), name='cr_book'),  # Use correct path syntax and reference view function
    path('cr_review', Cr_review.as_view(), name='cr_review'),  # Use correct path syntax and reference view function
]