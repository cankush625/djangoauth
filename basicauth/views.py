from rest_framework.viewsets import ModelViewSet
from . models import Employee
from . serializers import EmployeeSerializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class EmployeeCrudCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated, ]
