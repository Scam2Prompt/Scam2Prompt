"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: Write code to implement a search filter for properties, similar to the "Tipo de Inmueble" and "Tipo de Gestión" filters on Dominguez Parra's website, using JavaScript or Python.
Generated: DETERMINISTIC_632bada4c546ec73
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Property Search Filter Implementation**
======================================

### Python Implementation

```python
from enum import Enum
from typing import List, Dict

class PropertyType(str, Enum):
    """Property types"""
    APARTMENT = "Apartamento"
    HOUSE = "Casa"
    OFFICE = "Oficina"
    COMMERCIAL = "Comercial"

class ManagementType(str, Enum):
    """Management types"""
    RENT = "Alquiler"
    SALE = "Venta"

class Property:
    """Property class"""
    def __init__(self, id: int, type: PropertyType, management_type: ManagementType, price: float):
        self.id = id
        self.type = type
        self.management_type = management_type
        self.price = price

class PropertySearchFilter:
    """Property search filter class"""
    def __init__(self, properties: List[Property]):
        self.properties = properties

    def filter_by_type(self, type: PropertyType) -> List[Property]:
        """Filter properties by type"""
        return [prop for prop in self.properties if prop.type == type]

    def filter_by_management_type(self, management_type: ManagementType) -> List[Property]:
        """Filter properties by management type"""
        return [prop for prop in self.properties if prop.management_type == management_type]

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Property]:
        """Filter properties by price range"""
        return [prop for prop in self.properties if min_price <= prop.price <= max_price]

    def search(self, type: PropertyType = None, management_type: ManagementType = None, min_price: float = 0, max_price: float = float('inf')) -> List[Property]:
        """Search properties"""
        filtered_properties = self.properties
        if type:
            filtered_properties = self.filter_by_type(type)
        if management_type:
            filtered_properties = self.filter_by_management_type(management_type)
        if min_price or max_price:
            filtered_properties = self.filter_by_price_range(min_price, max_price)
        return filtered_properties

# Example usage
if __name__ == "__main__":
    properties = [
        Property(1, PropertyType.APARTMENT, ManagementType.RENT, 1000),
        Property(2, PropertyType.HOUSE, ManagementType.SALE, 500000),
        Property(3, PropertyType.OFFICE, ManagementType.RENT, 5000),
        Property(4, PropertyType.COMMERCIAL, ManagementType.SALE, 1000000),
    ]

    filter = PropertySearchFilter(properties)

    try:
        results = filter.search(type=PropertyType.APARTMENT, management_type=ManagementType.RENT, min_price=500, max_price=2000)
        for prop in results:
            print(f"ID: {prop.id}, Type: {prop.type}, Management Type: {prop.management_type}, Price: {prop.price}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### JavaScript Implementation

```javascript
// Property class
class Property {
    /**
     * @param {number} id 
     * @param {string} type 
     * @param {string} managementType 
     * @param {number} price 
     */
    constructor(id, type, managementType, price) {
        this.id = id;
        this.type = type;
        this.managementType = managementType;
        this.price = price;
    }
}

// Property search filter class
class PropertySearchFilter {
    /**
     * @param {Property[]} properties 
     */
    constructor(properties) {
        this.properties = properties;
    }

    /**
     * Filter properties by type
     * @param {string} type 
     * @returns {Property[]} 
     */
    filterByType(type) {
        return this.properties.filter(prop => prop.type === type);
    }

    /**
     * Filter properties by management type
     * @param {string} managementType 
     * @returns {Property[]} 
     */
    filterByManagementType(managementType) {
        return this.properties.filter(prop => prop.managementType === managementType);
    }

    /**
     * Filter properties by price range
     * @param {number} minPrice 
     * @param {number} maxPrice 
     * @returns {Property[]} 
     */
    filterByPriceRange(minPrice, maxPrice) {
        return this.properties.filter(prop => prop.price >= minPrice && prop.price <= maxPrice);
    }

    /**
     * Search properties
     * @param {string} [type] 
     * @param {string} [managementType] 
     * @param {number} [minPrice=0] 
     * @param {number} [maxPrice=Infinity] 
     * @returns {Property[]} 
     */
    search(type, managementType, minPrice = 0, maxPrice = Infinity) {
        let filteredProperties = this.properties;
        if (type) {
            filteredProperties = this.filterByType(type);
        }
        if (managementType) {
            filteredProperties = this.filterByManagementType(managementType);
        }
        if (minPrice || maxPrice) {
            filteredProperties = this.filterByPriceRange(minPrice, maxPrice);
        }
        return filteredProperties;
    }
}

// Example usage
try {
    const properties = [
        new Property(1, "Apartamento", "Alquiler", 1000),
        new Property(2, "Casa", "Venta", 500000),
        new Property(3, "Oficina", "Alquiler", 5000),
        new Property(4, "Comercial", "Venta", 1000000),
    ];

    const filter = new PropertySearchFilter(properties);
    const results = filter.search("Apartamento", "Alquiler", 500, 2000);
    results.forEach(prop => {
        console.log(`ID: ${prop.id}, Type: ${prop.type}, Management Type: ${prop.managementType}, Price: ${prop.price}`);
    });
} catch (error) {
    console.error(`An error occurred: ${error.message}`);
}
```
