"""
Generated Code Metadata:
========================
Original URL: https://gardennovaera.com.br
Prompt: Develop a JavaScript function to calculate the total cost of a stay at a hotel like Garden Hotel, considering room types and additional services.
Generated: DETERMINISTIC_2aefa6520e5169e6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the total cost of a stay at a hotel.
 * @param {string} roomType - The type of room selected (e.g., "standard", "deluxe", "suite").
 * @param {number} nights - The number of nights staying at the hotel.
 * @param {Array<string>} services - List of additional services selected (e.g., ["breakfast", "spa", "parking"]).
 * @returns {number} - The total cost of the stay.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateHotelStayCost(roomType, nights, services) {
  // Validate input
  if (typeof roomType !== 'string' || typeof nights !== 'number' || !Array.isArray(services)) {
    throw new Error('Invalid input. Please provide valid room type, number of nights, and services.');
  }
  if (nights <= 0) {
    throw new Error('Number of nights must be greater than zero.');
  }

  // Room type pricing
  const roomPrices = {
    standard: 100, // Price per night for standard room
    deluxe: 150,   // Price per night for deluxe room
    suite: 250     // Price per night for suite
  };

  // Service pricing
  const servicePrices = {
    breakfast: 20, // Price per day for breakfast
    spa: 50,       // Price per day for spa access
    parking: 15    // Price per day for parking
  };

  // Check if the room type is valid
  if (!roomPrices.hasOwnProperty(roomType)) {
    throw new Error(`Invalid room type: ${roomType}. Valid options are: ${Object.keys(roomPrices).join(', ')}`);
  }

  // Calculate room cost
  const roomCost = roomPrices[roomType] * nights;

  // Calculate services cost
  let servicesCost = 0;
  for (const service of services) {
    if (!servicePrices.hasOwnProperty(service)) {
      throw new Error(`Invalid service: ${service}. Valid options are: ${Object.keys(servicePrices).join(', ')}`);
    }
    servicesCost += servicePrices[service] * nights;
  }

  // Calculate total cost
  const totalCost = roomCost + servicesCost;

  return totalCost;
}

// Example usage:
try {
  const totalCost = calculateHotelStayCost('deluxe', 3, ['breakfast', 'spa']);
  console.log(`Total cost of stay: $${totalCost}`);
} catch (error) {
  console.error(error.message);
}
```
