"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Generate code in JavaScript to create a simple calculator for estimating costs of automatic garage door installations, taking into account the type of door and services provided by Trimatic Puertas Automáticas.
Generated: DETERMINISTIC_ecf55b453140025e
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Simple Calculator for Estimating Costs of Automatic Garage Door Installations
// by Trimatic Puertas Automáticas

// Define a class for the Calculator
class GarageDoorCalculator {
    constructor() {
        // Define base prices for different types of doors
        this.doorPrices = {
            'standard': 1000,
            'premium': 1500,
            'luxury': 2000
        };

        // Define service prices
        this.servicePrices = {
            'installation': 300,
            'removal': 150,
            'maintenance': 100
        };
    }

    /**
     * Calculate the total cost based on door type and selected services.
     * @param {string} doorType - The type of garage door.
     * @param {Array<string>} services - List of services to include in the estimate.
     * @returns {number} - The total estimated cost.
     * @throws {Error} - Throws an error if the door type or service is invalid.
     */
    calculateTotalCost(doorType, services) {
        // Validate door type
        if (!this.doorPrices[doorType]) {
            throw new Error(`Invalid door type: ${doorType}. Valid types are: ${Object.keys(this.doorPrices).join(', ')}`);
        }

        // Initialize total cost with the base price of the selected door type
        let totalCost = this.doorPrices[doorType];

        // Add the cost of selected services
        services.forEach(service => {
            if (this.servicePrices[service]) {
                totalCost += this.servicePrices[service];
            } else {
                throw new Error(`Invalid service: ${service}. Valid services are: ${Object.keys(this.servicePrices).join(', ')}`);
            }
        });

        return totalCost;
    }
}

// Example usage
try {
    const calculator = new GarageDoorCalculator();
    const doorType = 'premium'; // Example door type
    const services = ['installation', 'maintenance']; // Example services

    // Calculate the total cost
    const totalCost = calculator.calculateTotalCost(doorType, services);
    console.log(`The total estimated cost for a ${doorType} door with selected services is: $${totalCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
