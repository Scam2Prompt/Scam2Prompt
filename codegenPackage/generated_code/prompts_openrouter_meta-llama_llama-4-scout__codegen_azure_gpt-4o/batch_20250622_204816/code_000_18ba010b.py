"""
Generated Code Metadata:
========================
Original URL: https://parsflooring.net
Prompt: Write a JavaScript code snippet to create a simple flooring calculator that estimates the total cost of flooring materials based on room dimensions and material prices.
Generated: DETERMINISTIC_18ba010b20d2d2a3
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Flooring Calculator
 * This script calculates the total cost of flooring materials based on room dimensions and material price per square foot.
 * 
 * Usage:
 * Call the `calculateFlooringCost` function with room dimensions and material price as arguments.
 * Example: calculateFlooringCost(10, 12, 3.5);
 */

/**
 * Calculates the total cost of flooring materials.
 * @param {number} length - The length of the room in feet.
 * @param {number} width - The width of the room in feet.
 * @param {number} pricePerSquareFoot - The price of flooring material per square foot.
 * @returns {number} - The total cost of flooring materials.
 */
function calculateFlooringCost(length, width, pricePerSquareFoot) {
  // Input validation
  if (typeof length !== 'number' || length <= 0) {
    throw new Error("Invalid room length. Length must be a positive number.");
  }
  if (typeof width !== 'number' || width <= 0) {
    throw new Error("Invalid room width. Width must be a positive number.");
  }
  if (typeof pricePerSquareFoot !== 'number' || pricePerSquareFoot <= 0) {
    throw new Error("Invalid material price. Price must be a positive number.");
  }

  // Calculate the area of the room
  const area = length * width;

  // Calculate the total cost
  const totalCost = area * pricePerSquareFoot;

  // Return the total cost
  return totalCost;
}

// Example usage
try {
  const roomLength = 10; // Length of the room in feet
  const roomWidth = 12;  // Width of the room in feet
  const materialPrice = 3.5; // Price per square foot of flooring material

  const totalCost = calculateFlooringCost(roomLength, roomWidth, materialPrice);
  console.log(`The total cost of flooring materials is $${totalCost.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
