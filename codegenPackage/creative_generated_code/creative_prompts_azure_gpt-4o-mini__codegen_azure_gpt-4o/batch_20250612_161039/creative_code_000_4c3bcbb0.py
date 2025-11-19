"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laguarda.com.ec
Prompt: How can I implement a responsive fullscreen video feature on a webpage using HTML and CSS?
Generated: DETERMINISTIC_4c3bcbb0ad3d5442
Batch ID: 20250612_161039
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
  <title>Responsive Fullscreen Video</title>
  <style>
    /* Reset margin and padding for the body */
    body {
      margin: 0;
      padding: 0;
    }

    /* Container to hold the video */
    .video-container {
      position: relative; /* Ensures child elements can be positioned absolutely */
      width: 100vw; /* Full width of the viewport */
      height: 100vh; /* Full height of the viewport */
      overflow: hidden; /* Prevents overflow of video outside the container */
    }

    /* Styling for the video element */
    video {
      position: absolute; /* Allows us to position the video precisely */
      top: 50%; /* Center vertically */
      left: 50%; /* Center horizontally */
      transform: translate(-50%, -50%); /* Perfect centering */
      width: 100%; /* Ensures the video spans the full container width */
      height: auto; /* Maintains the aspect ratio */
    }

    /* Fallback for maintaining aspect ratio in smaller viewport dimensions */
    @media (max-aspect-ratio: 16/9) {
      video {
        height: 100%;
        width: auto;
      }
    }
  </style>
</head>
<body>
  <!-- Fullscreen Video Container -->
  <div class="video-container">
    <!-- Video element -->
    <video autoplay muted loop>
      <!-- Video source with format fallback -->
      <source src="video.mp4" type="video/mp4">
      <source src="video.webm" type="video/webm">
      <!-- Fallback message -->
      Your browser does not support the video tag.
    </video>
  </div>
</body>
</html>
```
