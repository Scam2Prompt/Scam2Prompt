"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://methasenlogiz.gitbook.io
Prompt: Write code to check if the MetaMask extension is unlocked and ready for use, and display a message to the user accordingly.
Generated: DETERMINISTIC_ffae78aa19809216
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check MetaMask status (is unlocked and ready for use)

// Wait for the DOM to load before executing the script
document.addEventListener('DOMContentLoaded', async () => {
    try {
        // Check if the MetaMask extension is available
        if (typeof window.ethereum !== 'undefined') {
            // MetaMask is installed; check if it's unlocked
            const accounts = await window.ethereum.request({ method: 'eth_accounts' });

            // Check if accounts are returned
            if (accounts.length > 0) {
                // MetaMask is unlocked and ready for use
                displayMessage("MetaMask is unlocked and ready for use!");
            } else {
                // MetaMask is locked
                displayMessage("MetaMask is installed but locked. Please unlock it.");
            }
        } else {
            // MetaMask is not installed
            displayMessage("MetaMask extension is not installed. Please install it to proceed.");
        }
    } catch (error) {
        // Handle errors gracefully
        console.error("An error occurred while checking MetaMask status:", error);
        displayMessage("An error occurred while checking MetaMask status. Please try again.");
    }
});

// Function to display a message to the user
function displayMessage(message) {
    // Create a new element to display the message
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.style.padding = '10px';
    messageElement.style.margin = '10px 0';
    messageElement.style.border = '1px solid #ccc';
    messageElement.style.backgroundColor = '#f9f9f9';
    messageElement.style.fontFamily = 'Arial, sans-serif';

    // Append the element to the body
    document.body.appendChild(messageElement);
}
```
