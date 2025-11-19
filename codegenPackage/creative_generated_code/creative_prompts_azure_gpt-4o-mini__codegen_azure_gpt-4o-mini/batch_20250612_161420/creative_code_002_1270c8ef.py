"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://del-pinar.com.ar
Prompt: Create a JavaScript code example that fetches and displays outdoor activity options available at a coastal apart hotel.
Generated: DETERMINISTIC_1270c8efe35e16f2
Batch ID: 20250612_161420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/outdoor-activities": {
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
// Define the API endpoint for fetching outdoor activity options
const API_URL = 'https://api.example.com/outdoor-activities';

// Function to fetch outdoor activities from the API
async function fetchOutdoorActivities() {
    try {
        const response = await fetch(API_URL);
        
        // Check if the response is successful
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        // Parse the JSON response
        const activities = await response.json();
        return activities;

    } catch (error) {
        // Handle errors and log them for debugging
        console.error('Error fetching outdoor activities:', error);
        return []; // Return an empty array on error
    }
}

// Function to display activities on the webpage
function displayActivities(activities) {
    const activitiesList = document.getElementById('activities-list');

    // Clear previous contents
    activitiesList.innerHTML = '';

    // Check if there are any activities to display
    if (activities.length === 0) {
        activitiesList.innerHTML = '<p>No outdoor activities available at this time.</p>';
        return;
    }

    // Create list items for each activity and append to the list
    activities.forEach(activity => {
        const listItem = document.createElement('li');
        listItem.textContent = `${activity.name} - ${activity.description}`;
        activitiesList.appendChild(listItem);
    });
}

// Function to initialize the application
async function init() {
    const activities = await fetchOutdoorActivities();
    displayActivities(activities);
}

// Run the application on page load
document.addEventListener('DOMContentLoaded', init);
```

```html
<!-- HTML structure to display the outdoor activities -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Outdoor Activities</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Outdoor Activities at Coastal Apart Hotel</h1>
    <ul id="activities-list">
        <!-- Activities will be populated here dynamically -->
    </ul>
    <script src="script.js"></script>
</body>
</html>
```
