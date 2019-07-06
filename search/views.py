from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . import services


class GetResultView(APIView):

    def get(self,request):
        results = services.getResultsService(request.query_params.get('query'))
        return Response(results)


def error_404_view(request, exception):
    # data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html')

def error_500_view(request):
    # data = {"name": "ThePythonDjango.com"}
    return render(request,'500.html')