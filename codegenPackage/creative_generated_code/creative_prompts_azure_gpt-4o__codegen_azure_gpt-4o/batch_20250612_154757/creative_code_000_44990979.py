"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write code to implement a radial scroll progress indicator in Webflow, ensuring smooth performance without jank, as described on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_4499097973a49bb2
Batch ID: 20250612_154757
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
  <title>Radial Scroll Progress Indicator</title>
  <style>
    /* Styles for the radial progress indicator */
    .progress-container {
      position: fixed;
      top: 10px;
      right: 10px;
      width: 50px;
      height: 50px;
      z-index: 9999;
    }

    .progress-ring {
      position: relative;
      width: 100%;
      height: 100%;
      transform: rotate(-90deg); /* Rotate to start at the top */
    }

    .progress-circle {
      fill: none;
      stroke: #ddd; /* Background circle */
      stroke-width: 6;
    }

    .progress-circle-fill {
      fill: none;
      stroke: #0077ff; /* Progress color */
      stroke-width: 6;
      stroke-linecap: round; /* Rounded edges */
      stroke-dasharray: 0 100; /* Dynamic progress */
      transition: stroke-dasharray 0.2s ease-out; /* Smooth animation */
    }
  </style>
</head>
<body>
  <!-- Progress indicator container -->
  <div class="progress-container">
    <svg class="progress-ring" viewBox="0 0 50 50">
      <!-- Background circle -->
      <circle class="progress-circle" cx="25" cy="25" r="22"></circle>
      <!-- Fill circle -->
      <circle class="progress-circle-fill" cx="25" cy="25" r="22"></circle>
    </svg>
  </div>

  <script>
    // Radial Progress Indicator Script

    // Cache DOM elements for better performance
    const progressFill = document.querySelector('.progress-circle-fill');
    const radius = progressFill.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;

    // Set the maximum circumference for the stroke-dasharray
    progressFill.style.strokeDasharray = `${circumference} ${circumference}`;
    progressFill.style.strokeDashoffset = circumference;

    // Function to calculate and update progress
    const updateProgress = () => {
      // Calculate scroll progress
      const scrollTop = window.scrollY; // Current scroll position
      const documentHeight = document.documentElement.scrollHeight; // Total height of the document
      const viewportHeight = window.innerHeight; // Height of the viewport
      const scrollableHeight = documentHeight - viewportHeight; // Scrollable height

      // Prevent division by zero
      if (scrollableHeight <= 0) {
        return;
      }

      // Calculate scroll progress percentage
      const progress = scrollTop / scrollableHeight;

      // Update stroke-dashoffset based on progress
      const offset = circumference * (1 - progress); // Invert progress
      progressFill.style.strokeDashoffset = offset;
    };

    // Event listener for scroll updates
    window.addEventListener('scroll', updateProgress);

    // Initial progress update
    updateProgress();
  </script>
</body>
</html>
```
