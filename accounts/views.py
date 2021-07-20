from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.utils.decorators import method_decorator
from .serializers import UserAccountSerializer, CoursesSerializer, SubjectsSerializer, SessionYearModelSerializer, FeedBackStudentSerializer, FeedBackUserAccountSerializer, LeaveReportStudentSerializer, LeaveReportStaffSerializer
from .models import UserAccount, SessionYearModel, Courses, Subjects, FeedBackStudent, FeedBackUserAccount, LeaveReportStudent, LeaveReportStaff

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


@api_view(['GET'])
def useSearchi(request, pk):
    users = UserAccount.objects.filter(id=pk)
    serializer = UserAccountSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCourseName(request, pk):
    courses = Courses.objects.filter(id=pk)
    serializer = CoursesSerializer(courses, many=True)
    return Response(serializer.data)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class getCsrfCookie(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({'sucess': 'CSRF cookie set'})


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
    subjectsa = Subjects.objects.all()
    serializer = SubjectsSerializer(subjectsa, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addSessionYear(request):
    serializer = SessionYearModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def viewSessionYear(request):
    sessionyear = SessionYearModel.object.all()
    serializer = SessionYearModelSerializer(sessionyear, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addStudentFeedBack(request):
    serializer = FeedBackStudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getStudentFeedBack(request):
    feedback = FeedBackStudent.objects.all()
    serializer = FeedBackStudentSerializer(feedback, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addStaffFeedBack(request):
    serializer = FeedBackUserAccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getStaffFeedBack(request):
    feedback = FeedBackUserAccount.objects.all()
    serializer = FeedBackUserAccountSerializer(feedback, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStudentLeave(request):
    leave = LeaveReportStudent.objects.all()
    serializer = LeaveReportStudentSerializer(leave, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addStudentLeave(request):
    serializer = LeaveReportStudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
