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
 * Simple search function to check if a given phone number, bank account number, or name
 * is associated with a reported scammer.
 * 
 * This function uses a predefined list of reported scammers for demonstration purposes.
 * In a production environment, this data would typically come from a secure database or API.
 */

// Predefined list of reported scammers (mock data)
const reportedScammers = [
  { phoneNumber: "123-456-7890", bankAccount: "9876543210", name: "John Doe" },
  { phoneNumber: "555-123-4567", bankAccount: "1234567890", name: "Jane Smith" },
  { phoneNumber: "999-888-7777", bankAccount: "1122334455", name: "Alice Johnson" }
];

/**
 * Function to check if the input matches any reported scammer.
 * @param {Object} query - The search query object containing phoneNumber, bankAccount, or name.
 * @returns {Object|null} - Returns the matching scammer object if found, otherwise null.
 */
function searchScammer(query) {
  try {
    // Validate input
    if (!query || typeof query !== 'object') {
      throw new Error("Invalid query object. Please provide a valid search query.");
    }

    const { phoneNumber, bankAccount, name } = query;

    // Search for a matching scammer
    const result = reportedScammers.find(scammer =>
      (phoneNumber && scammer.phoneNumber === phoneNumber) ||
      (bankAccount && scammer.bankAccount === bankAccount) ||
      (name && scammer.name.toLowerCase() === name.toLowerCase())
    );

    return result || null; // Return the matching scammer or null if not found
  } catch (error) {
    console.error("Error during search:", error.message);
    return null; // Return null in case of an error
  }
}

// Example usage
const query1 = { phoneNumber: "123-456-7890" };
const query2 = { name: "Jane Smith" };
const query3 = { bankAccount: "0000000000" }; // Non-existent account

console.log(searchScammer(query1)); // Should return the matching scammer object
console.log(searchScammer(query2)); // Should return the matching scammer object
console.log(searchScammer(query3)); // Should return null (no match)
```
