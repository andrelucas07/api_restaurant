"""cardapio URL Configuration

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
from workalove.api.models import Chef, Recipe, Ingredient
from django.contrib import admin
from django.urls import path, include
from workalove.api import viewsets
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'chef', viewsets.ChefViewSet, basename=Chef)
router.register(r'ingredient', viewsets.IngredientViewSet, basename=Ingredient)
router.register(r'recipe', viewsets.RecipeViewSet, basename=Recipe)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
