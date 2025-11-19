"""
Generated Code Metadata:
========================
Original URL: https://ittastours.com
Prompt: "Write a JavaScript function to filter and display tour packages based on user preferences for destination, duration, and price range."
Generated: DETERMINISTIC_317d539fe937ae08
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters tour packages based on user preferences for destination, duration, and price range.
 * @param {Array} tourPackages - Array of tour package objects. Each object should have `destination`, `duration`, and `price` properties.
 * @param {Object} preferences - User preferences object containing `destination`, `minDuration`, `maxDuration`, `minPrice`, and `maxPrice`.
 * @returns {Array} - Array of filtered tour packages matching the user preferences.
 */
function filterTourPackages(tourPackages, preferences) {
  // Validate input parameters
  if (!Array.isArray(tourPackages)) {
    throw new Error("Invalid input: tourPackages must be an array.");
  }
  if (typeof preferences !== "object" || preferences === null) {
    throw new Error("Invalid input: preferences must be a non-null object.");
  }

  const {
    destination,
    minDuration = 0,
    maxDuration = Infinity,
    minPrice = 0,
    maxPrice = Infinity,
  } = preferences;

  // Filter tour packages based on user preferences
  return tourPackages.filter((package) => {
    // Validate package structure
    if (
      typeof package.destination !== "string" ||
      typeof package.duration !== "number" ||
      typeof package.price !== "number"
    ) {
      console.warn("Skipping invalid package:", package);
      return false;
    }

    // Check destination match (if specified)
    const destinationMatch =
      !destination || package.destination.toLowerCase() === destination.toLowerCase();

    // Check duration range match
    const durationMatch =
      package.duration >= minDuration && package.duration <= maxDuration;

    // Check price range match
    const priceMatch =
      package.price >= minPrice && package.price <= maxPrice;

    // Return true if all conditions are met
    return destinationMatch && durationMatch && priceMatch;
  });
}

// Example usage:
const tourPackages = [
  { destination: "Paris", duration: 5, price: 1200 },
  { destination: "London", duration: 3, price: 800 },
  { destination: "New York", duration: 7, price: 1500 },
  { destination: "Tokyo", duration: 10, price: 2000 },
];

const userPreferences = {
  destination: "Paris",
  minDuration: 4,
  maxDuration: 6,
  minPrice: 1000,
  maxPrice: 1300,
};

const filteredPackages = filterTourPackages(tourPackages, userPreferences);
console.log("Filtered Tour Packages:", filteredPackages);
```
