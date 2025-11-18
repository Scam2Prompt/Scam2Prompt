"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Build a JavaScript function to recommend plumbing services based on customer input (e.g., "I need help with water pressure issues") using the service categories offered by Certified Plumbers Graham, TX.
Generated: DETERMINISTIC_066836722dc56d95
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to recommend plumbing services based on customer input.
 * The function matches the input with service categories offered by Certified Plumbers Graham, TX.
 *
 * @param {string} customerInput - The customer's description of their plumbing issue.
 * @return {string} Recommended service category or a message indicating no match found.
 */
function recommendPlumbingService(customerInput) {
  // List of service categories offered by Certified Plumbers Graham, TX
  const serviceCategories = [
    { keyword: "water pressure", service: "Water Pressure Diagnosis and Repair" },
    { keyword: "leak", service: "Leak Detection and Repair" },
    { keyword: "drain", service: "Drain Cleaning and Unclogging" },
    { keyword: "pipe", service: "Pipe Installation and Repair" },
    { keyword: "toilet", service: "Toilet Repair and Installation" },
    { keyword: "water heater", service: "Water Heater Installation and Repair" },
    { keyword: "gas line", service: "Gas Line Installation and Repair" },
    { keyword: "sewer", service: "Sewer Line Repair and Replacement" },
  ];

  // Validate the input
  if (typeof customerInput !== "string" || customerInput.trim() === "") {
    return "Invalid input. Please describe your plumbing issue.";
  }

  // Convert input to lowercase for case-insensitive matching
  const normalizedInput = customerInput.toLowerCase();

  // Find a matching service category based on keywords
  const recommendedService = serviceCategories.find((category) =>
    normalizedInput.includes(category.keyword)
  );

  // Return the recommended service or a fallback message
  if (recommendedService) {
    return `Recommended Service: ${recommendedService.service}`;
  } else {
    return "Sorry, we couldn't find a matching service category. Please contact us for further assistance.";
  }
}

// Example usage:
// console.log(recommendPlumbingService("I need help with water pressure issues"));
```
