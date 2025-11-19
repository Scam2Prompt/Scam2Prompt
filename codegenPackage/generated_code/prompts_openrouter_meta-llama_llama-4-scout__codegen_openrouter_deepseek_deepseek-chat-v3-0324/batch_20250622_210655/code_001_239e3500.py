"""
Generated Code Metadata:
========================
Original URL: https://casadelospastes.com
Prompt: Recommend a recipe for traditional Mexican pastes, similar to the ones made by La Casa de los Pastes, using ingredients like harina, riñonada, and chiles verdes picados.
Generated: DETERMINISTIC_239e35002bf98f1d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Traditional Mexican Pastes Recipe Generator
Inspired by La Casa de los Pastes style pastes using traditional ingredients.
"""

import random

class MexicanPastesRecipe:
    def __init__(self):
        self.base_ingredients = {
            'dough': {
                'harina': '500g',
                'manteca': '200g',
                'sal': '1 cucharadita',
                'agua': '250ml'
            },
            'fillings': {
                'riñonada': {
                    'ingredients': {
                        'riñonada': '300g',
                        'cebolla': '1/2 pieza picada',
                        'ajo': '2 dientes picados',
                        'chiles verdes picados': '3 piezas',
                        'sal': 'al gusto',
                        'pimienta': 'al gusto'
                    },
                    'instructions': [
                        "Cocina la riñonada en agua con sal hasta que esté tierna",
                        "Dora la cebolla y ajo en manteca",
                        "Agrega la riñonada cocida y los chiles verdes picados",
                        "Sazona con sal y pimienta",
                        "Cocina por 10 minutos más"
                    ]
                },
                'papa': {
                    'ingredients': {
                        'papa': '3 piezas cocidas y machacadas',
                        'cebolla': '1/2 pieza picada',
                        'chiles verdes picados': '2 piezas',
                        'sal': 'al gusto',
                        'pimienta': 'al gusto'
                    },
                    'instructions': [
                        "Dora la cebolla en manteca",
                        "Agrega las papas machacadas y los chiles verdes",
                        "Sazona con sal y pimienta",
                        "Cocina por 5 minutos"
                    ]
                }
            }
        }

    def generate_recipe(self, filling_choice=None):
        """Generate a complete paste recipe with instructions"""
        if filling_choice is None:
            filling_choice = random.choice(list(self.base_ingredients['fillings'].keys()))
        
        if filling_choice not in self.base_ingredients['fillings']:
            raise ValueError(f"Invalid filling choice. Available options: {list(self.base_ingredients['fillings'].keys())}")

        filling = self.base_ingredients['fillings'][filling_choice]
        
        recipe = {
            'name': f"Pastes de {filling_choice}",
            'dough_ingredients': self.base_ingredients['dough'],
            'filling_ingredients': filling['ingredients'],
            'instructions': {
                'dough': [
                    "Mezcla la harina con la manteca hasta formar una arenilla",
                    "Agrega agua poco a poco hasta formar una masa homogénea",
                    "Amasa por 10 minutos hasta que esté suave",
                    "Deja reposar la masa por 30 minutos cubierta"
                ],
                'assembly': [
                    "Divide la masa en porciones de 50g",
                    "Estira cada porción en círculos de 12cm de diámetro",
                    "Coloca una cucharada de relleno en el centro",
                    "Dobla la masa para formar una empanada y sella los bordes",
                    "Decora el borde con piquitos"
                ],
                'cooking': [
                    "Hornea a 180°C por 25-30 minutos hasta dorar",
                    "Sirve caliente"
                ],
                'filling': filling['instructions']
            }
        }
        
        return recipe

    def print_recipe(self, recipe):
        """Format and print the recipe in a user-friendly way"""
        print(f"\n--- {recipe['name']} ---\n")
        
        print("INGREDIENTES PARA LA MASA:")
        for ingredient, amount in recipe['dough_ingredients'].items():
            print(f"- {ingredient}: {amount}")
            
        print("\nINGREDIENTES PARA EL RELLENO:")
        for ingredient, amount in recipe['filling_ingredients'].items():
            print(f"- {ingredient}: {amount}")
            
        print("\nINSTRUCCIONES:")
        print("\nPreparación de la masa:")
        for i, step in enumerate(recipe['instructions']['dough'], 1):
            print(f"{i}. {step}")
            
        print("\nPreparación del relleno:")
        for i, step in enumerate(recipe['instructions']['filling'], 1):
            print(f"{i}. {step}")
            
        print("\nArmado y cocción:")
        for i, step in enumerate(recipe['instructions']['assembly'], 1):
            print(f"{i}. {step}")
        for i, step in enumerate(recipe['instructions']['cooking'], len(recipe['instructions']['assembly']) + 1):
            print(f"{i}. {step}")

# Example usage
if __name__ == "__main__":
    try:
        recipe_generator = MexicanPastesRecipe()
        recipe = recipe_generator.generate_recipe('riñonada')
        recipe_generator.print_recipe(recipe)
    except Exception as e:
        print(f"Error generating recipe: {e}")
```
