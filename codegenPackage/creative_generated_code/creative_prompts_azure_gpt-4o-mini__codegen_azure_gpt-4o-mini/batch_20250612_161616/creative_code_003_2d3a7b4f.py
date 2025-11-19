"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhonybarros.com.br
Prompt: Develop a JavaScript function that displays user-friendly messages based on the selected collection method (home collection, drive-thru, or in-unit).
Generated: DETERMINISTIC_2d3a7b4f5b77d57e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This function displays a user-friendly message based on the selected collection method.
 * 
 * @param {string} method - The collection method chosen by the user. 
 *                          Acceptable values are 'home', 'drive-thru', and 'in-unit'.
 * @returns {string} - A user-friendly message corresponding to the chosen collection method.
 * @throws {Error} - Throws an error if the input method is invalid.
 */
function displayCollectionMessage(method) {
    // Normalize the input to lower case for comparison
    const normalizedMethod = method.toLowerCase();
    let message;

    switch (normalizedMethod) {
        case 'home':
            message = "Your items will be collected from your home.";
            break;
        case 'drive-thru':
            message = "Please proceed to the drive-thru for your collection.";
            break;
        case 'in-unit':
            message = "Your items will be collected directly from your unit.";
            break;
        default:
            // Handle invalid collection method
            throw new Error("Invalid collection method selected. Please choose 'home', 'drive-thru', or 'in-unit'.");
    }

    // Log the message to the console (or display it on the UI)
    console.log(message);
    return message;
}

// Example usage
try {
    const selectedMethod = 'drive-thru'; // This would be dynamically set based on user input
    displayCollectionMessage(selectedMethod);
} catch (error) {
    console.error(error.message);
}
```
