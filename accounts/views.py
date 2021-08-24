from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.utils.decorators import method_decorator
from .serializers import UserAccountSerializer, CoursesSerializer, StudentResultSerializer, SubjectsSerializer, SessionYearModelSerializer, FeedBackStudentSerializer, FeedBackUserAccountSerializer, LeaveReportStudentSerializer, LeaveReportStaffSerializer, AttendanceReportSerializer, AttendanceSerializer, NotificationUserAccountSerializer, NotificationStudentSerializer, EnrollStudentSerializer
from .models import UserAccount, SessionYearModel, StudentResult, Courses, Subjects, FeedBackStudent, FeedBackUserAccount, LeaveReportStudent, LeaveReportStaff, AttendanceReport, Attendance, NotificationUserAccount, NotificationStudent, enroledstudent

# Create your views here.


@api_view(['POST'])
def addresult(request):
    serializer = StudentResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getresult(request, pk):
    result = StudentResult.objects.filter(subject_id=pk)
    serializer = StudentResultSerializer(result, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getresultByStudent(request, pk):
    result = StudentResult.objects.filter(student_id=pk)
    serializer = StudentResultSerializer(result, many=True)
    return Response(serializer.data)


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


@api_view(['GET'])
def viewSubjectById(request, pk):
    subjectsa = Subjects.objects.all(id=pk)
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


@api_view(['GET'])
def getStaffLeave(request):
    leave = LeaveReportStaff.objects.all()
    serializer = LeaveReportStaffSerializer(leave, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addStaffLeave(request):
    serializer = LeaveReportStaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getatendance(request):
    attendance = Attendance.objects.all()
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getatendanceById(request, pk):
    attendance = Attendance.objects.filter(id=pk)
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addatendance(request):
    serializer = AttendanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getattendancereport(request, pkss):
    attendancereport = AttendanceReport.objects.filter(attendance_id=pkss)
    serializer = AttendanceReportSerializer(attendancereport, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getattendancereportById(request, pkss):
    attendancereport = AttendanceReport.objects.filter(student_id=pkss)
    serializer = AttendanceReportSerializer(attendancereport, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addattendancereport(request):
    serializer = AttendanceReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getattendancedate(request, sid, ssid):
    attendancedate = Attendance.objects.filter(
        subject_id=sid, session_year_id=ssid)
    serializer = AttendanceSerializer(attendancedate, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def sendstafffnotification(request):
    serializer = NotificationUserAccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getstaffnotification(request, pk):
    notification = NotificationUserAccount.objects.filter(staff_id=pk)
    serializer = NotificationUserAccountSerializer(notification, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def sendstudentnotification(request):
    serializer = NotificationStudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getstudentnotification(request, pk):
    notification = NotificationStudent.objects.filter(student_id=pk)
    serializer = NotificationStudentSerializer(notification, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addenroledstudent(request):
    serializer = EnrollStudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getenroledstudent(request):
    enroled = enroledstudent.objects.all()
    serializer = EnrollStudentSerializer(enroled, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def editresult(request, pk):
    result = StudentResult.objects.get(id=pk)
    data = request.data
    serializer = StudentResultSerializer(result, data=request.data)
    # print(result)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['PUT'])
def editcourse(request, pk):
    attn = Courses.objects.get(id=pk)
    serializer = CoursesSerializer(attn, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['PUT'])
def editsub(request, pk):
    attn = Subjects.objects.get(id=pk)
    serializer = SubjectsSerializer(attn, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['PUT'])
def editattendance(request, pk):
    attn = AttendanceReport.objects.get(id=pk)
    serializer = AttendanceReportSerializer(attn, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET'])
def getSubject(request, pk):
    subjectsa = Subjects.objects.filter(staff_id=pk)
    serializer = SubjectsSerializer(subjectsa, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getsbycid(request,pk):
    sc = Subjects.objects.filter(course_id=pk)
    serializer = SubjectsSerializer(sc,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStaffLeavebyid(request, pk):
    leave = LeaveReportStaff.objects.filter(staff_id=pk)
    serializer = LeaveReportStaffSerializer(leave, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getstudentleaveById(request, pk):
    leave = LeaveReportStudent.objects.filter(student_id=pk)
    serializer = LeaveReportStudentSerializer(leave, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStaffFeedBackById(request, pk):
    feedback = FeedBackUserAccount.objects.filter(staff_id=pk)
    serializer = FeedBackUserAccountSerializer(feedback, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getstudentfeedBackByID(request, pk):
    feedback = FeedBackStudent.objects.filter(student_id=pk)
    serializer = FeedBackStudentSerializer(feedback, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def editstafffeedback(request, pk):
    fback = FeedBackUserAccount.objects.get(id=pk)
    serializer = FeedBackUserAccountSerializer(fback, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['PUT'])
def editstudentfeedback(request, pk):
    fback = FeedBackStudent.objects.get(id=pk)
    serializer = FeedBackStudentSerializer(fback, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['PUT'])
def editstudentleave(request, pk):
    fback = LeaveReportStudent.objects.get(id=pk)
    serializer = LeaveReportStudentSerializer(fback, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['PUT'])
def editstaffleave(request, pk):
    fback = LeaveReportStaff.objects.get(id=pk)
    serializer = LeaveReportStaffSerializer(fback, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['PUT'])
def edituser(request, pk):
    fback = UserAccount.objects.get(id=pk)
    serializer = UserAccountSerializer(fback, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['DELETE'])
def deletesubject(request, pk):
    sub = Subjects.objects.get(id=pk)
    if(sub.delete()):
        return Response('200ok')

    else:
        return Response('sorry')


@api_view(['DELETE'])
def deletecourses(request, pk):
    sub = Courses.objects.get(id=pk)
    if(sub.delete()):
        return Response('200ok')

    else:
        return Response('sorry')


@api_view(['DELETE'])
def deletestudent(request, pk):
    sub = UserAccount.objects.get(id=pk)
    if(sub.delete()):
        return Response('200ok')

    else:
        return Response('sorry')
@api_view(['GET'])
def getsbycid(request,pk):
    sc = Subjects.objects.filter