from rest_framework import serializers


from .models import Chef, Recipe, Ingredient


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = [
            'id', 'name',
        ]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'id', 'name',
        ]


class RecipeSerializer(serializers.ModelSerializer):
    # ingredients = serializers.StringRelatedField(read_only=False, many=True)
    # chef = serializers.StringRelatedField(read_only=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'chef', 'title', 'ingredients'
        ]
