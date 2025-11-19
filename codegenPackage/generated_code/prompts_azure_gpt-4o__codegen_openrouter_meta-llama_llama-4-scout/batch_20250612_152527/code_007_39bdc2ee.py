"""
Generated Code Metadata:
========================
Original URL: https://popcat.meme
Prompt: Write JavaScript code to implement a "POPCAT never stops popping" animation that loops indefinitely on a webpage.
Generated: DETERMINISTIC_39bdc2ee6fc47164
Batch ID: 20250612_152527
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/popcat_2.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/popcat_1.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// popcat.js

/**
 * POPCAT never stops popping animation implementation.
 */

// Get the popcat image element
const popcatImage = document.getElementById('popcat');

// Define the popcat animation frames
const popcatFrames = [
  'https://example.com/popcat_1.png', // replace with actual image URLs
  'https://example.com/popcat_2.png', // replace with actual image URLs
];

// Define the animation duration (in milliseconds)
const animationDuration = 100;

// Initialize the current frame index
let currentFrameIndex = 0;

// Initialize the last frame timestamp
let lastFrameTimestamp = 0;

// Function to animate the popcat
function animatePopcat(timestamp) {
  // Check if the animation duration has passed since the last frame
  if (timestamp - lastFrameTimestamp >= animationDuration) {
    // Update the last frame timestamp
    lastFrameTimestamp = timestamp;

    // Update the current frame index
    currentFrameIndex = (currentFrameIndex + 1) % popcatFrames.length;

    // Update the popcat image source
    popcatImage.src = popcatFrames[currentFrameIndex];
  }

  // Request the next animation frame
  requestAnimationFrame(animatePopcat);
}

// Add event listener to handle errors
popcatImage.addEventListener('error', () => {
  console.error('Error loading popcat image');
});

// Start the animation
if (popcatImage) {
  popcatImage.src = popcatFrames[0];
  requestAnimationFrame(animatePopcat);
} else {
  console.error('Popcat image element not found');
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>POPCAT never stops popping</title>
  <style>
    /* Add some basic styling to center the popcat image */
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    #popcat {
      width: 200px; /* adjust the width to match your image */
      height: 200px; /* adjust the height to match your image */
    }
  </style>
</head>
<body>
  <img id="popcat" alt="POPCAT">
  <script src="popcat.js"></script>
</body>
</html>
```
