"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python script to generate a catalog of tools and machinery, including categories like "roldana," "polé," "moitão," and "turbina," as described on the Geyciane Ferramentas webpage.
Generated: DETERMINISTIC_ba455586e4888dfd
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto

class Category(Enum):
    ROLDANA = "roldana"
    POLE = "polé"
    MOITAO = "moitão"
    TURBINA = "turbina"

@dataclass
class Tool:
    name: str
    category: Category
    description: str
    price: float
    stock: int
    sku: str
    weight_kg: Optional[float] = None
    dimensions: Optional[str] = None

class CatalogGenerator:
    def __init__(self):
        self.catalog: List[Tool] = []

    def add_tool(self, tool: Tool) -> None:
        """Add a tool to the catalog."""
        self.catalog.append(tool)

    def generate_catalog(self, filename: str = "tools_catalog.json") -> None:
        """Generate a JSON catalog file from the tools list."""
        try:
            catalog_data = [asdict(tool) for tool in self.catalog]
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(catalog_data, f, indent=4, ensure_ascii=False)
            print(f"Catalog successfully generated as {filename}")
        except IOError as e:
            print(f"Error writing catalog file: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

def sample_catalog() -> CatalogGenerator:
    """Generate a sample catalog with example tools."""
    catalog = CatalogGenerator()
    
    catalog.add_tool(Tool(
        name="Roldana de Aço 50mm",
        category=Category.ROLDANA,
        description="Roldana de aço galvanizado com 50mm de diâmetro",
        price=24.90,
        stock=150,
        sku="RLD50",
        weight_kg=0.5,
        dimensions="50x50x20mm"
    ))
    
    catalog.add_tool(Tool(
        name="Polé Dupla 100mm",
        category=Category.POLE,
        description="Polé dupla em aço carbono com rolamento",
        price=89.90,
        stock=75,
        sku="PLD100",
        weight_kg=1.2,
        dimensions="100x80x40mm"
    ))
    
    catalog.add_tool(Tool(
        name="Moitão 1 Tonelada",
        category=Category.MOITAO,
        description="Moitão de corrente para 1 tonelada",
        price=349.90,
        stock=30,
        sku="MT1T",
        weight_kg=3.5,
        dimensions="150x120x60mm"
    ))
    
    catalog.add_tool(Tool(
        name="Turbina Industrial 5HP",
        category=Category.TURBINA,
        description="Turbina industrial 5HP com eixo em aço",
        price=1250.00,
        stock=12,
        sku="TB5HP",
        weight_kg=8.7,
        dimensions="300x250x200mm"
    ))
    
    return catalog

if __name__ == "__main__":
    catalog = sample_catalog()
    catalog.generate_catalog()
```
