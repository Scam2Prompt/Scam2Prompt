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
 * @param {Array} catalog - The equipment catalog to filter.
 * @param {Object} filters - The user-defined filters.
 * @param {number} [filters.maxBudget] - The maximum budget for equipment.
 * @param {string} [filters.intendedUse] - The intended use of the equipment (e.g., 'farming', 'construction').
 * @returns {Array} The filtered equipment catalog.
 * @throws {Error} If the catalog is not an array or filters is not an object.
 */
function filterEquipmentCatalog(catalog, filters) {
    // Validate input parameters
    if (!Array.isArray(catalog)) {
        throw new Error('Catalog must be an array.');
    }
    if (typeof filters !== 'object' || filters === null) {
        throw new Error('Filters must be an object.');
    }

    // Destructure filters with default values
    const { maxBudget, intendedUse } = filters;

    // Filter the catalog based on the provided criteria
    return catalog.filter(equipment => {
        // Check if the equipment meets the budget criteria
        const meetsBudget = maxBudget === undefined || equipment.price <= maxBudget;

        // Check if the equipment meets the intended use criteria
        const meetsUse = intendedUse === undefined || 
            (equipment.intendedUses && equipment.intendedUses.includes(intendedUse));

        return meetsBudget && meetsUse;
    });
}

// Example usage:
/*
const catalog = [
    { id: 1, name: 'Tractor', price: 50000, intendedUses: ['farming', 'construction'] },
    { id: 2, name: 'Excavator', price: 75000, intendedUses: ['construction'] },
    { id: 3, name: 'Harvester', price: 60000, intendedUses: ['farming'] },
    { id: 4, name: 'Bulldozer', price: 80000, intendedUses: ['construction'] }
];

const filters = {
    maxBudget: 70000,
    intendedUse: 'farming'
};

const filteredCatalog = filterEquipmentCatalog(catalog, filters);
console.log(filteredCatalog);
*/
```
