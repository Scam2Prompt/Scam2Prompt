"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Create a JSON data structure to represent a catalog of machinery and tools, including properties for 'nome', 'descricao', and 'categoria', with sample data in Portuguese.
Generated: DETERMINISTIC_fb102504b7ea91f3
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent a tool or machinery item
class Tool:
    def __init__(self, nome, descricao, categoria):
        """
        Initialize a new Tool instance.

        :param nome: str - The name of the tool or machinery
        :param descricao: str - A description of the tool or machinery
        :param categoria: str - The category of the tool or machinery
        """
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria

    def to_dict(self):
        """
        Convert the Tool instance to a dictionary.

        :return: dict - A dictionary representation of the Tool instance
        """
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "categoria": self.categoria
        }

# Create a catalog of tools and machinery
catalog = [
    Tool("Furadeira", "Furadeira elétrica de alta potência", "Ferramentas Elétricas"),
    Tool("Serra Circular", "Serra circular para cortes precisos", "Ferramentas Elétricas"),
    Tool("Martelo", "Martelo de aço para construção", "Ferramentas Manuais"),
    Tool("Chave de Fenda", "Chave de fenda com cabo ergonômico", "Ferramentas Manuais"),
    Tool("Lixadeira", "Lixadeira orbital para acabamentos", "Ferramentas Elétricas")
]

# Convert the catalog to a list of dictionaries
catalog_dict = [tool.to_dict() for tool in catalog]

# Convert the catalog to JSON format
catalog_json = json.dumps(catalog_dict, ensure_ascii=False, indent=4)

# Function to save the catalog to a JSON file
def save_catalog_to_file(filename):
    """
    Save the catalog JSON data to a file.

    :param filename: str - The name of the file to save the JSON data
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(catalog_json)
        print(f"Catalog saved successfully to {filename}")
    except IOError as e:
        print(f"Error saving catalog to file: {e}")

# Save the catalog to a JSON file
save_catalog_to_file("catalogo_ferramentas.json")
```
