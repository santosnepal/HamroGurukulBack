from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserAccountSerializer, CoursesSerializer, SubjectsSerializer
from .models import UserAccount, SessionYearModel, Courses, Subjects
# Create your views here.


@api_view(['GET'])
def apiOverView(request):

    return Response("SARAL IS NOOB \n He got one Tap Shot in his Head")


@api_view(['GET'])
def userList(request):
    users = UserAccount.objects.all()
    serializer = UserAccountSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userSearch(request, pk):
    users = UserAccount.objects.filter(user_types=pk)
    serializer = UserAccountSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addCourse(request):
    serializer = CoursesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def viewCourses(request):
    courses = Courses.objects.all()
    serializer = CoursesSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addSubject(request):
    serializer = SubjectsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def viewSubject(request):
    subjects = Subjects.objects.all()
    serializer = SubjectsSerializer(subjects, many=True)
    return Response(serializer.data)
