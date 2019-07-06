from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . import services

# Accepts the query through the get request and passes it to the get results 
# service and returns the data as the response


class GetResultView(APIView):

    def get(self, request):
        results = services.getResultsService(request.query_params.get('query'))
        return Response(results)


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500_view(request):
    return render(request, '500.html')
