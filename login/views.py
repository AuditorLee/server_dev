from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import check_password, make_password
from .serializer import LoginUserSerializer

# Create your views here.

class AppLogout(APIView):
    def post(self, request):
        # 로그아웃한 시간
        return Response(status=200)

class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(dict(msg='로그인에 실패했습니다.'))
        
        if check_password(user_pw, user.user_pw):
            return Response(dict(msg='{}님 로그인 성공'.format(user_id)))
        else:
            return Response(dict(msg='로그인에 실패했습니다.'))

# 비밀번호 찾기, 비밀번호 초기화

class RegistUser(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        user_pw = request.data['user_pw']

        if user_id == '' or user_id is None or user_pw == '' or user_pw is None:
            return Response(data=dict(msg='아이디와 비밀번호를 입력해주세요.'))

        if LoginUser.objects.filter(user_id=user_id).exists():
            return Response(data=dict(msg='이미 존재하는 아이디입니다.'))

        user_pw = make_password(user_pw)
        
        LoginUser.objects.create(user_id=user_id, user_pw=user_pw)

        return Response(data=dict(msg='회원가입에 성공했습니다.', user_id=user_id))

# class RegistUser(APIView):
#     def post(self, request):
#         # user_id = request.data.get('user_id')
#         # user_pw = request.data.get('user_pw')
#         # name = request.data.get('name', "")
#         # birth_day = request.data.get('birth_day', None)
#         # gender = request.data.get('gender', 'male')
#         # email = request.data.get('email', "")
#         # age = request.data.get('age', 3)
#         # user_pw_encrypted = make_password(user_pw)

#         # if user_id 가 특수문자인지, 숫자인지, 한글인지...

#         # if LoginUser.objects.filter(user_id=user_id).exists():
#         #     user = LoginUser.objects.filter(user_id=user_id).first()
#         #     data = dict(
#         #         msg='이미 존재하는 아이디입니다.',
#         #         user_id=user.user_id,
#         #         user_pw=user.user_pw
#         #     )
#         #     return Response(data)
#        
#         # if user is not None:
#         #     return Response(dict(msg='동일한 아이디가 있습니다.'))

#         # LoginUser.objects.create(user_id=user_id, user_pw=user_pw_encrypted, name=name, birth_day=birth_day, gender=gender, email=email, age=age)

#         # # as-is
#         # data = dict(
#         #     user_id = user_id,
#         #     user_pw = user_pw_encrypted,
#         #     name=name,
#         #     birth_day=birth_day,
#         #     gender=gender,
#         #     email=email,
#         #     age=age
#         # )

#         # to-be
#         # user = Serialize(Input)
#         # Django-Rest-Framework 공식 홈페이지에서 Tutorial에 있는 Serialize 예제 참고
#         # dict()을 Serialize(Input) 한줄로 끝

#         # return Response(data)



#         serializer = LoginUserSerializer(request.data)

#         if LoginUser.objects.filter(user_id=serializer.data['user_id']).exists():
#             # DB에 있는 값 출력할 때 어떻게 나오는지 보려고 user 객체를 담음
#             user = LoginUser.objects.filter(user_id=serializer.data['user_id']).first()
#             data = dict(
#                 msg='이미 존재하는 아이디입니다.',
#                 user_id=user.user_id,
#                 user_pw=user.user_pw
#             )
#             return Response(data)

#         user = serializer.create(request.data)

#         return Response(data=LoginUserSerializer(user).data)
