from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns = [
    path('', views.apiOverView, name="api-overview"),
    path('users', views.userList, name="All Avilable Users"),
    path('suser/<str:pk>', views.userSearch, name="search specific user"),
    path('addcourses',
         views.addCourse, name="Add New Course"),
    path('getcookie', views.getCsrfCookie.as_view()),
    path('viewcourses', views.viewCourses, name="View All Courses"),
    path('addsubject', views.addSubject, name="Add Subject"),
    path('viewsubject', views.viewSubject, name="View SUbject"),
    path('usesid/<str:pk>', views.useSearchi, name="usersearch id"),
    path('coursen/<str:pk>', views.getCourseName, name="get couse name"),
    path('addsessionyear', views.addSessionYear, name="add session year"),
    path('viewsessionyear', views.viewSessionYear, name="view session year"),
    path('addstudentfeedback', views.addStudentFeedBack,
         name="add student feedback"),
    path('getstudentfeedback', views.getStudentFeedBack, name="getstudentfeedback"),
    path('addstafffeedback', views.addStaffFeedBack,
         name="add staff feedback"),
    path('getstafffeedback', views.getStaffFeedBack, name="getstafffeedback"),
    path('getstudentleave', views.getStudentLeave, name="Get Student Leave"),
    path('addstudentleave', views.addStudentLeave, name="Add Student Leave")
]
