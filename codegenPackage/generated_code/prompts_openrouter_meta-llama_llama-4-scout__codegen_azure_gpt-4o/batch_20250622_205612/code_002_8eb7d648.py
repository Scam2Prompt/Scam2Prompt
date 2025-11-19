"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a JavaScript code to implement a filtering system for auto parts products, allowing users to filter by vehicle type (e.g., Caminhão, Carro, Moto, Ônibus) and product category (e.g., Suspensão, Motor, Elétrica).
Generated: DETERMINISTIC_8eb7d6482703e8c4
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Auto Parts Filtering System

// Sample data representing auto parts products
const autoParts = [
  { id: 1, name: "Suspensão A", vehicleType: "Carro", category: "Suspensão" },
  { id: 2, name: "Motor B", vehicleType: "Moto", category: "Motor" },
  { id: 3, name: "Elétrica C", vehicleType: "Ônibus", category: "Elétrica" },
  { id: 4, name: "Suspensão D", vehicleType: "Caminhão", category: "Suspensão" },
  { id: 5, name: "Motor E", vehicleType: "Carro", category: "Motor" },
  { id: 6, name: "Elétrica F", vehicleType: "Moto", category: "Elétrica" },
];

// Function to filter auto parts based on vehicle type and product category
/**
 * Filters auto parts based on the provided criteria.
 * @param {string} vehicleType - The type of vehicle (e.g., Caminhão, Carro, Moto, Ônibus).
 * @param {string} category - The product category (e.g., Suspensão, Motor, Elétrica).
 * @returns {Array} - A filtered list of auto parts matching the criteria.
 */
function filterAutoParts(vehicleType, category) {
  try {
    // Validate input parameters
    if (!vehicleType && !category) {
      throw new Error("At least one filter criterion (vehicleType or category) must be provided.");
    }

    // Filter the auto parts based on the criteria
    const filteredParts = autoParts.filter((part) => {
      const matchesVehicleType = vehicleType ? part.vehicleType === vehicleType : true;
      const matchesCategory = category ? part.category === category : true;
      return matchesVehicleType && matchesCategory;
    });

    return filteredParts;
  } catch (error) {
    console.error("Error filtering auto parts:", error.message);
    return [];
  }
}

// Example usage
const vehicleTypeFilter = "Carro"; // Filter by vehicle type
const categoryFilter = "Motor"; // Filter by product category

const filteredResults = filterAutoParts(vehicleTypeFilter, categoryFilter);
console.log("Filtered Auto Parts:", filteredResults);

// Example: Filtering with only one criterion
const filteredByVehicleType = filterAutoParts("Moto", null);
console.log("Filtered by Vehicle Type:", filteredByVehicleType);

const filteredByCategory = filterAutoParts(null, "Suspensão");
console.log("Filtered by Category:", filteredByCategory);

// Example: Handling invalid input
const invalidFilter = filterAutoParts(null, null);
console.log("Invalid Filter Result:", invalidFilter);
```
