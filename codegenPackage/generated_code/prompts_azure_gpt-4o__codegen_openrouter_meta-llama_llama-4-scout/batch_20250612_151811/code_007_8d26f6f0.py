"""
Generated Code Metadata:
========================
Original URL: https://pancakeswpa.com
Prompt: Write a Django model for storing pancake recipes, including fields for history, varieties, and FAQs, inspired by Pancake World’s detailed content structure.
Generated: DETERMINISTIC_8d26f6f00b695d9d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class PancakeRecipe(models.Model):
    """
    Model representing a pancake recipe.
    """

    class RecipeStatus(models.TextChoices):
        PUBLISHED = 'published', 'Published'
        DRAFT = 'draft', 'Draft'
        ARCHIVED = 'archived', 'Archived'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=RecipeStatus.choices, default=RecipeStatus.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """
    Model representing an ingredient in a pancake recipe.
    """

    recipe = models.ForeignKey(PancakeRecipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"


class Instruction(models.Model):
    """
    Model representing an instruction in a pancake recipe.
    """

    recipe = models.ForeignKey(PancakeRecipe, on_delete=models.CASCADE, related_name='instructions')
    step = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField()

    def __str__(self):
        return f"Step {self.step}: {self.description}"


class PancakeRecipeHistory(models.Model):
    """
    Model representing the history of a pancake recipe.
    """

    recipe = models.ForeignKey(PancakeRecipe, on_delete=models.CASCADE, related_name='history')
    updated_at = models.DateTimeField(auto_now_add=True)
    changes = models.TextField()

    def __str__(self):
        return f"History for {self.recipe.name} - {self.updated_at}"


class PancakeRecipeVariety(models.Model):
    """
    Model representing a variety of a pancake recipe.
    """

    recipe = models.ForeignKey(PancakeRecipe, on_delete=models.CASCADE, related_name='varieties')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Variety: {self.name} for {self.recipe.name}"


class PancakeRecipeFAQ(models.Model):
    """
    Model representing a FAQ for a pancake recipe.
    """

    recipe = models.ForeignKey(PancakeRecipe, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"FAQ for {self.recipe.name}: {self.question}"
```

```python
# admin.py
from django.contrib import admin
from .models import PancakeRecipe, Ingredient, Instruction, PancakeRecipeHistory, PancakeRecipeVariety, PancakeRecipeFAQ

admin.site.register(PancakeRecipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(PancakeRecipeHistory)
admin.site.register(PancakeRecipeVariety)
admin.site.register(PancakeRecipeFAQ)
```

```python
# apps.py
from django.apps import AppConfig

class PancakeRecipeAppConfig(AppConfig):
    name = 'pancake_recipe'
    verbose_name = "Pancake Recipes"

    def ready(self):
        import pancake_recipe.signals  # noqa
```
