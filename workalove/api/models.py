from django.db import models


class Chef(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return '%d: %s' % (self.id, self.name)


    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%d: %s' % (self.id, self.name)
        

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Recipe(models.Model):
    title = models.CharField(max_length=120)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return '%d: %s' % (self.id, self.title)


    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
