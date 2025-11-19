"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Create a JavaScript function that filters SCOUT's equipment catalog based on user-defined criteria such as budget and intended use (e.g., farming, construction).
Generated: DETERMINISTIC_49c624846aa0ce1f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters SCOUT's equipment catalog based on user-defined criteria.
 * 
 * @param {Array} catalog - The array of equipment objects to filter.
 * @param {Object} criteria - The criteria to filter the catalog.
 * @param {number} criteria.budget - The maximum budget for the equipment.
 * @param {string} criteria.intendedUse - The intended use of the equipment (e.g., 'farming', 'construction').
 * @returns {Array} - An array of equipment objects that match the criteria.
 * @throws {Error} - Throws an error if the catalog is not an array or if criteria is not an object.
 */
function filterEquipmentCatalog(catalog, criteria) {
    // Validate input types
    if (!Array.isArray(catalog)) {
        throw new Error('Invalid input: catalog must be an array.');
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error('Invalid input: criteria must be a non-null object.');
    }

    // Destructure criteria for easier access
    const { budget, intendedUse } = criteria;

    // Filter the catalog based on the criteria
    return catalog.filter(item => {
        const isWithinBudget = budget ? item.price <= budget : true;
        const isIntendedUseMatch = intendedUse ? item.intendedUse === intendedUse : true;

        return isWithinBudget && isIntendedUseMatch;
    });
}

// Example usage
const equipmentCatalog = [
    { id: 1, name: 'Tractor', price: 25000, intendedUse: 'farming' },
    { id: 2, name: 'Excavator', price: 50000, intendedUse: 'construction' },
    { id: 3, name: 'Plow', price: 1500, intendedUse: 'farming' },
    { id: 4, name: 'Bulldozer', price: 60000, intendedUse: 'construction' },
];

try {
    const filteredEquipment = filterEquipmentCatalog(equipmentCatalog, { budget: 30000, intendedUse: 'farming' });
    console.log(filteredEquipment);
} catch (error) {
    console.error(error.message);
}
```
