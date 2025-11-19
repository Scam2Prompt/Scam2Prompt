"""
Generated Code Metadata:
========================
Original URL: https://treehousesessions.co.uk
Prompt: Create a simple web page using HTML, CSS, and JavaScript to display the schedule for Tree House Sessions Season 3, including artist names and performance dates.
Generated: DETERMINISTIC_52036214e8ccda5a
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tree House Sessions Season 3 Schedule</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Tree House Sessions Season 3 Schedule</h1>
    </header>
    <main>
        <section id="schedule">
            <h2>Performance Schedule</h2>
            <ul id="performance-list"></ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Tree House Sessions. All rights reserved.</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    line-height: 1.6;
}

/* Header styling */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Schedule section styling */
#schedule {
    background: #ffffff;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 20px;
}

/* List styling */
#performance-list {
    list-style-type: none;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Schedule data for Tree House Sessions Season 3
const scheduleData = [
    { artist: "Artist 1", date: "2023-06-01" },
    { artist: "Artist 2", date: "2023-06-08" },
    { artist: "Artist 3", date: "2023-06-15" },
    { artist: "Artist 4", date: "2023-06-22" },
    { artist: "Artist 5", date: "2023-06-29" },
];

// Function to display the schedule on the web page
function displaySchedule() {
    const performanceList = document.getElementById('performance-list');

    // Check if the performance list element exists
    if (!performanceList) {
        console.error("Performance list element not found.");
        return;
    }

    // Iterate over the schedule data and create list items
    scheduleData.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = `${item.artist} - ${item.date}`;
        performanceList.appendChild(listItem);
    });
}

// Execute the displaySchedule function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', displaySchedule);
```
