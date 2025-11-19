"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Create a function in JavaScript that calculates the cost of insulation services based on the materials and areas specified in the services provided by the company.
Generated: DETERMINISTIC_b71ac8d84f579b8f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost of insulation services based on materials and areas.
 * @param {Array} services - Array of service objects. Each object should contain:
 *   - material: {string} Type of insulation material (e.g., "fiberglass", "spray foam", "cellulose").
 *   - area: {number} Area in square feet to be insulated.
 * @returns {number} Total cost of insulation services.
 * @throws {Error} Throws an error if input is invalid.
 */
function calculateInsulationCost(services) {
  // Validate input
  if (!Array.isArray(services)) {
    throw new Error("Invalid input: services must be an array.");
  }

  // Define cost per square foot for each material
  const materialCosts = {
    fiberglass: 1.5, // $1.50 per square foot
    sprayFoam: 2.0,  // $2.00 per square foot
    cellulose: 1.8   // $1.80 per square foot
  };

  let totalCost = 0;

  for (const service of services) {
    // Validate service object structure
    if (
      typeof service !== "object" ||
      !service.material ||
      !service.area ||
      typeof service.material !== "string" ||
      typeof service.area !== "number" ||
      service.area <= 0
    ) {
      throw new Error("Invalid service object: Each service must have a valid material and area.");
    }

    // Check if the material is supported
    const costPerSquareFoot = materialCosts[service.material.toLowerCase()];
    if (!costPerSquareFoot) {
      throw new Error(`Unsupported material: ${service.material}`);
    }

    // Calculate cost for the current service
    totalCost += costPerSquareFoot * service.area;
  }

  return totalCost;
}

// Example usage:
try {
  const services = [
    { material: "fiberglass", area: 500 },
    { material: "sprayFoam", area: 300 },
    { material: "cellulose", area: 200 }
  ];
  const totalCost = calculateInsulationCost(services);
  console.log(`Total insulation cost: $${totalCost.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
