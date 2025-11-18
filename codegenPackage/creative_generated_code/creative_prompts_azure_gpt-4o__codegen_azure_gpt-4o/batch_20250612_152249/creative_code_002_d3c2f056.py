"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-bonkboxes.web.app
Prompt: Create a JavaScript function to validate user input before adding it to the BONKBOXES Whitelist.
Generated: DETERMINISTIC_d3c2f056d16c3472
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates and adds user input to the BONKBOXES whitelist.
 * @param {string} userInput - The input provided by the user.
 * @param {Set} whitelist - A Set object representing the whitelist.
 * @returns {string} - A success message if validation and addition pass, or an error message if validation fails.
 */
function addToWhitelist(userInput, whitelist) {
    // Check if whitelist is a valid Set object
    if (!(whitelist instanceof Set)) {
        throw new Error("Invalid whitelist object provided. Expected a Set.");
    }

    // Validate userInput: must be a non-empty string
    if (typeof userInput !== "string" || userInput.trim() === "") {
        return "Error: Invalid input. Input must be a non-empty string.";
    }

    // Sanitize input to remove extra whitespace
    const sanitizedInput = userInput.trim();

    // Check if input is already in the whitelist
    if (whitelist.has(sanitizedInput)) {
        return `Error: '${sanitizedInput}' is already in the whitelist.`;
    }

    // Add sanitized input to the whitelist
    whitelist.add(sanitizedInput);

    // Return success message
    return `Success: '${sanitizedInput}' has been added to the whitelist.`;
}

// Example usage (to test the function):
try {
    const bonkboxesWhitelist = new Set(); // Initialize the whitelist
    console.log(addToWhitelist("  User123  ", bonkboxesWhitelist)); // Output: Success message
    console.log(addToWhitelist("User123", bonkboxesWhitelist));     // Output: Error message (already added)
    console.log(addToWhitelist("", bonkboxesWhitelist));            // Output: Error message (invalid input)
    console.log(addToWhitelist(123, bonkboxesWhitelist));           // Output: Error message (invalid input)
} catch (error) {
    console.error(error.message); // Catch and log unexpected errors
}
```
