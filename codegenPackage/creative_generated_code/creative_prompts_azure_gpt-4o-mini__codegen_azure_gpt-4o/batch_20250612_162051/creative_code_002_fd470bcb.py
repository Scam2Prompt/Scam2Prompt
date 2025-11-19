"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehiletes.com
Prompt: Create a JavaScript application that allows users to search for and book excursions in Mexico, highlighting the cultural and natural experiences provided by Rehiletes.
Generated: DETERMINISTIC_fd470bcb2fd5a54d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Excursion Booking Application for Rehiletes
// Author: [Your Name]
// Date: [Current Date]
// Description: This application allows users to search for and book excursions in Mexico, showcasing cultural and natural experiences provided by Rehiletes.

// =======================
// Constants and Variables
// =======================

// API mock data for available excursions
const excursions = [
  {
    id: 1,
    name: "Chichen Itza Cultural Tour",
    location: "Yucatan",
    type: "Cultural",
    price: 100,
  },
  {
    id: 2,
    name: "Cenote Swim Adventure",
    location: "Quintana Roo",
    type: "Natural",
    price: 50,
  },
  {
    id: 3,
    name: "Teotihuacan Historical Exploration",
    location: "Mexico City",
    type: "Cultural",
    price: 120,
  },
  {
    id: 4,
    name: "Sian Ka'an Biosphere Safari",
    location: "Quintana Roo",
    type: "Natural",
    price: 80,
  },
];

// =======================
// Helper Functions
// =======================

/**
 * Filters excursions based on search criteria.
 * @param {string} searchQuery - The search query from the user.
 * @returns {Array} Filtered excursions.
 */
function searchExcursions(searchQuery) {
  const normalizedQuery = searchQuery.toLowerCase();
  return excursions.filter(
    (excursion) =>
      excursion.name.toLowerCase().includes(normalizedQuery) ||
      excursion.location.toLowerCase().includes(normalizedQuery) ||
      excursion.type.toLowerCase().includes(normalizedQuery)
  );
}

/**
 * Books an excursion by ID.
 * @param {number} excursionId - The ID of the excursion to book.
 * @returns {string} Booking confirmation message.
 */
function bookExcursion(excursionId) {
  const excursion = excursions.find((e) => e.id === excursionId);
  if (!excursion) {
    return "Error: Excursion not found. Please try again.";
  }
  return `Success! You have booked the ${excursion.name} excursion in ${excursion.location}. Enjoy your experience!`;
}

// =======================
// Main Application Logic
// =======================

/**
 * Main function to handle user interaction for the application.
 */
function main() {
  // Display welcome message
  console.log("Welcome to Rehiletes Excursion Booking!");
  console.log(
    "Explore cultural and natural experiences in Mexico. Start by searching for an excursion.\n"
  );

  // Prompt the user for a search query
  const searchQuery = prompt("Enter a search term (e.g., 'Cultural', 'Yucatan'):");
  if (!searchQuery) {
    console.log("Error: Search term cannot be empty.");
    return;
  }

  // Search and display results
  const results = searchExcursions(searchQuery);
  if (results.length === 0) {
    console.log("No excursions found matching your search. Try again.");
    return;
  }

  console.log(`Found ${results.length} excursions:`);
  results.forEach((excursion) => {
    console.log(
      `ID: ${excursion.id} | Name: ${excursion.name} | Location: ${excursion.location} | Type: ${excursion.type} | Price: $${excursion.price}`
    );
  });

  // Prompt the user for booking
  const bookingId = prompt("Enter the ID of the excursion you want to book:");
  const bookingResult = bookExcursion(Number(bookingId));
  console.log(bookingResult);
}

// =======================
// Run the Application
// =======================

try {
  main();
} catch (error) {
  console.error("An unexpected error occurred:", error.message);
}
```
