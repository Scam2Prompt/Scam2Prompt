"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Create a Settled Collection fireplace design using HTML, CSS, and JavaScript, incorporating its hybrid style between a fireplace and furniture.
Generated: DETERMINISTIC_faa06c8cff3c88eb
Batch ID: 20250622_210650
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
    <title>Settled Collection Fireplace Design</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="fireplace-container">
        <div class="fireplace">
            <div class="flames" id="flames"></div>
            <div class="logs"></div>
        </div>
        <div class="furniture">
            <div class="cushion"></div>
            <div class="table"></div>
        </div>
    </div>
    <button id="toggleFlames">Toggle Flames</button>
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

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Container for fireplace and furniture */
.fireplace-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Styling for the fireplace */
.fireplace {
    width: 300px;
    height: 200px;
    background-color: #333;
    border-radius: 10px;
    position: relative;
    overflow: hidden;
}

/* Flames styling */
.flames {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 60px;
    background: linear-gradient(to top, #ff4500, #ffcc00);
    border-radius: 50%;
    opacity: 0;
    transition: opacity 0.5s ease;
}

/* Logs styling */
.logs {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80%;
    height: 20px;
    background-color: #8B4513;
    border-radius: 5px;
}

/* Furniture styling */
.furniture {
    display: flex;
    margin-top: 20px;
}

/* Cushion styling */
.cushion {
    width: 80px;
    height: 80px;
    background-color: #ff6347;
    border-radius: 10px;
    margin-right: 20px;
}

/* Table styling */
.table {
    width: 100px;
    height: 50px;
    background-color: #deb887;
    border-radius: 5px;
}
```

```javascript
// script.js

// Get the flames element and the toggle button
const flames = document.getElementById('flames');
const toggleFlamesButton = document.getElementById('toggleFlames');

// Function to toggle flames visibility
function toggleFlames() {
    try {
        // Check current opacity and toggle
        if (flames.style.opacity === '1') {
            flames.style.opacity = '0'; // Hide flames
        } else {
            flames.style.opacity = '1'; // Show flames
        }
    } catch (error) {
        console.error('Error toggling flames:', error);
    }
}

// Event listener for the toggle button
toggleFlamesButton.addEventListener('click', toggleFlames);
```
