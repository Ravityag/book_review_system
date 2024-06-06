from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Author, UserTab, Review, Book
from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.renderers import UserRenderer



class Cr_user(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        form = request.data
        full_name = form.get('full_name')
        mobile = form.get('mobile')
        date_format = '%Y-%m-%d'
        start_date = form.get('start_date')
        if start_date:
            start_date_new = datetime.strptime(start_date, '%d-%m-%Y').strftime('%Y-%m-%d')
        else:
            start_date_new = None
        end_date = form.get('end_date')
        if end_date:
            end_date_new = datetime.strptime(end_date, '%d-%m-%Y').strftime('%Y-%m-%d')
        else:
            end_date_new = None
        username = form.get('username')
        password = form.get('password')
        email = form.get('email')
        result = {}
        if username is None:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)

        if len(username) == 0:
            return Response({'error': True, 'error_code': 400, 'error_description': 'Name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            author = UserTab.objects.create_user(username=username,
                                              password=password,
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



class LoginApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.validated_data['username']
                password = serializer.validated_data['password']
                user = authenticate(username=username, password=password)

                if not user:
                    return Response({'error': True, 'error_code': 400, 'error_description': 'Invalid Password'},
                                    status=status.HTTP_400_BAD_REQUEST)
                if user.is_active is False:
                    return Response({'error': True, 'error_code': 400, 'error_description': 'Account Not activated'},
                                    status=status.HTTP_400_BAD_REQUEST)
                else:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    })

            else:
                return Response({'error': True, 'error_code': 400, 'error_description': 'Invalid User'},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTab
        fields = ['username', 'password']


class ListAuthors(APIView):
    def get(self, request,id=0):
        if id==0:
            queryset = Author.objects.all()
        else:
            queryset = Author.objects.filter(au_id=id)
        result = {}
        if not queryset:
            result = {}
            result['error'] = False
            result['error_code'] = 200
            result['error_description'] = 'No Author found'
            result['action_list'] = ''
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        else:
            listt = []
            for obj in queryset:
                dictt = {}
                dictt['Author_ID'] = obj.au_id
                dictt['Author_CODE'] = obj.au_name
                dictt['Author_NAME'] = obj.au_bio

                listt.append(dictt)

            result['error'] = False
            result['error_code'] = 200
            result['error_description'] = 'Author List'
            result['action_list'] = listt

            return Response(result, status=status.HTTP_201_CREATED)