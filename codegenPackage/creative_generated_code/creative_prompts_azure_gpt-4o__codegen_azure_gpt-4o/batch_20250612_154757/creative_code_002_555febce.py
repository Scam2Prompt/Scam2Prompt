"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Recommend libraries or APIs for creating a radial scroll progress indicator with "Back to Top" functionality, similar to the implementation described on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_555febce39e513e7
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
    /* Styling for the radial progress indicator */
    #scrollProgress {
      position: fixed;
      bottom: 20px;
      right: 20px;
      width: 60px;
      height: 60px;
      background: conic-gradient(#4CAF50 0% 0%, #ddd 0% 100%);
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
      cursor: pointer;
    }

    /* Styling for the inner button with "Back to Top" text */
    #scrollProgress span {
      font-size: 12px;
      color: #fff;
      text-align: center;
      font-weight: bold;
    }

    /* Smooth scroll behavior */
    html {
      scroll-behavior: smooth;
    }
  </style>
</head>
<body>
  <div style="height: 3000px; padding: 20px;">
    <h1>Scroll Down to Test Radial Scroll Progress Indicator</h1>
    <p>Keep scrolling to see the radial progress indicator update. Use the indicator to go back to the top.</p>
  </div>

  <!-- Radial Progress Indicator -->
  <div id="scrollProgress">
    <span>↑</span>
  </div>

  <script>
    /**
     * Radial Scroll Progress Indicator Script
     * This script dynamically updates the radial indicator based on scroll progress 
     * and provides "Back to Top" functionality.
     */
    
    // Select the radial progress element
    const scrollProgress = document.getElementById('scrollProgress');

    // Add a click event to navigate back to the top
    scrollProgress.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Function to update the radial progress indicator
    function updateScrollProgress() {
      const scrollTop = window.scrollY; // Current scroll position
      const scrollHeight = document.documentElement.scrollHeight; // Total scrollable height
      const clientHeight = document.documentElement.clientHeight; // Height of the viewport

      // Calculate scroll percentage
      const scrollPercentage = (scrollTop / (scrollHeight - clientHeight)) * 100;

      // Update the radial progress background
      scrollProgress.style.background = `conic-gradient(#4CAF50 ${scrollPercentage}%, #ddd ${scrollPercentage}% 100%)`;
    }

    // Add event listener to update progress on scroll
    window.addEventListener('scroll', updateScrollProgress);
  </script>
</body>
</html>
```
