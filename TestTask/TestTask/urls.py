"""TestTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django_registration.backends.one_step.views import RegistrationView

from app.forms import CustomUserForm
from app.views import IndexTemplateView, TestModelListJson, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("accounts/register",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/"
         ), name="django_registration_register"),

    path('', IndexTemplateView.as_view(), name="entry-point"),
    path('testmodel_data/', TestModelListJson.as_view(),
         name="testmodel_list_json"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name="delete")




]
