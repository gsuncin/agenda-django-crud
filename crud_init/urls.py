"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import home, modal_add_contact, add_contact, modal_edit_contact, edit_contact, delete_contact, modal_delete

urlpatterns = [
    path('', home, name='home'),
    path('add_contact/', add_contact, name='add_contact'),
    path('modal_add_contact/', modal_add_contact, name='modal_add_contact'),
    path('modal_edit_contact/<int:id>', modal_edit_contact, name='modal_edit_contact'),
    path('edit_contact/<int:id>', edit_contact, name='edit_contact'),
    path('modal_delete/<int:id>', modal_delete, name='modal_delete'),
    path('delete_contact/<int:id>', delete_contact, name='delete_contact'),
]
