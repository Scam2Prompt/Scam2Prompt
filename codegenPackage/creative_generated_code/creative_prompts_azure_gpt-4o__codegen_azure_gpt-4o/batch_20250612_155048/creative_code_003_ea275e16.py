"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Write a function in JavaScript to filter CM-Canada's plumbing fixtures catalog (Liv fixtures™) by price range and certification standards.
Generated: DETERMINISTIC_ea275e168ef1d701
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters CM-Canada's plumbing fixtures catalog (Liv fixtures™) by price range and certification standards.
 * 
 * @param {Array} catalog - Array of plumbing fixtures, each fixture is an object with properties `name`, `price`, and `certifications`.
 * @param {Object} filterCriteria - Object containing `minPrice`, `maxPrice`, and `certifications` to filter the catalog.
 *   - `minPrice` (number): The minimum price of fixtures to include.
 *   - `maxPrice` (number): The maximum price of fixtures to include.
 *   - `certifications` (Array): List of certification standards to filter by (e.g., ["CSA", "UPC"]).
 * @returns {Array} - Array of fixtures that match the filter criteria.
 */
function filterPlumbingFixtures(catalog, filterCriteria) {
  // Validate inputs
  if (!Array.isArray(catalog)) {
    throw new Error("Invalid catalog: Expected an array of fixtures.");
  }

  if (
    typeof filterCriteria !== "object" ||
    filterCriteria === null ||
    typeof filterCriteria.minPrice !== "number" ||
    typeof filterCriteria.maxPrice !== "number" ||
    !Array.isArray(filterCriteria.certifications)
  ) {
    throw new Error("Invalid filterCriteria: Expected an object with minPrice, maxPrice, and certifications.");
  }

  // Destructure filter criteria
  const { minPrice, maxPrice, certifications } = filterCriteria;

  // Filter the catalog
  return catalog.filter((fixture) => {
    // Ensure fixture has valid properties
    if (
      typeof fixture !== "object" ||
      fixture === null ||
      typeof fixture.price !== "number" ||
      !Array.isArray(fixture.certifications)
    ) {
      console.warn("Skipping invalid fixture:", fixture);
      return false;
    }

    // Check if the fixture's price is within the range
    const isPriceInRange = fixture.price >= minPrice && fixture.price <= maxPrice;

    // Check if the fixture matches any of the desired certification standards
    const hasRequiredCertifications = certifications.some((certification) =>
      fixture.certifications.includes(certification)
    );

    // Return true if both conditions are met
    return isPriceInRange && hasRequiredCertifications;
  });
}

// Example usage:
// Define the catalog of plumbing fixtures
const plumbingFixturesCatalog = [
  { name: "Fixture A", price: 120, certifications: ["CSA", "UPC"] },
  { name: "Fixture B", price: 80, certifications: ["CSA"] },
  { name: "Fixture C", price: 200, certifications: ["UPC"] },
  { name: "Fixture D", price: 150, certifications: [] },
];

// Define filter criteria
const filterCriteria = {
  minPrice: 100,
  maxPrice: 200,
  certifications: ["CSA", "UPC"]
};

// Filter the catalog
const filteredFixtures = filterPlumbingFixtures(plumbingFixturesCatalog, filterCriteria);

// Log the filtered fixtures
console.log("Filtered Fixtures:", filteredFixtures);
```
