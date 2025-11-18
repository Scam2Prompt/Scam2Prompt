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
<!-- visitor-counter.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Live Visitor Counter">
    <title>Live Visitor Counter</title>
    <link rel="stylesheet" href="styles.css">
    <!-- Link to an external JavaScript file -->
    <script defer src="visitor-counter.js"></script>
</head>
<body>
    <div class="counter-container">
        <h1>Live Visitor Counter</h1>
        <div id="visitor-counter" class="visitor-counter">
            <!-- Placeholder for the counter number -->
            <span id="counter-number">0</span>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f3f4f6;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.counter-container {
    text-align: center;
    background: white;
    padding: 20px 40px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin: 0;
    font-size: 1.8em;
    color: #333;
}

.visitor-counter {
    margin-top: 20px;
    font-size: 48px;
    font-weight: bold;
    color: #007bff;
    border: 2px solid #007bff;
    border-radius: 5px;
    padding: 10px 20px;
    display: inline-block;
}
```

```javascript
// visitor-counter.js

// Generate a live visitor counter
// Note: Replace `YOUR_API_URL` with the actual backend endpoint that provides the live visitor count.

document.addEventListener('DOMContentLoaded', () => {
    const counterElement = document.getElementById('counter-number');

    // Function to fetch the current visitor count from the server
    const fetchVisitorCount = async () => {
        try {
            const response = await fetch('YOUR_API_URL');
            if (!response.ok) {
                throw new Error(`Failed to fetch visitor count: ${response.statusText}`);
            }
            const data = await response.json();
            counterElement.textContent = data.visitorCount || 0; // Update the counter
        } catch (error) {
            console.error(error);
            counterElement.textContent = 'Error'; // Show 'Error' if fetching fails
        }
    };

    // Fetch the visitor count periodically (every 5 seconds)
    fetchVisitorCount(); // Fetch on load
    setInterval(fetchVisitorCount, 5000); // Fetch every 5 seconds
});
```

> Note: Replace `YOUR_API_URL` with the actual URL of your API endpoint that provides the visitor count in JSON format (e.g., `{ "visitorCount": 123 }`). Server-side implementation for tracking visitors should be handled separately.
