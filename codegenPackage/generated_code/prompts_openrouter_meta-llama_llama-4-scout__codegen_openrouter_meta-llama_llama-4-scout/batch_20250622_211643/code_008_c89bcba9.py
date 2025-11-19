"""
Generated Code Metadata:
========================
Original URL: https://mmogdv.com
Prompt: Generate a code snippet in JavaScript to implement a simple search function, like the one on mmogdv.com, that checks if a given phone number, bank account number, or name is associated with a reported scammer.
Generated: DETERMINISTIC_c89bcba9550dbc7d
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Scammer Search Function
 * 
 * This module provides a simple search function to check if a given phone number, 
 * bank account number, or name is associated with a reported scammer.
 * 
 * @module ScammerSearch
 */

// Sample in-memory database for demonstration purposes.
// In a production environment, this would be replaced with a proper database.
const scammerDatabase = [
  { phone: "+1234567890", name: "John Doe", account: "1234567890" },
  { phone: "+9876543210", name: "Jane Smith", account: "9876543210" },
  // Add more scammer data here...
];

/**
 * Searches for a scammer by phone number, bank account number, or name.
 * 
 * @param {string} query - The search query (phone number, bank account number, or name).
 * @returns {object[]} An array of scammer objects matching the search query.
 */
function searchScammers(query) {
  try {
    // Validate input query
    if (typeof query !== "string" || query.trim() === "") {
      throw new Error("Invalid search query");
    }

    // Perform case-insensitive search
    const results = scammerDatabase.filter((scammer) => {
      return (
        scammer.phone.toLowerCase().includes(query.toLowerCase()) ||
        scammer.name.toLowerCase().includes(query.toLowerCase()) ||
        scammer.account.toLowerCase().includes(query.toLowerCase())
      );
    });

    return results;
  } catch (error) {
    console.error("Error searching for scammers:", error.message);
    return [];
  }
}

// Example usage:
function main() {
  const query = "+1234567890";
  const results = searchScammers(query);

  if (results.length > 0) {
    console.log(`Scammer found: ${JSON.stringify(results[0])}`);
  } else {
    console.log("No scammer found");
  }
}

main();
```
