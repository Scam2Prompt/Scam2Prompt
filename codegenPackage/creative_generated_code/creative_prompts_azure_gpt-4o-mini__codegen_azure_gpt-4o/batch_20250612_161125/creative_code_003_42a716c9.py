"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Provide an example of a 100% scroll progress indicator using SVG in a Webflow project.
Generated: DETERMINISTIC_42a716c95cf3b3d7
Batch ID: 20250612_161125
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
  <title>Scroll Progress Indicator</title>
  <style>
    /* Basic styling for full-page content */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      height: 200vh; /* Makes the page scrollable */
    }
    .scroll-indicator-container {
      position: fixed;
      top: 10px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 1000;
      width: 150px;
      height: 150px;
    }
    svg {
      display: block;
    }
    .progress-ring__circle {
      fill: none;
      stroke: #4caf50; /* Progress indicator color */
      stroke-width: 10;
      stroke-linecap: round;
      transition: stroke-dashoffset 0.2s ease-out;
    }
    .progress-ring__background {
      fill: none;
      stroke: #e0e0e0; /* Background color */
      stroke-width: 10;
    }
  </style>
</head>
<body>
  <!-- Scroll Indicator SVG -->
  <div class="scroll-indicator-container">
    <svg width="150" height="150">
      <!-- Background Circle -->
      <circle
        class="progress-ring__background"
        cx="75"
        cy="75"
        r="65"
      ></circle>
      <!-- Progress Circle -->
      <circle
        class="progress-ring__circle"
        cx="75"
        cy="75"
        r="65"
        stroke-dasharray="408.4" /* Circumference of the circle */
        stroke-dashoffset="408.4" /* Initially hides the progress */
      ></circle>
    </svg>
  </div>

  <script>
    // JavaScript to handle scroll progress logic
    (function () {
      // Select the progress circle element
      const progressCircle = document.querySelector('.progress-ring__circle');
      const circleRadius = progressCircle.r.baseVal.value;
      const circleCircumference = 2 * Math.PI * circleRadius;

      // Set initial stroke-dasharray and stroke-dashoffset
      progressCircle.style.strokeDasharray = circleCircumference;

      const updateProgress = () => {
        const scrollTop = window.scrollY; // Amount of scroll from the top
        const scrollHeight = document.documentElement.scrollHeight; // Full scrollable height
        const clientHeight = document.documentElement.clientHeight; // Viewport height

        // Calculate scroll progress as a percentage
        const scrollPercentage = scrollTop / (scrollHeight - clientHeight);
        const offset = circleCircumference * (1 - scrollPercentage);

        // Update the stroke-dashoffset to indicate progress
        progressCircle.style.strokeDashoffset = offset;
      };

      // Attach scroll event listener to update progress
      window.addEventListener('scroll', updateProgress);

      // Initialize on page load
      updateProgress();
    })();
  </script>
</body>
</html>
```
