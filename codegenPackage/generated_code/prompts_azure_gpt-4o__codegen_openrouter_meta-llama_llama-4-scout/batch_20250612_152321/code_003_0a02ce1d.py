"""
Generated Code Metadata:
========================
Original URL: https://laguarda.com.ec
Prompt: Provide a solution to detect browser support for video playback and display an alternative message using JavaScript, as referenced on laguarda.com.ec.
Generated: DETERMINISTIC_0a02ce1d36aa733e
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// video-support-detector.js

/**
 * Detects browser support for video playback and displays an alternative message if not supported.
 */

// Function to check video support
function checkVideoSupport() {
  // Check if the browser has support for the HTML5 video tag
  const videoElement = document.createElement('video');
  const isVideoSupported = !!videoElement.canPlayType;

  // Check if the browser supports MP4 video playback
  const isMp4Supported = !!videoElement.canPlayType('video/mp4');

  return {
    isVideoSupported,
    isMp4Supported,
  };
}

// Function to display alternative message
function displayAlternativeMessage() {
  const alternativeMessageElement = document.getElementById('alternative-message');
  alternativeMessageElement.style.display = 'block';
}

// Function to initialize video support detection
function initVideoSupportDetection() {
  try {
    const videoSupport = checkVideoSupport();

    if (!videoSupport.isVideoSupported || !videoSupport.isMp4Supported) {
      displayAlternativeMessage();
    }
  } catch (error) {
    console.error('Error detecting video support:', error);
    displayAlternativeMessage();
  }
}

// Initialize video support detection on page load
document.addEventListener('DOMContentLoaded', initVideoSupportDetection);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Video Support Detector</title>
  <style>
    #alternative-message {
      display: none;
      color: red;
    }
  </style>
</head>
<body>
  <h1>Video Support Detector</h1>
  <video id="video-player" width="640" height="480" controls>
    <source src="example.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p id="alternative-message">
    Your browser does not support video playback. Please use a different browser.
  </p>

  <script src="video-support-detector.js"></script>
</body>
</html>
```
