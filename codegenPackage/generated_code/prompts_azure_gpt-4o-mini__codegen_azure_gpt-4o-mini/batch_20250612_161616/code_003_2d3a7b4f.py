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
 * Displays a user-friendly message based on the selected collection method.
 * 
 * @param {string} method - The collection method selected by the user. 
 *                          It can be 'home', 'drive-thru', or 'in-unit'.
 * @throws {Error} Will throw an error if the method is not recognized.
 */
function displayCollectionMessage(method) {
    // Normalize the input to lowercase to handle case sensitivity
    const normalizedMethod = method.toLowerCase();

    // Define messages for each collection method
    const messages = {
        home: "Your items will be collected from your home. Please ensure they are ready for pickup.",
        driveThru: "You can pick up your items at the drive-thru. Please follow the signs for collection.",
        inUnit: "Your items will be delivered directly to your unit. Please be available to receive them."
    };

    // Check if the selected method is valid and display the corresponding message
    if (messages[normalizedMethod]) {
        console.log(messages[normalizedMethod]);
    } else {
        // Throw an error if the method is not recognized
        throw new Error("Invalid collection method selected. Please choose 'home', 'drive-thru', or 'in-unit'.");
    }
}

// Example usage:
try {
    displayCollectionMessage('home'); // Valid input
    displayCollectionMessage('drive-thru'); // Valid input
    displayCollectionMessage('in-unit'); // Valid input
    displayCollectionMessage('invalid-method'); // Invalid input to demonstrate error handling
} catch (error) {
    console.error(error.message); // Log the error message to the console
}
```
