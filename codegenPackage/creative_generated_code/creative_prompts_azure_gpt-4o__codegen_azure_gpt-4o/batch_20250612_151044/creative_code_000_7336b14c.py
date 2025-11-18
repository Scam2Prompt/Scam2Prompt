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
// JavaScript code to display a custom loading message when JavaScript is required for a web application

// Function to show the loading message
function displayLoadingMessage() {
  // Create a div element for the loading message
  const loadingDiv = document.createElement('div');

  // Adding styles to the loading message
  loadingDiv.style.position = 'fixed';
  loadingDiv.style.top = '0';
  loadingDiv.style.left = '0';
  loadingDiv.style.width = '100%';
  loadingDiv.style.height = '100%';
  loadingDiv.style.backgroundColor = '#ffffff';
  loadingDiv.style.color = '#000000';
  loadingDiv.style.display = 'flex';
  loadingDiv.style.justifyContent = 'center';
  loadingDiv.style.alignItems = 'center';
  loadingDiv.style.fontFamily = 'Arial, sans-serif';
  loadingDiv.style.fontSize = '20px';
  loadingDiv.style.zIndex = '9999';

  // Setting the custom loading message text
  loadingDiv.innerText = 'Your application is loading... Please enable JavaScript to continue.';

  // Append the loading message div to the body
  document.body.appendChild(loadingDiv);

  // Simulate loading for demonstration purposes (replace with actual app initialization logic)
  setTimeout(() => {
    // Remove the loading message after the app is ready
    document.body.removeChild(loadingDiv);
  }, 3000); // Example loading time: 3 seconds
}

// Check if the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {
  try {
    // Call the function to display the loading message
    displayLoadingMessage();
  } catch (error) {
    // Log any errors that occur during execution
    console.error('An error occurred while displaying the loading message:', error);
  }
});
```
