"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Generate a code snippet in JavaScript to calculate the cost of accounting services based on the client's needs and services provided, as described on the Atual Contabilidade website."
Generated: DETERMINISTIC_11f5b2094cdf7abf
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of accounting services based on client needs and services provided.
 * @param {Object} clientData - Client information and service requirements
 * @param {string} clientData.businessType - Type of business (MEI, Simples Nacional, Lucro Presumido, etc.)
 * @param {string[]} clientData.services - Array of required services (e.g., ['bookkeeping', 'tax filing', 'payroll'])
 * @param {number} clientData.employees - Number of employees
 * @param {number} clientData.monthlyRevenue - Average monthly revenue in BRL
 * @returns {Object} - Calculation result with base price, additional fees, and total
 */
function calculateAccountingCost(clientData) {
    // Validate input
    if (!clientData || typeof clientData !== 'object') {
        throw new Error('Invalid client data: must be an object');
    }

    const requiredFields = ['businessType', 'services', 'employees', 'monthlyRevenue'];
    for (const field of requiredFields) {
        if (!clientData[field]) {
            throw new Error(`Missing required field: ${field}`);
        }
    }

    // Base pricing structure
    const basePrices = {
        'MEI': 150,
        'Simples Nacional': 300,
        'Lucro Presumido': 500,
        'Lucro Real': 800
    };

    // Service add-ons
    const servicePrices = {
        'bookkeeping': 100,
        'tax filing': 200,
        'payroll': 50,
        'financial advisory': 300,
        'tax planning': 250
    };

    // Employee tier pricing
    const employeeTiers = [
        { max: 5, multiplier: 1 },
        { max: 20, multiplier: 1.2 },
        { max: 100, multiplier: 1.5 },
        { max: Infinity, multiplier: 2 }
    ];

    // Revenue-based adjustments
    const revenueTiers = [
        { max: 10000, multiplier: 1 },
        { max: 50000, multiplier: 1.1 },
        { max: 100000, multiplier: 1.2 },
        { max: Infinity, multiplier: 1.3 }
    ];

    // Calculate base price
    if (!basePrices[clientData.businessType]) {
        throw new Error(`Unsupported business type: ${clientData.businessType}`);
    }
    let total = basePrices[clientData.businessType];

    // Add service costs
    clientData.services.forEach(service => {
        if (!servicePrices[service]) {
            throw new Error(`Unsupported service: ${service}`);
        }
        total += servicePrices[service];
    });

    // Apply employee multiplier
    const employeeTier = employeeTiers.find(tier => clientData.employees <= tier.max);
    total *= employeeTier.multiplier;

    // Apply revenue multiplier
    const revenueTier = revenueTiers.find(tier => clientData.monthlyRevenue <= tier.max);
    total *= revenueTier.multiplier;

    // Round to 2 decimal places
    total = Math.round(total * 100) / 100;

    return {
        basePrice: basePrices[clientData.businessType],
        serviceAddons: clientData.services.map(service => ({
            service,
            cost: servicePrices[service]
        })),
        employeeMultiplier: employeeTier.multiplier,
        revenueMultiplier: revenueTier.multiplier,
        totalCost: total
    };
}

// Example usage:
/*
const clientExample = {
    businessType: 'Simples Nacional',
    services: ['bookkeeping', 'tax filing'],
    employees: 8,
    monthlyRevenue: 25000
};

try {
    const quote = calculateAccountingCost(clientExample);
    console.log(quote);
} catch (error) {
    console.error('Error calculating cost:', error.message);
}
*/
```
