"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Create a Webflow-compatible scroll progress indicator that uses SVG and includes a "Back to Top" button, as detailed on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_44581a85514e841d
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
  <title>Scroll Progress Indicator</title>
  <style>
    /* Basic styling for the progress indicator */
    #scroll-progress-container {
      position: fixed;
      top: 10px;
      right: 10px;
      z-index: 1000;
    }

    svg {
      width: 60px;
      height: 60px;
      overflow: visible;
    }

    circle {
      fill: none;
      stroke-width: 6;
      transform: rotate(-90deg);
      transform-origin: center;
    }

    .circle-bg {
      stroke: #e0e0e0;
    }

    .circle-progress {
      stroke: #0077ff;
      stroke-linecap: round;
      stroke-dasharray: 283; /* Circumference of a circle with radius 45px */
      stroke-dashoffset: 283; /* Start fully "hidden" */
      transition: stroke-dashoffset 0.1s ease-out;
    }

    /* Styling for the "Back to Top" button */
    #back-to-top {
      position: fixed;
      bottom: 20px;
      right: 20px;
      padding: 10px 15px;
      background-color: #0077ff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 14px;
      display: none; /* Initially hidden */
    }

    #back-to-top:hover {
      background-color: #005bb5;
    }
  </style>
</head>
<body>
  <div id="scroll-progress-container">
    <!-- SVG Scroll Progress Indicator -->
    <svg viewBox="0 0 100 100">
      <circle class="circle-bg" cx="50" cy="50" r="45"></circle>
      <circle class="circle-progress" cx="50" cy="50" r="45"></circle>
    </svg>
  </div>
  
  <button id="back-to-top">Back to Top</button>

  <script>
    // Cache DOM elements
    const progressCircle = document.querySelector('.circle-progress');
    const backToTopButton = document.getElementById('back-to-top');

    // Constants
    const circleRadius = 45; // Matches the radius defined in SVG
    const circumference = 2 * Math.PI * circleRadius;

    // Ensure stroke-dasharray matches circumference for proper animations
    progressCircle.style.strokeDasharray = circumference;

    // Function to update scroll progress
    function updateScrollProgress() {
      const scrollTop = window.scrollY; // Current vertical scroll position
      const docHeight = document.documentElement.scrollHeight - window.innerHeight; // Total scrollable height
      const scrollFraction = scrollTop / docHeight; // Fraction of total scroll completed
      const offset = circumference * (1 - scrollFraction); // Calculate stroke-dashoffset

      // Update the stroke-dashoffset to reflect scroll progress
      progressCircle.style.strokeDashoffset = offset;

      // Show or hide the "Back to Top" button based on scroll position
      if (scrollTop > 100) {
        backToTopButton.style.display = 'block';
      } else {
        backToTopButton.style.display = 'none';
      }
    }

    // Function to scroll back to the top of the page
    function scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth', // Smooth scrolling for better UX
      });
    }

    // Attach event listeners
    window.addEventListener('scroll', updateScrollProgress);
    backToTopButton.addEventListener('click', scrollToTop);

    // Initial update to set progress indicator and button visibility correctly
    updateScrollProgress();
  </script>
</body>
</html>
```
