"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dunhill-servicedapartments.com
Prompt: Generate JavaScript code to implement a filter functionality for a webpage that allows users to search for apartments by price, type, number of bedrooms, and bathrooms, similar to the filters on the Dunhill Serviced Apartments website.
Generated: DETERMINISTIC_fbb8e6f9a36b35d3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Filter functionality for apartments based on price, type, number of bedrooms, and bathrooms

// Sample apartment data (in a real-world scenario, this would come from a database or API)
const apartments = [
  { id: 1, name: "Apartment A", price: 1200, type: "Studio", bedrooms: 1, bathrooms: 1 },
  { id: 2, name: "Apartment B", price: 1800, type: "1-Bedroom", bedrooms: 1, bathrooms: 1 },
  { id: 3, name: "Apartment C", price: 2500, type: "2-Bedroom", bedrooms: 2, bathrooms: 2 },
  { id: 4, name: "Apartment D", price: 3000, type: "3-Bedroom", bedrooms: 3, bathrooms: 2 },
  { id: 5, name: "Apartment E", price: 1000, type: "Studio", bedrooms: 1, bathrooms: 1 },
];

// Function to filter apartments based on user-defined criteria
function filterApartments(apartments, filters) {
  /*
   * Filters object structure:
   * {
   *   priceRange: { min: Number, max: Number },
   *   type: String,
   *   bedrooms: Number,
   *   bathrooms: Number
   * }
   */

  // Perform filtering based on provided criteria
  return apartments.filter((apartment) => {
    // Check price range
    if (filters.priceRange) {
      const { min, max } = filters.priceRange;
      if (apartment.price < min || apartment.price > max) return false;
    }

    // Check type
    if (filters.type && apartment.type !== filters.type) return false;

    // Check number of bedrooms
    if (filters.bedrooms && apartment.bedrooms !== filters.bedrooms) return false;

    // Check number of bathrooms
    if (filters.bathrooms && apartment.bathrooms !== filters.bathrooms) return false;

    return true; // Include apartment if all criteria are matched
  });
}

// Example usage
const userFilters = {
  priceRange: { min: 1000, max: 2000 },
  type: "Studio",
  bedrooms: 1,
  bathrooms: 1,
};

try {
  // Filter apartments based on user input
  const filteredApartments = filterApartments(apartments, userFilters);

  // Output the filtered apartments
  console.log("Filtered Apartments:", filteredApartments);
} catch (error) {
  // Handle unexpected errors
  console.error("An error occurred while filtering apartments:", error.message);
}
```

This code is ready to be used in a production-grade environment and can be integrated into a webpage with minor modifications, such as wiring it to front-end controls like dropdowns, input fields, and buttons.
