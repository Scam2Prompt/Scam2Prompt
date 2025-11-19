"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecbc.online
Prompt: Write a JavaScript function that retrieves the ECBC Radio programming schedule and displays it in a user-friendly format on a webpage.
Generated: DETERMINISTIC_d25e90a121c9a0c4
Batch ID: 20250612_155751
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ecbcradio.com/schedule": {
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
/**
 * Fetches the ECBC Radio programming schedule from a given API endpoint
 * and displays it in a user-friendly format on the webpage.
 */
async function fetchAndDisplaySchedule() {
    const apiEndpoint = 'https://api.ecbcradio.com/schedule'; // Replace with the actual API endpoint
    
    try {
        // Fetch the programming schedule from the API
        const response = await fetch(apiEndpoint);
        
        // Check if the response is successful
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        // Parse the JSON response
        const scheduleData = await response.json();
        
        // Call function to display the schedule on the webpage
        displaySchedule(scheduleData);
    } catch (error) {
        // Log any errors that occur during the fetch
        console.error('Failed to fetch schedule:', error);
        document.getElementById('schedule').innerHTML = 'Error loading schedule. Please try again later.';
    }
}

/**
 * Displays the programming schedule on the webpage
 * @param {Object} scheduleData - The schedule data retrieved from the API
 */
function displaySchedule(scheduleData) {
    const scheduleContainer = document.getElementById('schedule');
    
    // Clear the existing content
    scheduleContainer.innerHTML = '';

    // Create a list to display the programming schedule
    const scheduleList = document.createElement('ul');

    // Iterate over each program in the schedule data
    scheduleData.programs.forEach(program => {
        // Create a list item for each program
        const listItem = document.createElement('li');
        listItem.textContent = `${program.time}: ${program.title} - ${program.description}`;
        
        // Append the list item to the schedule list
        scheduleList.appendChild(listItem);
    });

    // Append the schedule list to the container
    scheduleContainer.appendChild(scheduleList);
}

// Call the function to fetch and display the schedule when the document is ready
document.addEventListener('DOMContentLoaded', fetchAndDisplaySchedule);
```

### HTML Structure
Make sure to include an HTML element with the ID "schedule" where the schedule will be displayed:

```html
<div id="schedule">Loading schedule...</div>
```

### Note
Ensure to replace the API endpoint with the actual URL where the ECBC Radio programming schedule can be fetched.
