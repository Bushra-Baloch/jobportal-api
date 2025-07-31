
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignupView, JobCreateView, JobListView, JobDetailView
from .views import JobApplicationCreateView, ApplicantApplicationListView
urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', TokenObtainPairView.as_view()),  # JWT login
      # Job URLs
    path('jobs/', JobListView.as_view()),           # Anyone can view jobs
    path('jobs/create/', JobCreateView.as_view()),  # Only companies
    path('jobs/<int:pk>/', JobDetailView.as_view()),  # Edit/Delete job (company only)

    path('apply/', JobApplicationCreateView.as_view()),  # Apply to job
    path('my-applications/', ApplicantApplicationListView.as_view()),  # View own applications
]






