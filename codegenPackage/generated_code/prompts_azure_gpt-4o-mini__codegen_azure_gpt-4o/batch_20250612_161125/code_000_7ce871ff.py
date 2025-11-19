"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: How can I implement a radial scroll progress indicator in Webflow using SVG?
Generated: DETERMINISTIC_7ce871ff346ef9ee
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Radial Scroll Progress Indicator</title>
  <style>
    /* Center the SVG and make it responsive */
    .progress-container {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 150px;
      height: 150px;
    }

    svg {
      width: 100%;
      height: 100%;
    }

    /* Style for the progress text */
    .progress-text {
      font-family: Arial, sans-serif;
      font-size: 1.5rem;
      text-anchor: middle;
      dominant-baseline: middle;
      fill: #333;
    }
  </style>
</head>
<body>
  <!-- Radial Progress Indicator -->
  <div class="progress-container">
    <svg viewBox="0 0 100 100">
      <!-- Background circle -->
      <circle cx="50" cy="50" r="45" stroke="#e6e6e6" stroke-width="5" fill="none" />
      <!-- Progress circle -->
      <circle
        cx="50"
        cy="50"
        r="45"
        stroke="#4caf50"
        stroke-width="5"
        fill="none"
        stroke-dasharray="282.743" <!-- Circumference of the circle -->
        stroke-dashoffset="282.743" <!-- Initially hidden -->
        stroke-linecap="round"
        class="progress-circle"
      />
      <!-- Progress percentage text -->
      <text x="50" y="50" class="progress-text">0%</text>
    </svg>
  </div>

  <script>
    // Select the progress circle and text elements
    const progressCircle = document.querySelector('.progress-circle');
    const progressText = document.querySelector('.progress-text');

    // Total circumference of the circle
    const circumference = 2 * Math.PI * 45;

    // Update the progress indicator based on scroll position
    function updateProgress() {
      // Calculate the scroll percentage
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrollPercent = (scrollTop / docHeight) * 100;

      // Calculate the stroke-dashoffset based on scroll percentage
      const offset = circumference - (scrollPercent / 100) * circumference;

      // Update the circle's stroke-dashoffset
      progressCircle.style.strokeDashoffset = offset;

      // Update the progress text
      progressText.textContent = `${Math.round(scrollPercent)}%`;
    }

    // Initialize the circle's stroke-dasharray
    progressCircle.style.strokeDasharray = circumference;

    // Add scroll event listener
    window.addEventListener('scroll', updateProgress);
  </script>
</body>
</html>
```
