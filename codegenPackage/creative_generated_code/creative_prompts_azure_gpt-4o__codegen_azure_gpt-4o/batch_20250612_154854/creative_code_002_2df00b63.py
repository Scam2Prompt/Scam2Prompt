"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://localcamflings.com
Prompt: Write JavaScript code to initialize a webcam video stream using the `getUserMedia` API and display the video feed on a webpage.
Generated: DETERMINISTIC_2df00b6376a7f9d9
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure the DOM is fully loaded before executing the script
document.addEventListener("DOMContentLoaded", () => {
  // Select the video element from the DOM
  const videoElement = document.getElementById("webcamFeed");

  // Check if the browser supports the getUserMedia API
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    console.error("getUserMedia API is not supported by your browser.");
    alert("Your browser does not support accessing the webcam.");
    return;
  }

  // Constraints for the webcam video stream
  const constraints = {
    video: true,
    audio: false, // Disabling audio for this example
  };

  // Request access to the webcam video stream
  navigator.mediaDevices
    .getUserMedia(constraints)
    .then((stream) => {
      // Set the video element's source to the webcam stream
      videoElement.srcObject = stream;

      // Play the video feed
      videoElement.play().catch((error) => {
        console.error("Error playing the video feed:", error);
      });
    })
    .catch((error) => {
      // Handle errors during webcam access
      console.error("Error accessing webcam:", error);
      alert("Unable to access the webcam. Please ensure permissions are granted.");
    });
});
```

```html
<!-- Include this HTML alongside the JavaScript code above -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Webcam Video Stream</title>
</head>
<body>
  <!-- Video element to display the webcam feed -->
  <video id="webcamFeed" autoplay muted playsinline style="width: 100%; max-width: 600px; border: 1px solid #ccc;"></video>
  
  <!-- Include the JavaScript file -->
  <script src="webcam.js"></script>
</body>
</html>
```
