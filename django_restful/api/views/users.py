# * coding:utf-8 *
from common.models import Users
from common.utils import JwtUtils
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class UserLoginView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        username = request.data.get("name", "")
        password = request.data.get("password", "")
        res = JwtUtils.get_token(username, password)
        user = Users.objects.filter(name=username, password=password).first()
        user = model_to_dict(user)
        user["jwt"] = res
        return Response(user, status=status.HTTP_200_OK)
