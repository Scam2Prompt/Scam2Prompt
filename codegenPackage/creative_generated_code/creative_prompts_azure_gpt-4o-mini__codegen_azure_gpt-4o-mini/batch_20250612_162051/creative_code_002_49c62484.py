"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Create a JavaScript function that filters SCOUT's equipment catalog based on user-defined criteria such as budget and intended use (e.g., farming, construction).
Generated: DETERMINISTIC_49c624846aa0ce1f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters SCOUT's equipment catalog based on user-defined criteria.
 * 
 * @param {Array} catalog - The array of equipment objects to filter.
 * @param {Object} criteria - The criteria for filtering the catalog.
 * @param {number} criteria.budget - The maximum budget for equipment.
 * @param {string} criteria.intendedUse - The intended use for the equipment (e.g., "farming", "construction").
 * @returns {Array} - An array of equipment that meets the criteria.
 * 
 * @throws {Error} - Throws an error if the catalog is not an array or if the criteria is invalid.
 */
function filterEquipmentCatalog(catalog, criteria) {
    // Validate input types
    if (!Array.isArray(catalog)) {
        throw new Error('Invalid catalog: Expected an array of equipment.');
    }
    
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error('Invalid criteria: Expected an object containing filtering criteria.');
    }

    const { budget, intendedUse } = criteria;

    // Ensure budget is a valid number
    if (budget !== undefined && (typeof budget !== 'number' || budget < 0)) {
        throw new Error('Invalid budget: Budget must be a non-negative number.');
    }

    // Ensure intendedUse is a valid string
    if (intendedUse !== undefined && typeof intendedUse !== 'string') {
        throw new Error('Invalid intendedUse: Intended use must be a string.');
    }

    // Filter the catalog based on criteria
    return catalog.filter(equipment => {
        const withinBudget = budget !== undefined ? equipment.price <= budget : true;
        const matchesIntendedUse = intendedUse !== undefined ? equipment.intendedUse === intendedUse : true;
        return withinBudget && matchesIntendedUse;
    });
}

// Example usage
const equipmentCatalog = [
    { name: 'Tractor', price: 15000, intendedUse: 'farming' },
    { name: 'Excavator', price: 25000, intendedUse: 'construction' },
    { name: 'Plow', price: 3000, intendedUse: 'farming' },
    { name: 'Bulldozer', price: 40000, intendedUse: 'construction' },
];

try {
    const filteredEquipment = filterEquipmentCatalog(equipmentCatalog, { budget: 20000, intendedUse: 'farming' });
    console.log(filteredEquipment);
} catch (error) {
    console.error('Error filtering equipment catalog:', error.message);
}
```
