"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: How can I implement a no-jank scroll progress indicator in Webflow using SVG, as described on the Scroll Progress Indicator webpage?
Generated: DETERMINISTIC_1529ffff44d79ecf
Batch ID: 20250612_154757
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Scroll Progress Indicator</title>
  <style>
    /* Styles for the scroll progress indicator */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
    }

    .content {
      height: 200vh; /* Simulate long content */
    }

    .scroll-indicator {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 10px;
      z-index: 9999;
    }

    svg {
      width: 100%;
      height: 100%;
    }

    path {
      stroke: #3498db; /* Progress color */
      stroke-width: 10;
      fill: none;
      stroke-linecap: round;
    }
  </style>
</head>
<body>

  <!-- Scroll progress SVG indicator -->
  <div class="scroll-indicator">
    <svg viewBox="0 0 100 10" xmlns="http://www.w3.org/2000/svg">
      <path id="progress-bar" d="M0 5 L100 5"></path>
    </svg>
  </div>

  <!-- Long content to enable scrolling -->
  <div class="content">
    <h1>Scroll to see the progress indicator</h1>
    <p>Scroll down to test the scroll progress indicator functionality.</p>
  </div>

  <script>
    // Function to update the scroll progress indicator
    (function() {
      const progressBar = document.getElementById('progress-bar');

      // Listen to scroll events
      window.addEventListener('scroll', () => {
        // Calculate the scroll percentage
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrollPercentage = (scrollTop / scrollHeight) * 100;

        // Update the width of the progress bar dynamically
        progressBar.setAttribute('stroke-dasharray', `${scrollPercentage}, 100`);
      });

      // Initialize the progress bar to avoid jank
      progressBar.setAttribute('stroke-dasharray', '0, 100');
    })();
  </script>

</body>
</html>
```
