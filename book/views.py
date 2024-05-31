from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Author, UserTab, Review, Book
from datetime import datetime

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Cr_user(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        form = request.data
        full_name = form.get('full_name')
        mobile = form.get('mobile')
        date_format = '%Y-%m-%d'
        start_date = form.get('start_date')
        if start_date:
            start_date_new = datetime.strptime(str(start_date), date_format)
        else:
            start_date_new = None
        end_date = form.get('end_date')
        if end_date:
            end_date_new = datetime.strptime(str(end_date), date_format)
        else:
            end_date_new = None
        username = form.get('username')
        pswrd = form.get('pswrd')
        email = form.get('email')
        result = {}
        if username is None:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)

        if len(username) == 0:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            author = UserTab.objects.create_user(username=username,
                                              password=pswrd,
                                              email=email,
                                              full_name=full_name,
                                              mobile=mobile,
                                              start_date=start_date_new,
                                              end_date=end_date_new
                                              )
            result = {'error': False, 'error_code': 201, 'error_description': 'Created successfully'}
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            result = {'error': True, 'error_code': 500, 'error_description': 'Internal Server Error'}
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Cr_auth(APIView):
    def post(self, request):
        form = request.data
        name = form.get('name')
        bio = form.get('bio')
        result = {}

        if name is None:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)

        if len(name) == 0:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            author = Author.objects.create(au_name=name, au_bio=bio)
            result = {'error': False, 'error_code': 201, 'error_description': 'Created successfully'}
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            result = {'error': True, 'error_code': 500, 'error_description': 'Internal Server Error'}
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Cr_book(APIView):
    def post(self, request):
        form = request.data
        bo_au = form.get('bo_au')
        bo_title = form.get('bo_title')
        bo_isbn = form.get('bo_isbn')

        result = {}

        if bo_title is None:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)

        if len(bo_title) == 0:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            author = Book.objects.create_user(bo_au_id=bo_au,
                                              bo_title=bo_title,
                                              bo_isbn=bo_isbn
                                              )
            result = {'error': False, 'error_code': 201, 'error_description': 'Created successfully'}
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            result = {'error': True, 'error_code': 500, 'error_description': 'Internal Server Error'}
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Cr_review(APIView):
    def post(self, request):
        form = request.data
        rv_user = form.get('rv_user')
        rv_book = form.get('rv_book')
        rv_rating = form.get('rv_rating')
        rv_comment = form.get('rv_comment')
        result = {}
        if rv_rating is None:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)

        if len(rv_rating) == 0:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            author = Review.objects.create_user(rv_user_id=rv_user,
                                                rv_book_id=rv_book,
                                                rv_rating=rv_rating,
                                                rv_comment=rv_comment
                                                )
            result = {'error': False, 'error_code': 201, 'error_description': 'Created successfully'}
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            result = {'error': True, 'error_code': 500, 'error_description': 'Internal Server Error'}
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


