"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: "Develop a JavaScript function to calculate the costs of becoming a taxi driver in Poland, including licensing fees, vehicle maintenance, and fuel expenses."
Generated: DETERMINISTIC_88f0e30e43580481
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
 * Calculates the total cost of becoming a taxi driver in Poland.
 * @param {Object} params - Parameters for cost calculation
 * @param {number} params.licenseFee - Cost of obtaining a taxi license (PLN)
 * @param {number} params.vehicleCost - Initial vehicle purchase cost (PLN)
 * @param {number} params.insuranceAnnual - Annual insurance cost (PLN)
 * @param {number} params.maintenanceMonthly - Monthly vehicle maintenance cost (PLN)
 * @param {number} params.fuelCostPerKm - Fuel cost per kilometer (PLN)
 * @param {number} params.dailyKm - Average daily kilometers driven
 * @param {number} params.workingDaysPerMonth - Number of working days per month
 * @param {number} params.durationMonths - Duration of operation in months
 * @returns {Object} - Object containing cost breakdown and total
 */
function calculateTaxiDriverCosts(params) {
    // Validate input parameters
    if (!params || typeof params !== 'object') {
        throw new Error('Invalid parameters: must provide an object with cost details');
    }

    const requiredParams = [
        'licenseFee', 'vehicleCost', 'insuranceAnnual',
        'maintenanceMonthly', 'fuelCostPerKm', 'dailyKm',
        'workingDaysPerMonth', 'durationMonths'
    ];

    for (const param of requiredParams) {
        if (typeof params[param] !== 'number' || params[param] < 0) {
            throw new Error(`Invalid parameter: ${param} must be a positive number`);
        }
    }

    // Calculate monthly fuel cost
    const monthlyFuelCost = params.fuelCostPerKm * params.dailyKm * params.workingDaysPerMonth;

    // Calculate total costs
    const totalLicenseFee = params.licenseFee;
    const totalVehicleCost = params.vehicleCost;
    const totalInsurance = (params.insuranceAnnual / 12) * params.durationMonths;
    const totalMaintenance = params.maintenanceMonthly * params.durationMonths;
    const totalFuel = monthlyFuelCost * params.durationMonths;

    const totalCost = totalLicenseFee + totalVehicleCost + totalInsurance + 
                     totalMaintenance + totalFuel;

    return {
        licenseFee: totalLicenseFee,
        vehicleCost: totalVehicleCost,
        insurance: parseFloat(totalInsurance.toFixed(2)),
        maintenance: parseFloat(totalMaintenance.toFixed(2)),
        fuel: parseFloat(totalFuel.toFixed(2)),
        total: parseFloat(totalCost.toFixed(2)),
        monthlyAverage: parseFloat((totalCost / params.durationMonths).toFixed(2))
    };
}

// Example usage:
/*
const costs = calculateTaxiDriverCosts({
    licenseFee: 5000,
    vehicleCost: 80000,
    insuranceAnnual: 6000,
    maintenanceMonthly: 1000,
    fuelCostPerKm: 0.5,
    dailyKm: 200,
    workingDaysPerMonth: 20,
    durationMonths: 12
});
console.log(costs);
*/
```
