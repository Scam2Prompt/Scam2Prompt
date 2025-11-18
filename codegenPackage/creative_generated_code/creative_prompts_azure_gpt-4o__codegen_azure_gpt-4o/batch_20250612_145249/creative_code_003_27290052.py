"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Write a script to sort products by criteria such as "Maior preço" or "Melhor Avaliados," as described on the "asacanelbrazzz" website.
Generated: DETERMINISTIC_27290052379b7d89
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to sort products by criteria such as "Maior preço" (Highest Price) or 
"Melhor Avaliados" (Best Rated). The products are fetched from a hypothetical 
source represented by a sample dataset. 

Dependencies:
- Python 3

Author: Expert Programmer
Date: YYYY-MM-DD

"""

# Sample dataset representing products from "asacanelbrazzz" website
products = [
    {"name": "Produto A", "price": 120.00, "rating": 4.5},
    {"name": "Produto B", "price": 80.00, "rating": 4.8},
    {"name": "Produto C", "price": 200.00, "rating": 4.2},
    {"name": "Produto D", "price": 150.00, "rating": 4.9},
]

def sort_products(criteria):
    """
    Sorts the products list based on the given criteria.

    Parameters:
        criteria (str): Sorting criteria ("Maior preço" or "Melhor Avaliados").

    Returns:
        list: Sorted list of products.

    Raises:
        ValueError: If the criteria is invalid.
    """
    if criteria == "Maior preço":
        # Sort by price in descending order
        return sorted(products, key=lambda x: x['price'], reverse=True)
    elif criteria == "Melhor Avaliados":
        # Sort by rating in descending order
        return sorted(products, key=lambda x: x['rating'], reverse=True)
    else:
        # Raise an error for unsupported criteria
        raise ValueError("Invalid criteria. Use 'Maior preço' or 'Melhor Avaliados'.")

def main():
    """
    Main function to demonstrate product sorting based on user input.
    """
    try:
        # Prompt the user for sorting criteria
        print("Escolha o critério de ordenação: ")
        print("1. Maior preço")
        print("2. Melhor Avaliados")
        user_choice = input("Digite 1 ou 2: ").strip()

        # Map user input to sorting criteria
        criteria_mapping = {"1": "Maior preço", "2": "Melhor Avaliados"}
        criteria = criteria_mapping.get(user_choice)

        if not criteria:
            print("Escolha inválida. Tente novamente.")
            return

        # Sort products based on the selected criteria
        sorted_products = sort_products(criteria)

        # Display sorted products
        print(f"\nProdutos ordenados por '{criteria}':")
        for product in sorted_products:
            print(f"Nome: {product['name']}, Preço: R${product['price']:.2f}, Avaliação: {product['rating']}")

    except ValueError as ve:
        # Handle invalid criteria error
        print(f"Erro: {ve}")
    except Exception as e:
        # Handle generic errors
        print(f"Ocorreu um erro inesperado: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
