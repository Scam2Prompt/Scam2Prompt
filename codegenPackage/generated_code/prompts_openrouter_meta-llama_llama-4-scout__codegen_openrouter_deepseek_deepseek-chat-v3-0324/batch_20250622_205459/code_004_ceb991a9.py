"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Write a JavaScript function to calculate the cost of transporting goods based on the type of freight and incoterms used by Kalgate Technology.
Generated: DETERMINISTIC_ceb991a92c472f6e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of transporting goods based on freight type and incoterms.
 * @param {string} freightType - Type of freight ('air', 'sea', 'road', 'rail')
 * @param {string} incoterm - Incoterm used ('EXW', 'FOB', 'CIF', 'DDP', etc.)
 * @param {number} baseCost - Base cost of the goods
 * @param {number} weight - Weight of the goods in kg
 * @param {number} distance - Distance in km (optional for some freight types)
 * @returns {number} Total transportation cost
 * @throws {Error} If invalid parameters are provided
 */
function calculateTransportCost(freightType, incoterm, baseCost, weight, distance = 0) {
    // Validate input parameters
    if (!['air', 'sea', 'road', 'rail'].includes(freightType)) {
        throw new Error('Invalid freight type. Must be one of: air, sea, road, rail');
    }

    if (!['EXW', 'FOB', 'CIF', 'CFR', 'DAP', 'DPU', 'DDP'].includes(incoterm)) {
        throw new Error('Invalid incoterm. Must be one of: EXW, FOB, CIF, CFR, DAP, DPU, DDP');
    }

    if (typeof baseCost !== 'number' || baseCost <= 0) {
        throw new Error('Base cost must be a positive number');
    }

    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Weight must be a positive number');
    }

    if (typeof distance !== 'number' || distance < 0) {
        throw new Error('Distance must be a non-negative number');
    }

    // Define freight rates per kg (example values)
    const freightRates = {
        air: 5.0,
        sea: 1.2,
        road: 0.8,
        rail: 0.5
    };

    // Define incoterm multipliers (example values)
    const incotermMultipliers = {
        EXW: 1.0,
        FOB: 1.1,
        CIF: 1.2,
        CFR: 1.15,
        DAP: 1.25,
        DPU: 1.3,
        DDP: 1.4
    };

    // Calculate base freight cost
    let freightCost = freightRates[freightType] * weight;
    
    // Apply distance factor for road and rail
    if (freightType === 'road' || freightType === 'rail') {
        freightCost *= (1 + (distance * 0.001)); // 0.1% per km
    }

    // Apply incoterm multiplier to base cost
    const totalCost = baseCost * incotermMultipliers[incoterm] + freightCost;

    return parseFloat(totalCost.toFixed(2));
}

// Example usage:
// try {
//     const cost = calculateTransportCost('road', 'DDP', 1000, 50, 300);
//     console.log(`Total transportation cost: $${cost}`);
// } catch (error) {
//     console.error('Error calculating transport cost:', error.message);
// }
```
