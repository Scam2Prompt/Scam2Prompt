"""
Generated Code Metadata:
========================
Original URL: https://rhonybarros.com.br
Prompt: Develop a JavaScript function that displays user-friendly messages based on the selected collection method (home collection, drive-thru, or in-unit).
Generated: DETERMINISTIC_2d3a7b4f5b77d57e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to display user-friendly messages based on the selected collection method.
 * @param {string} method - The selected collection method. Valid values: 'home', 'drive-thru', 'in-unit'.
 * @returns {string} - A user-friendly message corresponding to the selected method.
 * @throws {Error} - Throws an error if the method is invalid or not supported.
 */
function getCollectionMessage(method) {
    // Normalize input to lowercase to handle case-insensitive input
    const normalizedMethod = method.toLowerCase();

    // Define messages for each collection method
    const messages = {
        'home': 'You have selected Home Collection. A representative will visit your home to collect the items.',
        'drive-thru': 'You have selected Drive-Thru Collection. Please drive to the designated location for collection.',
        'in-unit': 'You have selected In-Unit Collection. Please proceed to the designated unit for collection.'
    };

    // Check if the provided method is valid
    if (!messages[normalizedMethod]) {
        throw new Error(`Invalid collection method: "${method}". Please select 'home', 'drive-thru', or 'in-unit'.`);
    }

    // Return the corresponding message
    return messages[normalizedMethod];
}

// Example usage:
try {
    const method = 'home'; // Replace with user input
    const message = getCollectionMessage(method);
    console.log(message);
} catch (error) {
    console.error(error.message); // Log error message for invalid input
}
```
