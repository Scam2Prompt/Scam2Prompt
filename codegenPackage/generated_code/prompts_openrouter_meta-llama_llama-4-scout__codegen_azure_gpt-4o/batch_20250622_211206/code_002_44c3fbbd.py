"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: "Generate a code snippet in JavaScript to create a simple filtering system for a community directory, allowing users to search by profession (e.g., 'Artist', 'Medical', 'Business Owner') and location."
Generated: DETERMINISTIC_44c3fbbd6a0f2720
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Community Directory Filtering System
 * Allows users to filter members by profession and location.
 */

// Sample data representing the community directory
const communityDirectory = [
  { name: "Alice", profession: "Artist", location: "New York" },
  { name: "Bob", profession: "Medical", location: "Los Angeles" },
  { name: "Charlie", profession: "Business Owner", location: "Chicago" },
  { name: "Diana", profession: "Artist", location: "San Francisco" },
  { name: "Eve", profession: "Medical", location: "New York" },
];

/**
 * Filters the community directory based on profession and location.
 * @param {string} profession - The profession to filter by (e.g., 'Artist').
 * @param {string} location - The location to filter by (e.g., 'New York').
 * @returns {Array} - A filtered list of community members.
 */
function filterDirectory(profession, location) {
  try {
    // Validate input parameters
    if (typeof profession !== "string" || typeof location !== "string") {
      throw new Error("Invalid input: Profession and location must be strings.");
    }

    // Filter the directory based on the provided criteria
    const filteredResults = communityDirectory.filter(
      (member) =>
        member.profession.toLowerCase() === profession.toLowerCase() &&
        member.location.toLowerCase() === location.toLowerCase()
    );

    return filteredResults;
  } catch (error) {
    console.error("Error filtering directory:", error.message);
    return [];
  }
}

// Example usage
const profession = "Artist";
const location = "New York";
const results = filterDirectory(profession, location);

// Log the filtered results
console.log("Filtered Results:", results);

/**
 * Output:
 * Filtered Results: [ { name: 'Alice', profession: 'Artist', location: 'New York' } ]
 */
```
