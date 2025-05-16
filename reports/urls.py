from django.urls import path
from .views import LoginView,ReportListView,ReportDetailView,ReportSummaryView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('reports', ReportListView.as_view()),
    path('report/<str:report_id>', ReportDetailView.as_view()),
    path('report/<str:report_id>/summary', ReportSummaryView.as_view()),
]
