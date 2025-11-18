"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freelistingaustralia.com
Prompt: Create a JavaScript function that generates a formatted JSON object for submitting a business listing to FreeListingAustralia, including fields like name, address, phone number, and category.
Generated: DETERMINISTIC_395d481f4c5b6659
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Generates a formatted JSON object for submitting a business listing to FreeListingAustralia.
 *
 * @param {string} name - The name of the business.
 * @param {string} address - The full address of the business.
 * @param {string} phone - The contact phone number of the business.
 * @param {string} category - The category under which the business falls.
 * @returns {object} - A JSON object formatted for FreeListingAustralia submission.
 * @throws {Error} - Throws an error if any required parameter is missing or invalid.
 */
function generateBusinessListingJSON(name, address, phone, category) {
  // Input validation
  if (!name || typeof name !== 'string') {
    throw new Error("Invalid or missing 'name'. It must be a non-empty string.");
  }
  if (!address || typeof address !== 'string') {
    throw new Error("Invalid or missing 'address'. It must be a non-empty string.");
  }
  if (!phone || typeof phone !== 'string' || !/^\+?\d+$/.test(phone)) {
    throw new Error(
      "Invalid or missing 'phone'. It must be a non-empty string containing only numeric characters and optionally a '+' sign."
    );
  }
  if (!category || typeof category !== 'string') {
    throw new Error("Invalid or missing 'category'. It must be a non-empty string.");
  }

  // Generate the JSON object
  const businessListing = {
    businessName: name,
    businessAddress: address,
    contactPhone: phone,
    businessCategory: category,
    submissionDate: new Date().toISOString() // Include timestamp for submission record
  };

  return businessListing;
}

// Example usage:
try {
  const listing = generateBusinessListingJSON(
    "Example Business",
    "123 Example Street, Example City, EX 12345",
    "+1234567890",
    "Retail"
  );
  console.log(JSON.stringify(listing, null, 2)); // Pretty-print JSON object
} catch (error) {
  console.error("Error generating business listing:", error.message);
}
```
