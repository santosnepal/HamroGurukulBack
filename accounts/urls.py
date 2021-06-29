from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverView, name="api-overview"),
    path('users', views.userList, name="All Avilable Users"),
    path('suser/<str:pk>', views.userSearch, name="search specific user"),
    path('addcourses', views.addCourse, name="Add New Course"),
    path('viewcourses', views.viewCourses, name="View All Courses"),
    path('addsubject', views.addSubject, name="Add Subject"),
    path('viewsubject', views.viewSubject, name="View SUbject")
]
