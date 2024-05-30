from .models import *
from .serializers import *

from rest_framework.generics import *
from rest_framework.permissions import *

'''--------------- Permissions -----------------------'''
class IsAdminOrReadOnly(BasePermission):
    """
      Faqat admin foydalanuvchilarga yozish huquqini beradi, boshqalarga faqat o'qish huquqi.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

'''--------------- end permissions --------------------'''



class CourseApiList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class CourseApiDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated]



class TeacherApiList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TeacherApiDetail(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAuthenticated]



class StudentApiList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentApiDetail(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]

