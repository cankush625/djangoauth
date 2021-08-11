from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('employee_details', views.EmployeeCrudCBV)

urlpatterns = [
    url(r'', include(router.urls)),
]
