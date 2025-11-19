"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eligibility-resolv.xyz
Prompt: Write a JavaScript function that utilizes `document.write()` to display a welcome message on a webpage.
Generated: DETERMINISTIC_5f1aad4cdf79f333
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Displays a welcome message on the webpage using document.write().
 * NOTE: Use document.write() cautiously as it overwrites the entire document content if called after the page has been fully loaded.
 */
function displayWelcomeMessage() {
    try {
        // Define the welcome message
        const welcomeMessage = "Welcome to our website! We hope you have a great experience.";

        // Use document.write() to display the message
        document.write(`<h1>${welcomeMessage}</h1>`);

        // Optionally, log the action to the console for debugging
        console.log("Welcome message successfully displayed on the webpage.");
    } catch (error) {
        // Handle potential errors gracefully
        console.error("An error occurred while attempting to display the welcome message:", error);
    }
}

// Call the function to display the message
displayWelcomeMessage();
```
