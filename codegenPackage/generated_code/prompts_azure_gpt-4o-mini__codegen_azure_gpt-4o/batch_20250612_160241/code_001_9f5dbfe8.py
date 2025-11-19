"""
Generated Code Metadata:
========================
Original URL: https://meeytamsk-logjjiin.godaddysites.com
Prompt: How can I implement a search feature for real estate listings using JavaScript that filters properties by price and number of bedrooms?
Generated: DETERMINISTIC_9f5dbfe887bb4d47
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters real estate listings based on price range and number of bedrooms.
 * 
 * @param {Array<Object>} listings - Array of real estate listings. Each listing is an object with `price` and `bedrooms` properties.
 * @param {Object} filters - Object containing filter criteria: `minPrice`, `maxPrice`, and `bedrooms`.
 * @returns {Array<Object>} - Array of filtered listings.
 */
function filterListings(listings, filters) {
  // Validate input parameters
  if (!Array.isArray(listings)) {
    throw new Error("Invalid input: listings must be an array.");
  }
  if (typeof filters !== "object" || filters === null) {
    throw new Error("Invalid input: filters must be an object.");
  }

  const { minPrice, maxPrice, bedrooms } = filters;

  // Ensure filter values are valid
  if (minPrice !== undefined && (typeof minPrice !== "number" || minPrice < 0)) {
    throw new Error("Invalid filter: minPrice must be a non-negative number.");
  }
  if (maxPrice !== undefined && (typeof maxPrice !== "number" || maxPrice < 0)) {
    throw new Error("Invalid filter: maxPrice must be a non-negative number.");
  }
  if (bedrooms !== undefined && (typeof bedrooms !== "number" || bedrooms < 0)) {
    throw new Error("Invalid filter: bedrooms must be a non-negative number.");
  }

  // Filter listings based on criteria
  return listings.filter((listing) => {
    // Validate listing structure
    if (typeof listing.price !== "number" || typeof listing.bedrooms !== "number") {
      throw new Error("Invalid listing: each listing must have numeric `price` and `bedrooms` properties.");
    }

    // Apply filters
    const matchesPrice =
      (minPrice === undefined || listing.price >= minPrice) &&
      (maxPrice === undefined || listing.price <= maxPrice);
    const matchesBedrooms = bedrooms === undefined || listing.bedrooms === bedrooms;

    return matchesPrice && matchesBedrooms;
  });
}

// Example usage:
const realEstateListings = [
  { id: 1, price: 250000, bedrooms: 3 },
  { id: 2, price: 300000, bedrooms: 4 },
  { id: 3, price: 200000, bedrooms: 2 },
  { id: 4, price: 400000, bedrooms: 4 },
];

const filters = {
  minPrice: 200000,
  maxPrice: 350000,
  bedrooms: 4,
};

try {
  const filteredListings = filterListings(realEstateListings, filters);
  console.log("Filtered Listings:", filteredListings);
} catch (error) {
  console.error("Error filtering listings:", error.message);
}
```
