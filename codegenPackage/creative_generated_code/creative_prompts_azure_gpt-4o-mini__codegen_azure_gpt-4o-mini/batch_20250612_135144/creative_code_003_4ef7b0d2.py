"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Create a web application that simulates the ergonomic classroom environment described by Atria, focusing on adjustable seating and optimal lighting for studying.
Generated: DETERMINISTIC_4ef7b0d276294486
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a simple web application that simulates an ergonomic classroom environment focusing on adjustable seating and optimal lighting for studying. This example uses HTML, CSS, and JavaScript.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ergonomic Classroom Simulator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Ergonomic Classroom Simulator</h1>
        
        <div class="settings">
            <label for="seat-height">Adjust Seat Height (inches): </label>
            <input type="range" id="seat-height" min="10" max="30" value="20">
            <span id="seat-height-value">20</span> inches
        </div>
        
        <div class="lighting">
            <label for="light-intensity">Set Light Intensity (%): </label>
            <input type="range" id="light-intensity" min="0" max="100" value="75">
            <span id="light-intensity-value">75</span>%
        </div>
        
        <div class="classroom-preview">
            <div id="classroom" class="classroom"></div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

.settings, .lighting {
    margin: 15px 0;
}

.classroom {
    width: 100%;
    height: 200px;
    background-color: #e2e2e2;
    border: 2px solid #ccc;
    border-radius: 4px;
    position: relative;
}

.adjusted-seat {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 50px;
    height: var(--seat-height);
    background-color: #4CAF50;
    transition: height 0.3s ease;
}

.light-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(255, 255, 255, 0.75);
    transition: opacity 0.3s ease;
}
```

```javascript
// script.js

// Get DOM elements
const seatHeightInput = document.getElementById('seat-height');
const seatHeightValue = document.getElementById('seat-height-value');
const lightIntensityInput = document.getElementById('light-intensity');
const lightIntensityValue = document.getElementById('light-intensity-value');
const classroomDiv = document.getElementById('classroom');

// Function to update seat height
function updateSeatHeight() {
    const height = seatHeightInput.value;
    seatHeightValue.textContent = height; // Update displayed value
    classroomDiv.style.setProperty('--seat-height', `${height}px`); // Update CSS variable
    const adjustedSeat = document.querySelector('.adjusted-seat');
    if (adjustedSeat) {
        adjustedSeat.style.height = `${height}px`; // Set height of the seat
    } else {
        const newSeat = document.createElement('div');
        newSeat.classList.add('adjusted-seat');
        newSeat.style.height = `${height}px`;
        classroomDiv.appendChild(newSeat);
    }
}

// Function to update light intensity
function updateLightIntensity() {
    const intensity = lightIntensityInput.value;
    lightIntensityValue.textContent = intensity; // Update displayed value
    const lightOverlay = document.querySelector('.light-overlay');

    // Create overlay if not exists
    if (!lightOverlay) {
        const newOverlay = document.createElement('div');
        newOverlay.classList.add('light-overlay');
        classroomDiv.appendChild(newOverlay);
    }

    // Update opacity based on intensity
    classroomDiv.querySelector('.light-overlay').style.opacity = (100 - intensity) / 100;
}

// Event listeners for input changes
seatHeightInput.addEventListener('input', updateSeatHeight);
lightIntensityInput.addEventListener('input', updateLightIntensity);

// Initial setup
updateSeatHeight(); // Set initial seat height
updateLightIntensity(); // Set initial light intensity
```

This code provides a simple user interface for adjusting seat height and light intensity in a classroom setting. The code handles user input with event listeners and updates the styles dynamically.
