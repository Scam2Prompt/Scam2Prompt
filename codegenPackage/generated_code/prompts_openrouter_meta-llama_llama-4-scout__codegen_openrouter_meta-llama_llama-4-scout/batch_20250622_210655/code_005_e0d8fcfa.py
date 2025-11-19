"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Develop a system for tracking and managing inventory of fabrics, threads, and other sewing materials for a workshop, including features for supplier management and material requisition."
Generated: DETERMINISTIC_e0d8fcfad08e442f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class MaterialType(str, Enum):
    FABRIC = "fabric"
    THREAD = "thread"
    OTHER = "other"

@dataclass
class Material:
    id: int
    name: str
    type: MaterialType
    quantity: int
    unit_price: float

@dataclass
class Supplier:
    id: int
    name: str
    contact_info: str

class Inventory:
    def __init__(self):
        self.materials: Dict[int, Material] = {}
        self.suppliers: Dict[int, Supplier] = {}
        self.material_id_counter = 1
        self.supplier_id_counter = 1

    def add_material(self, name: str, type: MaterialType, quantity: int, unit_price: float):
        material = Material(self.material_id_counter, name, type, quantity, unit_price)
        self.materials[self.material_id_counter] = material
        self.material_id_counter += 1
        return material

    def update_material(self, material_id: int, quantity: int = None, unit_price: float = None):
        if material_id not in self.materials:
            raise ValueError("Material not found")
        material = self.materials[material_id]
        if quantity is not None:
            material.quantity = quantity
        if unit_price is not None:
            material.unit_price = unit_price
        return material

    def delete_material(self, material_id: int):
        if material_id not in self.materials:
            raise ValueError("Material not found")
        del self.materials[material_id]

    def add_supplier(self, name: str, contact_info: str):
        supplier = Supplier(self.supplier_id_counter, name, contact_info)
        self.suppliers[self.supplier_id_counter] = supplier
        self.supplier_id_counter += 1
        return supplier

    def update_supplier(self, supplier_id: int, name: str = None, contact_info: str = None):
        if supplier_id not in self.suppliers:
            raise ValueError("Supplier not found")
        supplier = self.suppliers[supplier_id]
        if name is not None:
            supplier.name = name
        if contact_info is not None:
            supplier.contact_info = contact_info
        return supplier

    def delete_supplier(self, supplier_id: int):
        if supplier_id not in self.suppliers:
            raise ValueError("Supplier not found")
        del self.suppliers[supplier_id]

    def requisition_material(self, material_id: int, quantity: int):
        if material_id not in self.materials:
            raise ValueError("Material not found")
        material = self.materials[material_id]
        if material.quantity < quantity:
            raise ValueError("Insufficient quantity")
        material.quantity -= quantity
        return material

class MaterialRequisition:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.requisitions: List[Dict] = []

    def create_requisition(self, material_id: int, quantity: int):
        try:
            material = self.inventory.requisition_material(material_id, quantity)
            requisition = {
                "id": len(self.requisitions) + 1,
                "material_id": material_id,
                "quantity": quantity,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.requisitions.append(requisition)
            return requisition
        except ValueError as e:
            print(f"Error: {e}")

def main():
    inventory = Inventory()

    # Add materials
    fabric = inventory.add_material("Cotton Fabric", MaterialType.FABRIC, 100, 10.99)
    thread = inventory.add_material("Thread", MaterialType.THREAD, 500, 1.99)

    # Add suppliers
    supplier1 = inventory.add_supplier("Supplier 1", "123 Main St")

    # Create requisition
    requisition_system = MaterialRequisition(inventory)
    requisition = requisition_system.create_requisition(fabric.id, 20)

    # Print results
    print("Materials:")
    for material in inventory.materials.values():
        print(f"{material.id}: {material.name} - Quantity: {material.quantity}")

    print("\nSuppliers:")
    for supplier in inventory.suppliers.values():
        print(f"{supplier.id}: {supplier.name}")

    print("\nRequisitions:")
    for requisition in requisition_system.requisitions:
        print(requisition)

if __name__ == "__main__":
    main()
```
