"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python script to categorize tools and machinery for a Brazilian manufacturing company, including categories like 'ferramenta instrumental', 'maquinaria', and 'aparelhagem'.
Generated: DETERMINISTIC_e60b531f115342c6
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to categorize tools and machinery for a Brazilian manufacturing company.
Categories include 'ferramenta instrumental', 'maquinaria', and 'aparelhagem'.
"""

import json

# Define categories
CATEGORIES = {
    "ferramenta instrumental": ["chave de fenda", "martelo", "alicate", "serrote"],
    "maquinaria": ["tornos", "fresadoras", "prensas hidráulicas", "empilhadeiras"],
    "aparelhagem": ["medidor de pressão", "osciloscópio", "balança digital", "termômetro"]
}

def categorize_item(item_name):
    """
    Categorize a given item based on predefined categories.

    Args:
        item_name (str): Name of the item to categorize.

    Returns:
        str: Category name if found, otherwise 'Categoria desconhecida'.
    """
    for category, items in CATEGORIES.items():
        if item_name.lower() in [i.lower() for i in items]:
            return category
    return "Categoria desconhecida"

def main():
    """
    Main function to interact with the user and categorize items.
    """
    print("Bem-vindo ao sistema de categorização de ferramentas e máquinas!")
    print("Categorias disponíveis: 'ferramenta instrumental', 'maquinaria', 'aparelhagem'")
    print("Digite 'sair' para encerrar o programa.\n")

    while True:
        try:
            # Get user input
            item_name = input("Digite o nome do item para categorizar: ").strip()
            
            # Exit condition
            if item_name.lower() == "sair":
                print("Encerrando o programa. Até logo!")
                break
            
            # Categorize the item
            category = categorize_item(item_name)
            print(f"O item '{item_name}' pertence à categoria: {category}\n")
        
        except Exception as e:
            # Handle unexpected errors
            print(f"Ocorreu um erro: {e}. Por favor, tente novamente.\n")

if __name__ == "__main__":
    main()
```
