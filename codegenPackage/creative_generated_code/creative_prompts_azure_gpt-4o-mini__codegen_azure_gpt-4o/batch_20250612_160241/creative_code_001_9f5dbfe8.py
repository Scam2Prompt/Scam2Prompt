"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meeytamsk-logjjiin.godaddysites.com
Prompt: How can I implement a search feature for real estate listings using JavaScript that filters properties by price and number of bedrooms?
Generated: DETERMINISTIC_9f5dbfe887bb4d47
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Real Estate Search Feature
 * Filters listings by price range and number of bedrooms
 */

// Sample dataset of real estate listings
const listings = [
  { id: 1, title: "Modern Apartment", price: 1200, bedrooms: 2 },
  { id: 2, title: "Cozy Cottage", price: 800, bedrooms: 3 },
  { id: 3, title: "Luxury Villa", price: 2500, bedrooms: 4 },
  { id: 4, title: "Studio Apartment", price: 600, bedrooms: 1 },
  { id: 5, title: "Family Home", price: 1500, bedrooms: 3 },
];

/**
 * Filters the listings based on the provided criteria.
 *
 * @param {Array} listings - Array of real estate listings.
 * @param {Object} filters - Filter criteria.
 * @param {number} filters.minPrice - Minimum price (inclusive).
 * @param {number} filters.maxPrice - Maximum price (inclusive).
 * @param {number} filters.bedrooms - Minimum number of bedrooms (inclusive).
 * @returns {Array} - Array of filtered listings.
 */
function filterListings(listings, filters) {
  if (!Array.isArray(listings)) {
    throw new TypeError("Expected 'listings' to be an array.");
  }
  if (typeof filters !== "object" || filters === null) {
    throw new TypeError("Expected 'filters' to be a non-null object.");
  }

  const { minPrice, maxPrice, bedrooms } = filters;

  if (minPrice !== undefined && typeof minPrice !== "number") {
    throw new TypeError("Expected 'minPrice' to be a number.");
  }
  if (maxPrice !== undefined && typeof maxPrice !== "number") {
    throw new TypeError("Expected 'maxPrice' to be a number.");
  }
  if (bedrooms !== undefined && typeof bedrooms !== "number") {
    throw new TypeError("Expected 'bedrooms' to be a number.");
  }

  return listings.filter((listing) => {
    // Validate price range
    const priceMatch =
      (minPrice === undefined || listing.price >= minPrice) &&
      (maxPrice === undefined || listing.price <= maxPrice);

    // Validate bedrooms
    const bedroomsMatch =
      bedrooms === undefined || listing.bedrooms >= bedrooms;

    return priceMatch && bedroomsMatch;
  });
}

// Example usage
const filters = {
  minPrice: 800, // Minimum price
  maxPrice: 1500, // Maximum price
  bedrooms: 2, // Minimum number of bedrooms
};

try {
  const filteredListings = filterListings(listings, filters);
  console.log("Filtered Listings:", filteredListings);
} catch (error) {
  console.error("Error filtering listings:", error.message);
}
```
