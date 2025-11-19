"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Develop a simple financial calculator in JavaScript to determine the potential cost savings of using a fuel card program for a small trucking company.
Generated: DETERMINISTIC_f3a4c9f09ae7d59a
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
 * Financial Calculator for Fuel Card Savings
 * This script calculates the potential cost savings of using a fuel card program
 * for a small trucking company.
 * 
 * Assumptions:
 * - Fuel card provides a discount per gallon.
 * - The company has a fleet of trucks with average fuel consumption.
 * - The calculation is based on monthly fuel usage.
 */

// Function to calculate cost savings
function calculateFuelCardSavings({
    numberOfTrucks,
    averageMilesPerTruckPerMonth,
    averageMilesPerGallon,
    fuelPricePerGallon,
    fuelCardDiscountPerGallon
}) {
    try {
        // Input validation
        if (
            numberOfTrucks <= 0 ||
            averageMilesPerTruckPerMonth <= 0 ||
            averageMilesPerGallon <= 0 ||
            fuelPricePerGallon <= 0 ||
            fuelCardDiscountPerGallon < 0
        ) {
            throw new Error("Invalid input values. All inputs must be positive numbers.");
        }

        // Calculate total monthly fuel consumption in gallons
        const totalFuelConsumption = (numberOfTrucks * averageMilesPerTruckPerMonth) / averageMilesPerGallon;

        // Calculate total fuel cost without fuel card
        const totalFuelCostWithoutCard = totalFuelConsumption * fuelPricePerGallon;

        // Calculate total fuel cost with fuel card
        const totalFuelCostWithCard = totalFuelConsumption * (fuelPricePerGallon - fuelCardDiscountPerGallon);

        // Calculate savings
        const savings = totalFuelCostWithoutCard - totalFuelCostWithCard;

        // Return the results
        return {
            totalFuelConsumption: totalFuelConsumption.toFixed(2),
            totalFuelCostWithoutCard: totalFuelCostWithoutCard.toFixed(2),
            totalFuelCostWithCard: totalFuelCostWithCard.toFixed(2),
            savings: savings.toFixed(2)
        };
    } catch (error) {
        console.error("Error calculating fuel card savings:", error.message);
        return null;
    }
}

// Example usage
const inputData = {
    numberOfTrucks: 10, // Number of trucks in the fleet
    averageMilesPerTruckPerMonth: 3000, // Average miles driven per truck per month
    averageMilesPerGallon: 6, // Average miles per gallon for the trucks
    fuelPricePerGallon: 4.00, // Current fuel price per gallon
    fuelCardDiscountPerGallon: 0.20 // Discount per gallon using the fuel card
};

const result = calculateFuelCardSavings(inputData);

if (result) {
    console.log("Fuel Card Savings Calculation:");
    console.log(`Total Fuel Consumption (gallons): ${result.totalFuelConsumption}`);
    console.log(`Total Fuel Cost Without Card ($): ${result.totalFuelCostWithoutCard}`);
    console.log(`Total Fuel Cost With Card ($): ${result.totalFuelCostWithCard}`);
    console.log(`Total Savings ($): ${result.savings}`);
}
```
