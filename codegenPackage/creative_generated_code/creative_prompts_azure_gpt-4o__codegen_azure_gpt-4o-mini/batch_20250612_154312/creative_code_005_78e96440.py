"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitaldhara.com
Prompt: Write a JavaScript code snippet for frontend web development, leveraging the expertise in mobile and web development described by Digital Dhara.
Generated: DETERMINISTIC_78e964405a4ff55c
Batch ID: 20250612_154312
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/data": {
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
// Utility function to fetch data from an API
async function fetchData(url) {
    try {
        const response = await fetch(url);
        
        // Check if the response is OK (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        // Parse JSON data from the response
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error fetching data:", error);
        throw error; // Re-throw the error for further handling
    }
}

// Function to display data on the webpage
function displayData(data) {
    const outputElement = document.getElementById("output");
    outputElement.innerHTML = ""; // Clear previous content

    // Create and append elements to display the data
    data.forEach(item => {
        const div = document.createElement("div");
        div.classList.add("data-item");
        div.textContent = JSON.stringify(item); // Displaying item as a JSON string for clarity
        outputElement.appendChild(div);
    });
}

// Main function to initiate data fetching and display
async function init() {
    const apiUrl = "https://api.example.com/data"; // Replace with your API URL

    try {
        const data = await fetchData(apiUrl);
        displayData(data);
    } catch (error) {
        const outputElement = document.getElementById("output");
        outputElement.textContent = "Failed to load data. Please try again later.";
    }
}

// Event listener for DOMContentLoaded to ensure the DOM is fully loaded before running the init function
document.addEventListener("DOMContentLoaded", init);
```

```html
<!-- HTML structure to support the JavaScript functionality -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Fetch Example</title>
    <style>
        .data-item {
            border: 1px solid #ccc;
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Fetched Data</h1>
    <div id="output"></div>
    
    <script src="script.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
