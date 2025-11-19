"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status.ttec.smartteam.chat
Prompt: Create a JavaScript function that checks the current status of the TTEC STC Cluster and displays it on a webpage.
Generated: DETERMINISTIC_9ea5676c751a8bef
Batch ID: 20250612_161044
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/ttec-status": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Define the function to check the TTEC STC Cluster status
async function checkTTECClusterStatus() {
    const statusUrl = 'https://api.example.com/ttec-status'; // Replace with actual API endpoint

    try {
        // Fetch the current status from the API
        const response = await fetch(statusUrl);

        // Check if the response is ok (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the JSON response
        const data = await response.json();

        // Display the status on the webpage
        displayStatus(data.status); // Assuming the response has a 'status' property

    } catch (error) {
        // Handle any errors that occurred during the fetch operation
        console.error('Error fetching TTEC STC Cluster status:', error);
        displayError('Failed to retrieve status. Please try again later.');
    }
}

// Function to display the status on the webpage
function displayStatus(status) {
    const statusElement = document.getElementById('cluster-status'); // Ensure this element exists in your HTML
    statusElement.textContent = `Current Cluster Status: ${status}`;
    statusElement.style.color = status === 'Operational' ? 'green' : 'red'; // Change color based on status
}

// Function to display error messages on the webpage
function displayError(message) {
    const errorElement = document.getElementById('error-message'); // Ensure this element exists in your HTML
    errorElement.textContent = message;
    errorElement.style.color = 'red';
}

// Call the function to check the status when the document is ready
document.addEventListener('DOMContentLoaded', () => {
    checkTTECClusterStatus();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TTEC STC Cluster Status</title>
</head>
<body>
    <h1>TTEC STC Cluster Status</h1>
    <div id="cluster-status">Checking status...</div>
    <div id="error-message"></div>

    <script src="path/to/your/script.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
