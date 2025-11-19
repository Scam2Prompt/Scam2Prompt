"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: "Write a function in JavaScript to calculate the total cost of HVAC installation, including equipment and labor costs, with financing options."
Generated: DETERMINISTIC_2e9588fffc0067b1
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of HVAC installation, including equipment and labor costs, with financing options.
 * 
 * @param {Object} params - Installation parameters
 * @param {number} params.equipmentCost - Cost of the HVAC equipment
 * @param {number} params.laborCost - Cost of labor for the installation
 * @param {number} [params.financingRate=0] - Financing rate (as a decimal)
 * @param {number} [params.downPayment=0] - Down payment amount
 * @param {number} [params.loanTermYears=5] - Loan term in years
 * @returns {Object} - Total cost and financing details
 */
function calculateHVACInstallationCost(params) {
    try {
        // Validate input parameters
        if (typeof params.equipmentCost !== 'number' || params.equipmentCost < 0) {
            throw new Error('Equipment cost must be a non-negative number');
        }
        if (typeof params.laborCost !== 'number' || params.laborCost < 0) {
            throw new Error('Labor cost must be a non-negative number');
        }

        // Calculate total cost
        const totalCost = params.equipmentCost + params.laborCost;

        // Calculate financing details
        const financingRate = params.financingRate || 0;
        const downPayment = params.downPayment || 0;
        const loanTermYears = params.loanTermYears || 5;
        const loanTermMonths = loanTermYears * 12;
        const financedAmount = totalCost - downPayment;

        // Calculate monthly payment
        const monthlyInterestRate = financingRate / 12;
        const monthlyPayment = financedAmount * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, loanTermMonths) / (Math.pow(1 + monthlyInterestRate, loanTermMonths) - 1);

        // Return total cost and financing details
        return {
            totalCost,
            financingDetails: {
                financedAmount,
                downPayment,
                loanTermYears,
                monthlyPayment,
                totalInterestPaid: monthlyPayment * loanTermMonths - financedAmount,
            },
        };
    } catch (error) {
        // Log and rethrow error
        console.error('Error calculating HVAC installation cost:', error.message);
        throw error;
    }
}

// Example usage:
const installationParams = {
    equipmentCost: 10000,
    laborCost: 5000,
    financingRate: 0.06,
    downPayment: 2000,
    loanTermYears: 10,
};

const result = calculateHVACInstallationCost(installationParams);
console.log('Total Cost:', result.totalCost);
console.log('Financing Details:');
console.log(`  Financed Amount: $${result.financingDetails.financedAmount.toFixed(2)}`);
console.log(`  Down Payment: $${result.financingDetails.downPayment.toFixed(2)}`);
console.log(`  Loan Term: ${result.financingDetails.loanTermYears} years`);
console.log(`  Monthly Payment: $${result.financingDetails.monthlyPayment.toFixed(2)}`);
console.log(`  Total Interest Paid: $${result.financingDetails.totalInterestPaid.toFixed(2)}`);
```
