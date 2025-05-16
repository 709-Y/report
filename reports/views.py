
from .utils import load_users,load_reports
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import load_reports, generate_summary
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        users = load_users()
        for user in users:
            if user['email'] == email:
                return Response({'message': 'Login successful', 'user': user}, status=status.HTTP_200_OK)

        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
class ReportListView(APIView):
    def get(self, request):
        user_id = request.GET.get('user_id')
        if not user_id:
            return Response({"error": "Missing user_id"}, status=status.HTTP_400_BAD_REQUEST)

        reports = load_reports()
        user_reports = [r for r in reports if r["user_id"] == user_id]
        return Response(user_reports)
class ReportDetailView(APIView):
    def get(self, request, report_id):
        reports = load_reports()
        print("Loaded Reports:", reports)  # 👈 加这一行
        report = next((r for r in reports if r["report_id"] == report_id), None)
        if report:
            return Response(report)
        else:
            return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)

class ReportSummaryView(APIView):
    def post(self, request, report_id):
        reports = load_reports()
        report = next((r for r in reports if r["report_id"] == report_id), None)

        if not report:
            return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)

        content = report.get("content", "")
        if not content:
            return Response({"error": "Report content is empty"}, status=status.HTTP_400_BAD_REQUEST)

        # 调用摘要函数，可能返回真实或模拟结果
        summary = generate_summary(content)

        # 判断是否是模拟摘要（你可以在 utils.py 中做标记返回）
        return Response({
            "report_id": report_id,
            "summary": summary
        }, status=status.HTTP_200_OK)