"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laguarda.com.ec
Prompt: Can you provide a code snippet for creating a fullscreen video background that adjusts to various screen sizes?
Generated: DETERMINISTIC_c738e0fcbdbff5fe
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
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Fullscreen Video Background</title>
  <style>
    /* Ensure body has no margins and fills the viewport */
    body {
      margin: 0;
      overflow: hidden; /* Prevent scrolling */
    }

    /* Fullscreen video styling */
    .video-background {
      position: fixed; /* Ensures video stays in place */
      top: 0;
      left: 0;
      width: 100%; /* Stretches to fit width */
      height: 100%; /* Stretches to fit height */
      object-fit: cover; /* Ensures video covers whole screen */
      z-index: -1; /* Places video behind other content */
    }

    /* Example overlay for adding content on top of the video */
    .content-overlay {
      position: relative; /* Ensures content stays above video */
      color: white; /* Text color for visibility */
      text-align: center; /* Centers content */
      font-family: Arial, sans-serif;
      font-size: 1.5em;
      padding: 20px;
    }
  </style>
</head>
<body>
  <!-- Fullscreen video element -->
  <video class="video-background" autoplay muted loop>
    <source src="video.mp4" type="video/mp4">
    <!-- Fallback message for unsupported browsers -->
    Your browser does not support the video tag.
  </video>

  <!-- Overlay content -->
  <div class="content-overlay">
    <h1>Welcome to My Website</h1>
    <p>Enjoy the immersive experience!</p>
  </div>

  <script>
    // Basic error handling for video loading
    document.querySelector('.video-background').addEventListener('error', (event) => {
      console.error('Error loading video:', event);
      alert('Failed to load the background video.');
    });
  </script>
</body>
</html>
```
