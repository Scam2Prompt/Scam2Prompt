"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneymintpinnacles.firebaseapp.com
Prompt: Generate a script to validate browser support for HTML5 video formats (mp4 and webm) and provide fallback options, inspired by the Disney Pinnacle webpage.
Generated: DETERMINISTIC_0ef8faf7e080edd3
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML5 Video Format Validator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 20px;
    }
    .fallback-message {
      color: #d9534f;
      font-weight: bold;
    }
    video {
      max-width: 100%;
      height: auto;
    }
  </style>
</head>
<body>
  <h1>HTML5 Video Format Validator</h1>
  
  <!-- JavaScript will dynamically populate this section -->
  <div id="video-container"></div>

  <script>
    // Function to check browser support for a specific video format
    function isFormatSupported(format) {
      const videoElement = document.createElement('video');
      return videoElement.canPlayType && videoElement.canPlayType(format).length > 0;
    }

    // Main function to validate video formats and provide fallback
    function validateVideoSupport() {
      const container = document.getElementById('video-container');
      container.innerHTML = ''; // Clear previous content

      // Define formats to check
      const formats = [
        { type: 'video/mp4', src: 'example.mp4' }, // Replace 'example.mp4' with actual video file path
        { type: 'video/webm', src: 'example.webm' } // Replace 'example.webm' with actual video file path
      ];

      let supported = false;

      // Iterate through formats
      formats.forEach(format => {
        if (isFormatSupported(format.type)) {
          const videoElement = document.createElement('video');
          videoElement.controls = true; // Enable video controls
          videoElement.src = format.src;
          container.appendChild(videoElement);
          supported = true;
        }
      });

      // Fallback message if no formats are supported
      if (!supported) {
        const fallbackMessage = document.createElement('p');
        fallbackMessage.classList.add('fallback-message');
        fallbackMessage.textContent = 'Your browser does not support HTML5 video formats (MP4 or WebM). Please update your browser or try viewing this content on another device.';
        container.appendChild(fallbackMessage);
      }
    }

    // Execute validation on page load
    window.onload = validateVideoSupport;
  </script>
</body>
</html>
```
