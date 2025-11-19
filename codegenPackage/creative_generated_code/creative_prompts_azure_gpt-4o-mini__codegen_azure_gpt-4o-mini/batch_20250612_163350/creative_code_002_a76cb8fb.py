"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haitwik.com
Prompt: Create a JavaScript snippet that displays "This is my website" in a loop, inspired by the content of haitwik.com.
Generated: DETERMINISTIC_a76cb8fbf71b9ae0
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a function to display the message in a loop
function displayMessage() {
    // Message to be displayed
    const message = "This is my website";

    // Set the number of repetitions
    const repetitions = 5;

    // Call the loop function to display the message
    loopMessage(message, repetitions);
}

// Function to loop through and display the message
function loopMessage(message, count) {
    // Check if count is a valid number
    if (typeof count !== 'number' || count <= 0) {
        console.error('Count must be a positive number.');
        return;
    }

    for (let i = 0; i < count; i++) {
        // Create a new paragraph element to hold the message
        const paragraph = document.createElement('p');
        paragraph.textContent = message;

        // Append the paragraph to the body of the document
        document.body.appendChild(paragraph);
    }
}

// Invoke the displayMessage function when the document is fully loaded
document.addEventListener('DOMContentLoaded', (event) => {
    displayMessage();
});
```
