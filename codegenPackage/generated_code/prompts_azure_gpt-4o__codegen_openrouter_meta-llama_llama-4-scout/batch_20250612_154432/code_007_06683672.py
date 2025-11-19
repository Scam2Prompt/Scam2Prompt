"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Build a JavaScript function to recommend plumbing services based on customer input (e.g., "I need help with water pressure issues") using the service categories offered by Certified Plumbers Graham, TX.
Generated: DETERMINISTIC_066836722dc56d95
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Plumbing Service Recommendation Function
 * 
 * This function takes customer input and recommends plumbing services based on the service categories offered by Certified Plumbers Graham, TX.
 */

// Define the service categories offered by Certified Plumbers Graham, TX
const serviceCategories = {
  "water pressure issues": ["Water Pressure Adjustment", "Water Pump Installation", "Pipe Inspection"],
  "leaky faucets": ["Faucet Repair", "Faucet Replacement", "Drip Fix"],
  "clogged drains": ["Drain Cleaning", "Drain Inspection", "Pipe Descaling"],
  "toilet installation": ["Toilet Installation", "Toilet Replacement", "Toilet Repair"],
  "general plumbing": ["Plumbing Inspection", "Pipe Repair", "Fixture Installation"]
};

/**
 * Recommends plumbing services based on customer input.
 * 
 * @param {string} customerInput - The customer's plumbing issue (e.g., "I need help with water pressure issues").
 * @returns {string[]} An array of recommended plumbing services.
 */
function recommendPlumbingServices(customerInput) {
  try {
    // Convert customer input to lowercase for case-insensitive matching
    customerInput = customerInput.toLowerCase();

    // Use regular expression to extract keywords from customer input
    const keywords = customerInput.match(/\b\w+\b/g);

    // Initialize an empty array to store recommended services
    let recommendedServices = [];

    // Iterate over each keyword
    keywords.forEach(keyword => {
      // Check if the keyword matches a service category
      if (Object.keys(serviceCategories).includes(keyword)) {
        // Add services for the matched category to the recommended services array
        recommendedServices = recommendedServices.concat(serviceCategories[keyword]);
      }
    });

    // If no services are recommended, suggest general plumbing services
    if (recommendedServices.length === 0) {
      recommendedServices = serviceCategories["general plumbing"];
    }

    // Return the recommended services
    return recommendedServices;
  } catch (error) {
    // Log and rethrow any errors
    console.error("Error recommending plumbing services:", error);
    throw error;
  }
}

// Example usage:
const customerInput = "I need help with water pressure issues";
const recommendedServices = recommendPlumbingServices(customerInput);
console.log("Recommended Services:");
console.log(recommendedServices);
```
