from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view, APIView

from api_app.models import Student
from api_home import serializers
from api_home.permissions import IsAdminOrReadOnly
from api_home.serializers import StudentSerializer
from django.shortcuts import get_object_or_404


# @api_view(['GET'])
# def show_student_data(request):
#     student = {
#         'name':'charles',
#         'level': 'core'
#     }

#     return Response(student)
#api view functions
@api_view(['GET', 'POST'])
def show_student_data(request):
    

    method = request.method
    if method == 'GET':
        students = Student.objects.all()
        serializers = StudentSerializer(students, many=True)
        return Response(serializers.data)
    else:
        serializers  = StudentSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#class api views
class StudentSer(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format = None):
        students = Student.objects.all()
        serializers = StudentSerializer(students, many=True)
        return Response(serializers.data)


    def post(self, request, format = None):
        serializers = StudentSerializer(data = request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDescription(APIView):
    def get_student(self, pk):
        # try:
        #     return Student.objects.get(pk=pk)
        # except Student.DoesNotExist:
        #     return Http404
        return get_object_or_404(Student, pk=pk)
    
    def get(self, request, pk, format = None):
        student = self.get_student(pk)
        serializers = StudentSerializer(student)
        return Response(serializers.data)

#generics
class  StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class StudentCreateAPIView(generics.CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def perform_create(self, serializer):
#         return serializer.save()
        

