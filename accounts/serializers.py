from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name',
                  'last_name', 'password', 'user_types',)


class SessionYearModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionYearModel
        fields = ['id', 'session_start_year', 'session_end_year', ]


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'course_name', 'created_at', 'updated_at']


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'subject_name', 'course_id',
                  'staff_id', 'created_at', 'updated_at']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'subject_id', 'attendance_date',
                  'session_year_id', 'created_at', 'updated_at']


class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = ['id', 'student_id', 'attendance_id',
                  'status', 'created_at', 'updated_at']


class LeaveReportStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStudent
        fields = ['id', 'student_id', 'leave_date', 'leave_message',
                  'leave_status', 'created_at', 'updated_at']


class LeaveReportStaffStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStaff
        fields = ['id', 'staff_id', 'leave_date', 'leave_message',
                  'leave_status', 'created_at', 'updated_at']


class FeedBackStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackStudent
        fields = ['id', 'student_id', 'feedback',
                  'feedback_reply', 'created_at', 'updated_at']


class FeedBackUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackUserAccount
        fields = ['id', 'staff_id', 'feedback',
                  'feedback_reply', 'created_at', 'updated_at']


class NotificationStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStudent
        fields = ['id', 'student_id', 'message', 'created_at', 'updated_at']


class NotificationUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationUserAccount
        fields = ['id', 'staff_id', 'message', 'created_at', 'updated_at']


class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        fields = ['id', 'subject_id', 'student_id', 'subject_exam_marks',
                  'subject_assignment_marks', 'created_at', 'updated_at']
