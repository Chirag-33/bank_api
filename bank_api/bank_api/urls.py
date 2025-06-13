"""
URL configuration for bank_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse
from api.views import BankViewSet, BranchViewSet

router = DefaultRouter()
router.register('banks', BankViewSet)
router.register('branches', BranchViewSet)

def root_view(request):
    return JsonResponse({
        "message": "Welcome to the Bank API 👋",
        "available_endpoints": [
            "/api/banks/",
            "/api/branches/"
        ]
    })

urlpatterns = [
    path('', root_view),  
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
