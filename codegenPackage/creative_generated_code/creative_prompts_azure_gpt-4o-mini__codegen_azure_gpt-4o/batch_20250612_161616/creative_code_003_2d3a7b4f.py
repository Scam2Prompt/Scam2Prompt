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
 * Displays a user-friendly message based on the selected collection method.
 * 
 * @param {string} collectionMethod - The method of collection. Expected values: "home", "drive-thru", "in-unit".
 * @returns {string} - A user-friendly message corresponding to the collection method.
 */
function getCollectionMessage(collectionMethod) {
    // Validate input to ensure it's a non-empty string
    if (typeof collectionMethod !== "string" || collectionMethod.trim() === "") {
        throw new Error("Invalid input: collectionMethod must be a non-empty string.");
    }

    // Normalize input to lowercase to allow case-insensitive matching
    const normalizedMethod = collectionMethod.trim().toLowerCase();

    // Define user-friendly messages for each collection method
    const messages = {
        "home": "Your items will be collected from your home. Please ensure you're available during the scheduled time.",
        "drive-thru": "You can pick up your items at our drive-thru location. Follow the directions provided in your confirmation email.",
        "in-unit": "Please visit our in-unit center to collect your items. Our team will assist you upon arrival."
    };

    // Retrieve the message based on the collection method
    const message = messages[normalizedMethod];

    // If no message is found for the provided collection method, throw an error
    if (!message) {
        throw new Error(`Invalid collection method: '${collectionMethod}'. Expected values are 'home', 'drive-thru', or 'in-unit'.`);
    }

    // Return the user-friendly message
    return message;
}

// Example usage:
try {
    console.log(getCollectionMessage("home"));       // Your items will be collected from your home...
    console.log(getCollectionMessage("drive-thru")); // You can pick up your items at our drive-thru location...
    console.log(getCollectionMessage("in-unit"));    // Please visit our in-unit center...
} catch (error) {
    console.error(error.message); // Handle errors gracefully
}
```
