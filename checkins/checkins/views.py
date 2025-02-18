from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response





from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Times,Users
from .serializers import UsersSerializer,TimesSerializer


class TimesViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many Companies

      serializer_class = TimesSerializer
      queryset = Times.objects.all()

class UsersViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many Companies

      serializer_class = UsersSerializer
      queryset = Users.objects.all()



@api_view(['GET', 'POST'])
def times_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        times = Times.objects.all()
        serializer = TimesSerializer(times, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = TimesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def login(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        times = Users.objects.all()
        serializer = UsersSerializer(times, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"value":1}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#def postTime(request):
#    print 'RECEIVED REQUEST: ' + request.method
#    if request.method == 'POST':
#        print 'Hello'
#    else: #GET
#        return render(request, 'buttonExample.html')
