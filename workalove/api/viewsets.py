from workalove.api.serializers import ChefSerializer, RecipeSerializer, IngredientSerializer
from .models import Chef, Recipe, Ingredient

from rest_framework.response import Response
from rest_framework import viewsets


class ChefViewSet(viewsets.ModelViewSet):
    serializer_class = ChefSerializer

    def get_queryset(self):
        queryset = Chef.objects.all()

        return queryset

    def create(self, request, *args, **kwargs):
        chef_data = request.data

        new_chef = Chef(name=chef_data["name"])
        if new_chef.name.isdigit():
            return Response('field must be string.', status=422)

        serializer = ChefSerializer(data={"name": new_chef.name})

        if serializer.is_valid():
            new_chef.save()
            return Response(serializer.data, status=201)

        return Response('field must be filled.', status=422)

    def list(self, request):
        queryset = Chef.objects.all()
        serializer_class = ChefSerializer(queryset, many=True)

        return Response(serializer_class.data)

    def destroy(self, request, pk):
        try:
            Chef.objects.get(pk=pk).delete()
        except Exception:
            return Response("Chef doesn't exists.", status=404)

        return Response('Chef deleted.', status=204)


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        recipe_data = request.data

        new_recipe = Recipe(chef=Chef.objects.get(
            id=recipe_data["chef"]),
            title=recipe_data["title"],
            )

        if new_recipe.title.isdigit():
            return Response('field must be string.')

        ingredients_list = Ingredient.objects.filter(id__in=request.POST.getlist("ingredients"))

        serializer = RecipeSerializer(data={
            "id": new_recipe.id,
            "chef": new_recipe.chef.pk, 
            "title": new_recipe.title,
            "ingredients": [i.pk for i in ingredients_list]
            },)

        if serializer.is_valid():
            new_recipe.save()
            new_recipe.ingredients.add(*ingredients_list)
            return Response(serializer.data)

        return Response('fields must be filled.')

    def list(self, request):      
        param_search_chef = self.request.query_params.get("chef")
        param_search_title = self.request.query_params.get("title")

        if param_search_chef and param_search_title:

            queryset = Recipe.objects.filter(
                chef__name__icontains=param_search_chef, 
                title__icontains=param_search_title
                )
            
            serializer = RecipeSerializer(data=queryset, many=True)

            serializer.is_valid()

            return Response(serializer.data)
            
        else:
            if param_search_chef:
                queryset = Recipe.objects.filter(chef__name__icontains=param_search_chef)
                serializer = RecipeSerializer(data=queryset, many=True)

                serializer.is_valid()

                return Response(serializer.data)

            elif param_search_title:
                queryset = Recipe.objects.filter(title__icontains=param_search_title)
                serializer = RecipeSerializer(data=queryset, many=True)

                serializer.is_valid()

                return Response(serializer.data)

            recipe  = Recipe.objects.all()
            serializer_class = RecipeSerializer(recipe, many=True)

            return Response(serializer_class.data)

    def destroy(self, request, pk):
        try:
            Recipe.objects.filter(id=pk).delete()
        except Exception:
            return Response("Recipe doesn't exists.", status=404)

        return Response('Recipe deleted.', status=204)

    def retrieve(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            serializer = RecipeSerializer(recipe)

            return Response(serializer.data)

        except Exception:
            return Response("Recipe doesn't exist.", status=404)


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        queryset = Ingredient.objects.all()

        return queryset

    def create(self, request, *args, **kwargs):
        ingredient_data = request.data

        new_ingredient = Ingredient(name=ingredient_data["name"])

        if new_ingredient.name.isdigit():
            return Response('field must be string.')

        serializer = IngredientSerializer(data={"name": new_ingredient.name})

        if serializer.is_valid():
            new_ingredient.save()

            return Response(serializer.data)

        return Response('field must be filled.')

    def list(self, request):

        queryset = Ingredient.objects.all()

        serializer_class = IngredientSerializer(queryset, many=True)

        return Response(serializer_class.data)

    def destroy(self, request, pk):
        try:
            Ingredient.objects.get(pk=pk).delete()
        except Exception:
            return Response("Recipe doesn't exists", status=404)
        
        return Response('Ingredient deleted!', status=204)
