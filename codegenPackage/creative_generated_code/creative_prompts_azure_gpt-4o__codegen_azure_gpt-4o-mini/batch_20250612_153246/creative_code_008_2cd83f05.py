"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duct-split.com
Prompt: Write JavaScript code to implement a search functionality for the "duct-split.com" website, allowing users to filter Gree air conditioners by cooling capacity, inverter type, and price range.
Generated: DETERMINISTIC_2cd83f058d359002
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// airConditionerSearch.js

// Sample data representing Gree air conditioners
const airConditioners = [
    { id: 1, model: 'Gree Model A', coolingCapacity: 18000, inverterType: 'Inverter', price: 500 },
    { id: 2, model: 'Gree Model B', coolingCapacity: 24000, inverterType: 'Non-Inverter', price: 600 },
    { id: 3, model: 'Gree Model C', coolingCapacity: 12000, inverterType: 'Inverter', price: 400 },
    { id: 4, model: 'Gree Model D', coolingCapacity: 30000, inverterType: 'Inverter', price: 800 },
    { id: 5, model: 'Gree Model E', coolingCapacity: 15000, inverterType: 'Non-Inverter', price: 550 },
];

// Function to filter air conditioners based on user criteria
function searchAirConditioners(criteria) {
    try {
        // Destructure criteria for easier access
        const { minCoolingCapacity, maxCoolingCapacity, inverterType, minPrice, maxPrice } = criteria;

        // Validate the criteria object
        if (typeof criteria !== 'object') {
            throw new Error('Criteria must be an object');
        }

        // Filter the air conditioners based on criteria
        return airConditioners.filter(ac => {
            const coolingCapacityValid = ac.coolingCapacity >= (minCoolingCapacity || 0) && ac.coolingCapacity <= (maxCoolingCapacity || Infinity);
            const inverterTypeValid = !inverterType || ac.inverterType === inverterType;
            const priceValid = ac.price >= (minPrice || 0) && ac.price <= (maxPrice || Infinity);
            return coolingCapacityValid && inverterTypeValid && priceValid;
        });
    } catch (error) {
        console.error('Error searching air conditioners:', error.message);
        return [];
    }
}

// Example usage
const searchCriteria = {
    minCoolingCapacity: 12000,
    maxCoolingCapacity: 24000,
    inverterType: 'Inverter',
    minPrice: 400,
    maxPrice: 700,
};

const results = searchAirConditioners(searchCriteria);
console.log('Search Results:', results);
```

This JavaScript code implements a search functionality for filtering Gree air conditioners based on specified criteria. It includes error handling and is structured for clarity and maintainability.
