"""
Generated Code Metadata:
========================
Original URL: https://www.ozonator.si
Prompt: Design a simple user interface using HTML/CSS and JavaScript for a mobile application that allows users to monitor and control ozone generators remotely, considering the features and safety precautions highlighted on this website.
Generated: DETERMINISTIC_6e0263137cd937de
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ozone Generator Control</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Ozone Generator Control</h1>
    </header>
    <main>
        <section class="device-status">
            <h2>Device Status</h2>
            <p id="device-status-text">Disconnected</p>
            <button id="connect-button">Connect</button>
        </section>
        <section class="ozone-level">
            <h2>Ozone Level</h2>
            <p id="ozone-level-text">0 ppm</p>
            <input id="ozone-level-slider" type="range" min="0" max="1000" value="0">
            <label for="ozone-level-slider">Ozone Level (ppm): <span id="ozone-level-slider-value">0</span></label>
        </section>
        <section class="safety-features">
            <h2>Safety Features</h2>
            <label>
                <input id="auto-shutoff-checkbox" type="checkbox">
                Auto Shutoff
            </label>
            <label>
                <input id="alert-threshold-checkbox" type="checkbox">
                Alert Threshold
            </label>
            <input id="alert-threshold-input" type="number" min="0" max="1000" value="500">
            <label for="alert-threshold-input">Alert Threshold (ppm): <span id="alert-threshold-input-value">500</span></label>
        </section>
        <section class="controls">
            <button id="start-button" disabled>Start</button>
            <button id="stop-button" disabled>Stop</button>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

label {
    display: block;
    margin-bottom: 0.5em;
}

input[type="range"] {
    width: 100%;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 0.5em 1em;
    font-size: 1em;
    cursor: pointer;
}

button:disabled {
    background-color: #666;
    cursor: not-allowed;
}
```

**script.js**
```javascript
// Get HTML elements
const deviceStatusText = document.getElementById('device-status-text');
const connectButton = document.getElementById('connect-button');
const ozoneLevelText = document.getElementById('ozone-level-text');
const ozoneLevelSlider = document.getElementById('ozone-level-slider');
const ozoneLevelSliderValue = document.getElementById('ozone-level-slider-value');
const autoShutoffCheckbox = document.getElementById('auto-shutoff-checkbox');
const alertThresholdCheckbox = document.getElementById('alert-threshold-checkbox');
const alertThresholdInput = document.getElementById('alert-threshold-input');
const alertThresholdInputValue = document.getElementById('alert-threshold-input-value');
const startButton = document.getElementById('start-button');
const stopButton = document.getElementById('stop-button');

// Initialize device status and ozone level
let deviceConnected = false;
let ozoneLevel = 0;

// Connect button click event handler
connectButton.addEventListener('click', () => {
    // Simulate device connection (replace with actual connection logic)
    deviceConnected = true;
    deviceStatusText.textContent = 'Connected';
    connectButton.disabled = true;
    startButton.disabled = false;
    stopButton.disabled = false;
});

// Ozone level slider change event handler
ozoneLevelSlider.addEventListener('input', (e) => {
    ozoneLevel = parseInt(e.target.value);
    ozoneLevelText.textContent = `${ozoneLevel} ppm`;
    ozoneLevelSliderValue.textContent = ozoneLevel;
});

// Auto shutoff checkbox change event handler
autoShutoffCheckbox.addEventListener('change', (e) => {
    if (e.target.checked) {
        console.log('Auto shutoff enabled');
    } else {
        console.log('Auto shutoff disabled');
    }
});

// Alert threshold checkbox change event handler
alertThresholdCheckbox.addEventListener('change', (e) => {
    if (e.target.checked) {
        alertThresholdInput.disabled = false;
        console.log('Alert threshold enabled');
    } else {
        alertThresholdInput.disabled = true;
        console.log('Alert threshold disabled');
    }
});

// Alert threshold input change event handler
alertThresholdInput.addEventListener('input', (e) => {
    alertThresholdInputValue.textContent = e.target.value;
});

// Start button click event handler
startButton.addEventListener('click', () => {
    if (deviceConnected) {
        // Simulate ozone generator start (replace with actual start logic)
        console.log('Ozone generator started');
    } else {
        console.error('Device not connected');
    }
});

// Stop button click event handler
stopButton.addEventListener('click', () => {
    if (deviceConnected) {
        // Simulate ozone generator stop (replace with actual stop logic)
        console.log('Ozone generator stopped');
    } else {
        console.error('Device not connected');
    }
});

// Error handling
try {
    // Simulate device connection errors (replace with actual error handling)
    // ...
} catch (error) {
    console.error('Error:', error);
}
```
