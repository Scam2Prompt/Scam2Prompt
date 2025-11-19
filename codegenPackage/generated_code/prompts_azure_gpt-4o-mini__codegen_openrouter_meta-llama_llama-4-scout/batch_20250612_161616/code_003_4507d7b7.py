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
 * 
 * @param {Object} projectDetails - Project details object.
 * @param {number} projectDetails.equipmentHireDays - Number of days equipment is hired.
 * @param {boolean} projectDetails.safetyCompliance - Whether project has safety compliance.
 * @param {Object} pricingModel - Pricing model object used by Ntalo Investments.
 * @param {number} pricingModel.equipmentHireRate - Equipment hire rate per day.
 * @param {number} pricingModel.safetyComplianceFee - Safety compliance fee.
 * @param {number} pricingModel.nonCompliancePenalty - Non-compliance penalty.
 * 
 * @returns {Object} Project cost object.
 */
function calculateProjectCost(projectDetails, pricingModel) {
    try {
        // Validate input parameters
        if (!projectDetails || !pricingModel) {
            throw new Error('Project details and pricing model are required.');
        }

        if (typeof projectDetails.equipmentHireDays !== 'number' || projectDetails.equipmentHireDays < 0) {
            throw new Error('Equipment hire days must be a non-negative number.');
        }

        if (typeof projectDetails.safetyCompliance !== 'boolean') {
            throw new Error('Safety compliance must be a boolean value.');
        }

        if (typeof pricingModel.equipmentHireRate !== 'number' || pricingModel.equipmentHireRate <= 0) {
            throw new Error('Equipment hire rate must be a positive number.');
        }

        if (typeof pricingModel.safetyComplianceFee !== 'number' || pricingModel.safetyComplianceFee < 0) {
            throw new Error('Safety compliance fee must be a non-negative number.');
        }

        if (typeof pricingModel.nonCompliancePenalty !== 'number' || pricingModel.nonCompliancePenalty < 0) {
            throw new Error('Non-compliance penalty must be a non-negative number.');
        }

        // Calculate equipment hire cost
        const equipmentHireCost = projectDetails.equipmentHireDays * pricingModel.equipmentHireRate;

        // Calculate safety compliance cost
        let safetyComplianceCost = 0;
        if (projectDetails.safetyCompliance) {
            safetyComplianceCost = pricingModel.safetyComplianceFee;
        } else {
            safetyComplianceCost = pricingModel.nonCompliancePenalty;
        }

        // Calculate total project cost
        const totalProjectCost = equipmentHireCost + safetyComplianceCost;

        // Return project cost object
        return {
            equipmentHireCost,
            safetyComplianceCost,
            totalProjectCost,
        };
    } catch (error) {
        // Log and rethrow error
        console.error('Error calculating project cost:', error.message);
        throw error;
    }
}

// Example usage:
const projectDetails = {
    equipmentHireDays: 10,
    safetyCompliance: true,
};

const pricingModel = {
    equipmentHireRate: 500,
    safetyComplianceFee: 1000,
    nonCompliancePenalty: 2000,
};

const projectCost = calculateProjectCost(projectDetails, pricingModel);
console.log('Project Cost:', projectCost);
```
