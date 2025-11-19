"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Design a Webflow scroll progress indicator that displays 100% completion with an SVG and a "Back to Top" button.
Generated: DETERMINISTIC_135f954b802c8dd7
Batch ID: 20250622_212208
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
  <title>Scroll Progress Indicator</title>
  <style>
    /* Style for the progress indicator */
    #progress-container {
      position: fixed;
      top: 10px;
      right: 10px;
      width: 50px;
      height: 50px;
    }

    svg {
      transform: rotate(-90deg); /* Rotate to start from the top */
    }

    circle {
      fill: none;
      stroke-width: 5;
    }

    .progress-bg {
      stroke: #e0e0e0; /* Background circle color */
    }

    .progress {
      stroke: #007bff; /* Progress circle color */
      stroke-linecap: round;
      stroke-dasharray: 157; /* Circumference of the circle */
      stroke-dashoffset: 157; /* Start with no progress */
      transition: stroke-dashoffset 0.2s ease-out;
    }

    /* Style for the "Back to Top" button */
    #back-to-top {
      position: fixed;
      bottom: 20px;
      right: 20px;
      padding: 10px 15px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      display: none; /* Initially hidden */
      font-size: 14px;
    }

    #back-to-top:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <!-- Scroll Progress Indicator -->
  <div id="progress-container">
    <svg width="50" height="50" viewBox="0 0 50 50">
      <!-- Background circle -->
      <circle class="progress-bg" cx="25" cy="25" r="25"></circle>
      <!-- Progress circle -->
      <circle class="progress" cx="25" cy="25" r="25"></circle>
    </svg>
  </div>

  <!-- Back to Top Button -->
  <button id="back-to-top">Back to Top</button>

  <!-- Content to scroll -->
  <div style="height: 2000px; padding: 20px;">
    <h1>Scroll Down</h1>
    <p>Scroll to see the progress indicator and the "Back to Top" button.</p>
  </div>

  <script>
    // Select elements
    const progressCircle = document.querySelector('.progress');
    const backToTopButton = document.getElementById('back-to-top');
    const circleRadius = progressCircle.r.baseVal.value;
    const circleCircumference = 2 * Math.PI * circleRadius;

    // Set the stroke-dasharray to the circumference of the circle
    progressCircle.style.strokeDasharray = circleCircumference;

    // Function to update the scroll progress
    function updateScrollProgress() {
      const scrollTop = window.scrollY; // Current scroll position
      const scrollHeight = document.documentElement.scrollHeight; // Total scrollable height
      const clientHeight = document.documentElement.clientHeight; // Viewport height
      const scrollPercentage = scrollTop / (scrollHeight - clientHeight); // Scroll percentage

      // Update the stroke-dashoffset based on scroll percentage
      const offset = circleCircumference * (1 - scrollPercentage);
      progressCircle.style.strokeDashoffset = offset;

      // Show or hide the "Back to Top" button
      backToTopButton.style.display = scrollTop > 100 ? 'block' : 'none';
    }

    // Function to scroll back to the top
    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Attach event listeners
    window.addEventListener('scroll', updateScrollProgress);
    backToTopButton.addEventListener('click', scrollToTop);

    // Initialize the scroll progress on page load
    updateScrollProgress();
  </script>
</body>
</html>
```
