from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from .models import User, Job, JobApplication
from .serializers import (
    UserSignupSerializer,
    JobSerializer,
    JobApplicationSerializer
)
class SignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IsCompany(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'company'


class IsApplicant(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'applicant'


class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsCompany]

    def perform_create(self, serializer):
        serializer.save(company=self.request.user)


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsCompany]

    def perform_update(self, serializer):
        serializer.save(company=self.request.user)


class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsApplicant]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


class ApplicantApplicationListView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsApplicant]

    def get_queryset(self):
        return JobApplication.objects.filter(applicant=self.request.user).order_by('-applied_at')
