"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boredturtleyc.netlify.app
Prompt: Write JavaScript code to display a custom loading message when a web application requires JavaScript to run, similar to the behavior described on the "Bored Turtle Yacht Club" webpage.
Generated: DETERMINISTIC_7336b14c02d4d34a
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to display a custom loading message
function displayLoadingMessage() {
    // Create a div element for the loading message
    const loadingDiv = document.createElement('div');
    loadingDiv.id = 'loading-message';
    loadingDiv.style.position = 'fixed';
    loadingDiv.style.top = '0';
    loadingDiv.style.left = '0';
    loadingDiv.style.width = '100%';
    loadingDiv.style.height = '100%';
    loadingDiv.style.backgroundColor = 'rgba(255, 255, 255, 0.8)';
    loadingDiv.style.color = '#333';
    loadingDiv.style.display = 'flex';
    loadingDiv.style.justifyContent = 'center';
    loadingDiv.style.alignItems = 'center';
    loadingDiv.style.fontSize = '24px';
    loadingDiv.style.zIndex = '1000';
    loadingDiv.innerText = 'Loading... Please wait!';

    // Append the loading message to the body
    document.body.appendChild(loadingDiv);
}

// Function to remove the loading message
function removeLoadingMessage() {
    const loadingDiv = document.getElementById('loading-message');
    if (loadingDiv) {
        loadingDiv.remove(); // Remove the loading message if it exists
    }
}

// Display the loading message when the script loads
displayLoadingMessage();

// Simulate a delay to represent loading time (for demonstration purposes)
setTimeout(() => {
    // Remove loading message after simulated load
    removeLoadingMessage();
    // Here you can initialize your main application logic
}, 3000); // Adjust the timeout as needed (3000ms = 3 seconds)

// Error handling for unsupported browsers (if necessary)
if (typeof document === 'undefined') {
    console.error('This web application requires JavaScript to run properly.');
}
```
