"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Develop a JavaScript function that calculates project costs based on equipment hire and safety compliance, reflecting the pricing model used by Ntalo Investments.
Generated: DETERMINISTIC_4507d7b7ac0c8ab3
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates project costs based on equipment hire and safety compliance.
 * Pricing model follows Ntalo Investments' standards.
 * 
 * @param {Object} params - Project parameters
 * @param {number} params.equipmentHours - Total hours of equipment hire
 * @param {string} params.equipmentType - Type of equipment (e.g., 'excavator', 'crane', 'bulldozer')
 * @param {boolean} params.safetyCompliance - Whether safety compliance is required
 * @param {number} [params.discountRate=0] - Optional discount rate (0-1)
 * @returns {Object} - Result containing cost breakdown and total
 * @throws {Error} - If invalid parameters are provided
 */
function calculateProjectCost(params) {
    // Validate input parameters
    if (!params || typeof params !== 'object') {
        throw new Error('Invalid parameters: must provide an object');
    }

    const { equipmentHours, equipmentType, safetyCompliance, discountRate = 0 } = params;

    if (typeof equipmentHours !== 'number' || equipmentHours <= 0) {
        throw new Error('Invalid equipmentHours: must be a positive number');
    }

    if (typeof equipmentType !== 'string' || !equipmentType.trim()) {
        throw new Error('Invalid equipmentType: must be a non-empty string');
    }

    if (typeof safetyCompliance !== 'boolean') {
        throw new Error('Invalid safetyCompliance: must be a boolean');
    }

    if (typeof discountRate !== 'number' || discountRate < 0 || discountRate > 1) {
        throw new Error('Invalid discountRate: must be between 0 and 1');
    }

    // Equipment hourly rates (Ntalo Investments pricing model)
    const equipmentRates = {
        excavator: 150,
        crane: 200,
        bulldozer: 175,
        forklift: 100,
        generator: 75
    };

    // Get equipment rate or default to base rate if not found
    const baseRate = 120;
    const equipmentRate = equipmentRates[equipmentType.toLowerCase()] || baseRate;

    // Calculate base equipment cost
    const baseEquipmentCost = equipmentHours * equipmentRate;

    // Safety compliance fee (10% of equipment cost)
    const safetyFee = safetyCompliance ? baseEquipmentCost * 0.1 : 0;

    // Subtotal before discount
    const subtotal = baseEquipmentCost + safetyFee;

    // Apply discount if any
    const discountAmount = subtotal * discountRate;
    const total = subtotal - discountAmount;

    return {
        equipmentType: equipmentType,
        equipmentHours: equipmentHours,
        equipmentRate: equipmentRate,
        baseEquipmentCost: parseFloat(baseEquipmentCost.toFixed(2)),
        safetyCompliance: safetyCompliance,
        safetyFee: parseFloat(safetyFee.toFixed(2)),
        subtotal: parseFloat(subtotal.toFixed(2)),
        discountRate: discountRate,
        discountAmount: parseFloat(discountAmount.toFixed(2)),
        total: parseFloat(total.toFixed(2))
    };
}
```
