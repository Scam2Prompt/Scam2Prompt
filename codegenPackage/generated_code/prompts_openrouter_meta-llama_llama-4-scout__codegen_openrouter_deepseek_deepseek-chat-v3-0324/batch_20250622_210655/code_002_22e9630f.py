"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Create a JavaScript function to calculate the cost of a surgical procedure based on individual patient needs and procedure details.
Generated: DETERMINISTIC_22e9630fb5886033
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of a surgical procedure based on patient needs and procedure details.
 * @param {Object} procedureDetails - Details about the surgical procedure
 * @param {string} procedureDetails.procedureType - Type of procedure (e.g., 'cardiac', 'orthopedic')
 * @param {number} procedureDetails.durationHours - Duration of procedure in hours
 * @param {boolean} procedureDetails.isEmergency - Whether the procedure is an emergency
 * @param {Object} patientDetails - Details about the patient
 * @param {number} patientDetails.age - Patient's age
 * @param {boolean} patientDetails.hasInsurance - Whether patient has insurance
 * @param {string} patientDetails.insurancePlan - Type of insurance plan (if any)
 * @returns {number} Calculated total cost of the procedure
 * @throws {Error} If required parameters are missing or invalid
 */
function calculateSurgicalCost(procedureDetails, patientDetails) {
    // Validate input parameters
    if (!procedureDetails || !patientDetails) {
        throw new Error('Both procedureDetails and patientDetails are required');
    }

    const requiredProcedureFields = ['procedureType', 'durationHours', 'isEmergency'];
    const requiredPatientFields = ['age', 'hasInsurance'];

    for (const field of requiredProcedureFields) {
        if (procedureDetails[field] === undefined) {
            throw new Error(`Missing required procedure field: ${field}`);
        }
    }

    for (const field of requiredPatientFields) {
        if (patientDetails[field] === undefined) {
            throw new Error(`Missing required patient field: ${field}`);
        }
    }

    // Base costs for different procedure types
    const baseCosts = {
        cardiac: 5000,
        orthopedic: 4000,
        neurological: 6000,
        general: 3000,
        cosmetic: 4500
    };

    // Validate procedure type
    if (!baseCosts[procedureDetails.procedureType]) {
        throw new Error(`Invalid procedure type: ${procedureDetails.procedureType}`);
    }

    // Calculate base cost
    let totalCost = baseCosts[procedureDetails.procedureType];

    // Apply duration multiplier (per hour)
    totalCost += totalCost * 0.1 * procedureDetails.durationHours;

    // Emergency surcharge
    if (procedureDetails.isEmergency) {
        totalCost *= 1.25;
    }

    // Age-based adjustments
    if (patientDetails.age < 18) {
        totalCost *= 0.9; // 10% discount for minors
    } else if (patientDetails.age > 65) {
        totalCost *= 0.85; // 15% discount for seniors
    }

    // Insurance adjustments
    if (patientDetails.hasInsurance) {
        const insurancePlans = {
            'basic': 0.8,
            'premium': 0.7,
            'government': 0.5
        };

        const discountFactor = insurancePlans[patientDetails.insurancePlan] || 0.9;
        totalCost *= discountFactor;
    }

    // Ensure cost is not negative (shouldn't happen but good practice)
    totalCost = Math.max(0, totalCost);

    // Round to 2 decimal places for currency
    return Math.round(totalCost * 100) / 100;
}
```
