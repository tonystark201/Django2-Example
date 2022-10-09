# * coding:utf-8 *


from api.views.classes import ClassesView, ClassView
from api.views.courses import CoursesView, CourseView
from api.views.others import HealthCheckView
from api.views.scores import ScoresView, ScoreView
from api.views.students import StudentsView, StudentView
from api.views.teachers import TeachersView, TeacherView
from api.views.users import UserLoginView
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/health-check", HealthCheckView.as_view()),
    path("v1/api/login", UserLoginView.as_view()),
    path("v1/api/classes", ClassesView.as_view()),
    re_path("^v1/api/classes/(?P<id>[a-zA-Z0-9_-]+)$", ClassView.as_view()),
    path("v1/api/teachers", TeachersView.as_view()),
    re_path("^v1/api/teachers/(?P<id>[a-zA-Z0-9_-]+)$", TeacherView.as_view()),
    path("v1/api/courses", CoursesView.as_view()),
    re_path("^v1/api/courses/(?P<id>[a-zA-Z0-9_-]+)$", CourseView.as_view()),
    path("v1/api/students", StudentsView.as_view()),
    re_path("^v1/api/students/(?P<id>[a-zA-Z0-9_-]+)$", StudentView.as_view()),
    path("v1/api/scores", ScoresView.as_view()),
    re_path("^v1/api/scores/(?P<id>[a-zA-Z0-9_-]+)$", ScoreView.as_view())
]
