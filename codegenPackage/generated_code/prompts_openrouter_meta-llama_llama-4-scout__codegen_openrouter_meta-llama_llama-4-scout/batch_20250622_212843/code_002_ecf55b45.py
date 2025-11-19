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
/**
 * Calculates the estimated cost of automatic garage door installations.
 * 
 * @author [Your Name]
 */

// Define a class for the calculator
class GarageDoorCalculator {
  /**
   * Constructor for the calculator.
   */
  constructor() {
    // Define the base prices for different types of doors
    this.doorPrices = {
      'single-panel': 800,
      'multi-panel': 1200,
      'sectional': 1500,
      'rolling': 1000,
    };

    // Define the prices for additional services
    this.servicePrices = {
      'installation': 500,
      'programming': 100,
      'maintenance': 200,
    };
  }

  /**
   * Calculates the total cost of the garage door installation.
   * 
   * @param {string} doorType The type of garage door.
   * @param {string[]} services The services provided by Trimatic Puertas Automáticas.
   * @returns {number} The estimated total cost.
   */
  calculateTotalCost(doorType, services) {
    // Check if the door type is valid
    if (!(doorType in this.doorPrices)) {
      throw new Error(`Invalid door type: ${doorType}`);
    }

    // Calculate the base cost of the door
    let totalCost = this.doorPrices[doorType];

    // Add the cost of services
    services.forEach((service) => {
      if (!(service in this.servicePrices)) {
        throw new Error(`Invalid service: ${service}`);
      }
      totalCost += this.servicePrices[service];
    });

    return totalCost;
  }

  /**
   * Generates a detailed estimate of the costs.
   * 
   * @param {string} doorType The type of garage door.
   * @param {string[]} services The services provided by Trimatic Puertas Automáticas.
   * @returns {object} An object containing the detailed estimate.
   */
  generateDetailedEstimate(doorType, services) {
    try {
      // Calculate the total cost
      const totalCost = this.calculateTotalCost(doorType, services);

      // Create a detailed estimate object
      const estimate = {
        doorType,
        doorPrice: this.doorPrices[doorType],
        services: services.map((service) => ({
          service,
          price: this.servicePrices[service],
        })),
        totalCost,
      };

      return estimate;
    } catch (error) {
      // Return an error message if there's an issue with the input
      return { error: error.message };
    }
  }
}

// Example usage
function main() {
  const calculator = new GarageDoorCalculator();
  const doorType = 'sectional';
  const services = ['installation', 'programming'];

  const detailedEstimate = calculator.generateDetailedEstimate(doorType, services);
  console.log(detailedEstimate);
}

main();
```
