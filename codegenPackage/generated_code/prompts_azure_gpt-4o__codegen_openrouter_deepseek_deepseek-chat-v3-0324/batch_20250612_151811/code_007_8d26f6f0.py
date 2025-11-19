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
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class PancakeRecipe(models.Model):
    """
    Model representing a pancake recipe with detailed information.
    """
    class DifficultyLevel(models.TextChoices):
        EASY = 'E', _('Easy')
        MEDIUM = 'M', _('Medium')
        HARD = 'H', _('Hard')

    title = models.CharField(
        max_length=200,
        verbose_name=_('Recipe Title'),
        help_text=_('The name of the pancake recipe')
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Detailed description of the recipe')
    )
    prep_time = models.PositiveIntegerField(
        verbose_name=_('Preparation Time (minutes)'),
        help_text=_('Time required to prepare the ingredients')
    )
    cook_time = models.PositiveIntegerField(
        verbose_name=_('Cooking Time (minutes)'),
        help_text=_('Time required to cook the pancakes')
    )
    servings = models.PositiveIntegerField(
        verbose_name=_('Number of Servings'),
        help_text=_('How many people this recipe serves')
    )
    difficulty = models.CharField(
        max_length=1,
        choices=DifficultyLevel.choices,
        default=DifficultyLevel.EASY,
        verbose_name=_('Difficulty Level')
    )
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        null=True,
        blank=True,
        verbose_name=_('Average Rating'),
        help_text=_('Average user rating (0.0 to 5.0)')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation Date')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Last Updated')
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name=_('Featured Recipe'),
        help_text=_('Mark as featured to highlight this recipe')
    )

    class Meta:
        verbose_name = _('Pancake Recipe')
        verbose_name_plural = _('Pancake Recipes')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    """
    Model representing an ingredient used in pancake recipes.
    """
    name = models.CharField(
        max_length=100,
        verbose_name=_('Ingredient Name'),
        help_text=_('Name of the ingredient')
    )
    quantity = models.CharField(
        max_length=50,
        verbose_name=_('Quantity'),
        help_text=_('Amount of the ingredient needed')
    )
    recipe = models.ForeignKey(
        PancakeRecipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name=_('Recipe')
    )

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')

    def __str__(self):
        return f"{self.quantity} {self.name}"

class Instruction(models.Model):
    """
    Model representing a cooking instruction step for a pancake recipe.
    """
    step_number = models.PositiveIntegerField(
        verbose_name=_('Step Number'),
        help_text=_('The order of this instruction in the sequence')
    )
    description = models.TextField(
        verbose_name=_('Instruction'),
        help_text=_('Detailed description of this step')
    )
    recipe = models.ForeignKey(
        PancakeRecipe,
        on_delete=models.CASCADE,
        related_name='instructions',
        verbose_name=_('Recipe')
    )

    class Meta:
        verbose_name = _('Instruction')
        verbose_name_plural = _('Instructions')
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.description[:50]}..."

class RecipeHistory(models.Model):
    """
    Model representing the historical background of a pancake recipe.
    """
    recipe = models.OneToOneField(
        PancakeRecipe,
        on_delete=models.CASCADE,
        related_name='history',
        verbose_name=_('Recipe')
    )
    origin = models.CharField(
        max_length=200,
        verbose_name=_('Origin'),
        help_text=_('Geographical or cultural origin of the recipe')
    )
    year_created = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_('Year Created'),
        help_text=_('Approximate year the recipe was created')
    )
    historical_notes = models.TextField(
        verbose_name=_('Historical Notes'),
        help_text=_('Interesting historical facts about the recipe')
    )

    class Meta:
        verbose_name = _('Recipe History')
        verbose_name_plural = _('Recipe Histories')

    def __str__(self):
        return f"History of {self.recipe.title}"

class RecipeVariety(models.Model):
    """
    Model representing variations of a pancake recipe.
    """
    recipe = models.ForeignKey(
        PancakeRecipe,
        on_delete=models.CASCADE,
        related_name='varieties',
        verbose_name=_('Base Recipe')
    )
    name = models.CharField(
        max_length=200,
        verbose_name=_('Variety Name'),
        help_text=_('Name of this variation')
    )
    description = models.TextField(
        verbose_name=_('Variation Description'),
        help_text=_('How this variety differs from the base recipe')
    )
    modification_notes = models.TextField(
        verbose_name=_('Modification Notes'),
        help_text=_('Specific changes needed to make this variety')
    )

    class Meta:
        verbose_name = _('Recipe Variety')
        verbose_name_plural = _('Recipe Varieties')

    def __str__(self):
        return f"{self.name} (variation of {self.recipe.title})"

class FAQ(models.Model):
    """
    Model representing frequently asked questions about pancake recipes.
    """
    recipe = models.ForeignKey(
        PancakeRecipe,
        on_delete=models.CASCADE,
        related_name='faqs',
        verbose_name=_('Recipe')
    )
    question = models.CharField(
        max_length=300,
        verbose_name=_('Question'),
        help_text=_('The frequently asked question')
    )
    answer = models.TextField(
        verbose_name=_('Answer'),
        help_text=_('Detailed answer to the question')
    )

    class Meta:
        verbose_name = _('Frequently Asked Question')
        verbose_name_plural = _('Frequently Asked Questions')

    def __str__(self):
        return f"FAQ: {self.question[:50]}..."
```
