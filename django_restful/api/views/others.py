
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response


class HealthCheckView(ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        return Response("Success")