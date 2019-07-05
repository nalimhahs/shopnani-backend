from rest_framework.views import APIView
from rest_framework.response import Response

from . import services


class GetResultView(APIView):

    def get(self,request):
        results = services.getResultsService(request.query_params.get('query'))
        return Response(results)
