"""
Generated Code Metadata:
========================
Original URL: https://avabase.vercel.app
Prompt: Design a simple web page using HTML, CSS, and JavaScript to display the AVAAI Hunt campaign details, including the campaign pool value and time left to participate.
Generated: DETERMINISTIC_644cd0fd12587c98
Batch ID: 20250622_212702
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
    <title>AVAAI Hunt Campaign</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>AVAAI Hunt Campaign</h1>
        <div id="campaign-details">
            <p><strong>Campaign Pool Value:</strong> <span id="pool-value">$0</span></p>
            <p><strong>Time Left to Participate:</strong> <span id="time-left">00:00:00</span></p>
        </div>
        <button id="participate-button">Participate Now</button>
    </div>

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
}

/* Container styling */
.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Button styling */
button {
    padding: 10px 15px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background-color: #218838;
}
```

```javascript
// script.js

// Function to update the campaign details
function updateCampaignDetails(poolValue, timeLeft) {
    try {
        // Update the pool value
        document.getElementById('pool-value').innerText = `$${poolValue.toFixed(2)}`;
        
        // Update the time left
        document.getElementById('time-left').innerText = timeLeft;
    } catch (error) {
        console.error("Error updating campaign details:", error);
    }
}

// Function to simulate campaign data
function simulateCampaign() {
    const poolValue = Math.random() * 10000; // Random pool value between 0 and 10000
    const timeLeft = formatTimeLeft(3600); // Simulate 1 hour left

    updateCampaignDetails(poolValue, timeLeft);
}

// Function to format time left in HH:MM:SS
function formatTimeLeft(seconds) {
    const hours = String(Math.floor(seconds / 3600)).padStart(2, '0');
    const minutes = String(Math.floor((seconds % 3600) / 60)).padStart(2, '0');
    const secs = String(seconds % 60).padStart(2, '0');
    return `${hours}:${minutes}:${secs}`;
}

// Event listener for the participate button
document.getElementById('participate-button').addEventListener('click', () => {
    alert("Thank you for participating in the AVAAI Hunt campaign!");
});

// Initialize the campaign on page load
window.onload = simulateCampaign;
```
