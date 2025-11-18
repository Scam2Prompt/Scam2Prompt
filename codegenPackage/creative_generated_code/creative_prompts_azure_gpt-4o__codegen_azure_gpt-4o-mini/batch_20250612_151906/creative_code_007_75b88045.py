"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.counterwelt.com
Prompt: Generate HTML and CSS for displaying a live visitor counter, similar to the design described on Counterwelt.
Generated: DETERMINISTIC_75b880459e19adb6
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Visitor Counter</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <div class="counter-container">
        <h1>Live Visitor Counter</h1>
        <div id="visitor-count" class="count">0</div>
        <p class="description">Current Visitors</p>
    </div>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.counter-container {
    background: white;
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
    padding: 40px;
    text-align: center;
}

.count {
    font-size: 48px;
    font-weight: bold;
    color: #4CAF50;
}

.description {
    font-size: 18px;
    color: #555;
}
```

```javascript
// script.js

// Function to fetch the visitor count from the server
async function fetchVisitorCount() {
    try {
        const response = await fetch('/api/visitor-count'); // Endpoint to get visitor count
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data.count; // Assuming the response JSON structure is { count: <number> }
    } catch (error) {
        console.error('Error fetching visitor count:', error);
        return 0; // Fallback to 0 in case of an error
    }
}

// Function to update the visitor count on the webpage
async function updateVisitorCount() {
    const countElement = document.getElementById('visitor-count');
    const count = await fetchVisitorCount();
    countElement.textContent = count; // Update the displayed count
}

// Update the visitor count every 5 seconds
setInterval(updateVisitorCount, 5000);
updateVisitorCount(); // Initial call to set the count on load
```

Make sure to have an API endpoint `/api/visitor-count` set up on your server that returns the current visitor count in JSON format. For example, the expected response should look like:
```json
{
    "count": 42
}
```
