from .serializers import DataStoreSerializer
from .services import data_read_service
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DataStore


class CSVDataReadView(APIView):
    def get(self, request):
        data_update_res = data_read_service('reader/csv_folder/data.csv')
        if data_update_res:
            all_objects = DataStore.objects.all()
            serializer_data = DataStoreSerializer(all_objects, many=True).data
            return Response({"newData": serializer_data},
                            status=status.HTTP_200_OK)
        else:
            return Response("Data Update Got Error. Please Make Data Format correct and then try",
                            status=status.HTTP_400_BAD_REQUEST)
