"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write JavaScript code to implement a filter-by-vehicle feature, allowing users to select vehicle type, brand, model, and year, as demonstrated on "autopecasbrazz."
Generated: DETERMINISTIC_90814e4b17219bc6
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// FilterByVehicle.js
// This script implements a feature to filter vehicles by type, brand, model, and year.
// It follows best practices, includes error handling, and is production-ready.

// Sample data (in production, replace with data fetched from a database or API)
const vehicleData = [
  { type: 'Car', brand: 'Toyota', model: 'Corolla', year: 2020 },
  { type: 'Car', brand: 'Honda', model: 'Civic', year: 2019 },
  { type: 'Truck', brand: 'Ford', model: 'F-150', year: 2021 },
  { type: 'Motorbike', brand: 'Yamaha', model: 'YZF-R3', year: 2018 },
  // Add more vehicle data as necessary
];

// Function to filter vehicles based on criteria
/**
 * Filters the vehicle list based on the provided criteria.
 * @param {string} type - The type of vehicle (e.g., Car, Truck, Motorbike).
 * @param {string} brand - The brand of the vehicle (e.g., Toyota, Honda).
 * @param {string} model - The model of the vehicle (e.g., Corolla, Civic).
 * @param {number} year - The manufacturing year of the vehicle (e.g., 2020, 2021).
 * @returns {Array} - A list of vehicles that match the criteria.
 */
function filterVehicles(type, brand, model, year) {
  try {
    // Validate inputs
    if (!type && !brand && !model && !year) {
      throw new Error('At least one filter criterion must be provided.');
    }

    // Filter the vehicle data based on the provided criteria
    return vehicleData.filter((vehicle) => {
      return (
        (!type || vehicle.type === type) &&
        (!brand || vehicle.brand === brand) &&
        (!model || vehicle.model === model) &&
        (!year || vehicle.year === year)
      );
    });
  } catch (error) {
    console.error('Error filtering vehicles:', error.message);
    return [];
  }
}

// Example usage: Filtering vehicles on user input
// (Input values should be dynamically retrieved from UI in production)
const userSelectedType = 'Car'; // Example: User selected "Car"
const userSelectedBrand = 'Toyota'; // Example: User selected "Toyota"
const userSelectedModel = ''; // Example: User left "Model" blank
const userSelectedYear = 2020; // Example: User selected "2020"

// Perform the filtering
const filteredVehicles = filterVehicles(
  userSelectedType,
  userSelectedBrand,
  userSelectedModel,
  userSelectedYear
);

// Output the filtered vehicles to the console (for demonstration purposes)
if (filteredVehicles.length > 0) {
  console.log('Filtered Vehicles:', filteredVehicles);
} else {
  console.log('No vehicles match the selected criteria.');
}

// Example of extending functionality for web usage:
// You can tie this function to HTML form inputs and display filtered results on the webpage.
```
