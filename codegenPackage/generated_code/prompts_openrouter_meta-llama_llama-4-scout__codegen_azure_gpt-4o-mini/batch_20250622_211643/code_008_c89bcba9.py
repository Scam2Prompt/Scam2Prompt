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
// Simple Search Function to Check for Reported Scammers
// This function checks if a given phone number, bank account number, or name
// is associated with a reported scammer from a predefined list.

class ScammerDatabase {
    constructor() {
        // Sample data representing reported scammers
        this.scammers = [
            { name: "John Doe", phone: "123-456-7890", bankAccount: "987654321" },
            { name: "Jane Smith", phone: "098-765-4321", bankAccount: "123456789" },
            // Add more scammers as needed
        ];
    }

    /**
     * Searches for a scammer by name, phone number, or bank account number.
     * @param {string} query - The search term (name, phone, or bank account).
     * @returns {Array} - An array of matching scammers or an empty array if none found.
     */
    search(query) {
        if (typeof query !== 'string') {
            throw new Error("Query must be a string.");
        }

        // Normalize the query to lower case for case-insensitive search
        const normalizedQuery = query.toLowerCase();

        // Filter the scammers based on the query
        const results = this.scammers.filter(scammer => {
            return (
                scammer.name.toLowerCase().includes(normalizedQuery) ||
                scammer.phone.includes(normalizedQuery) ||
                scammer.bankAccount.includes(normalizedQuery)
            );
        });

        return results;
    }
}

// Example usage
try {
    const scammerDB = new ScammerDatabase();
    const searchTerm = "123-456-7890"; // Example search term
    const results = scammerDB.search(searchTerm);

    if (results.length > 0) {
        console.log("Scammer(s) found:", results);
    } else {
        console.log("No scammers found for the given search term.");
    }
} catch (error) {
    console.error("An error occurred during the search:", error.message);
}
```
