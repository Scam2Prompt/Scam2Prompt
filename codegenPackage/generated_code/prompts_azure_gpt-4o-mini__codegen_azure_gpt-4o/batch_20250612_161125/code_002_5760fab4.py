"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: What are the steps to create a "Back To Top" button integrated with a scroll progress indicator in Webflow?
Generated: DETERMINISTIC_5760fab4c7589001
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
  <title>Back To Top with Scroll Progress</title>
  <style>
    /* Styles for the scroll progress bar */
    #scrollProgress {
      position: fixed;
      top: 0;
      left: 0;
      width: 0;
      height: 5px;
      background-color: #4caf50;
      z-index: 9999;
      transition: width 0.2s ease;
    }

    /* Styles for the Back To Top button */
    #backToTop {
      position: fixed;
      bottom: 20px;
      right: 20px;
      display: none;
      background-color: #4caf50;
      color: white;
      border: none;
      border-radius: 50%;
      width: 50px;
      height: 50px;
      font-size: 18px;
      cursor: pointer;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      z-index: 9999;
    }

    #backToTop:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <!-- Scroll Progress Bar -->
  <div id="scrollProgress"></div>

  <!-- Back To Top Button -->
  <button id="backToTop" title="Back to Top">↑</button>

  <!-- Example Content -->
  <div style="height: 3000px; padding: 20px;">
    <h1>Scroll Down to See the Progress Bar and Back To Top Button</h1>
    <p>Keep scrolling to test the functionality.</p>
  </div>

  <script>
    // Get references to the elements
    const scrollProgress = document.getElementById('scrollProgress');
    const backToTop = document.getElementById('backToTop');

    // Function to update the scroll progress bar
    function updateScrollProgress() {
      const scrollTop = window.scrollY; // Current scroll position
      const scrollHeight = document.documentElement.scrollHeight; // Total scrollable height
      const clientHeight = document.documentElement.clientHeight; // Viewport height
      const scrollPercentage = (scrollTop / (scrollHeight - clientHeight)) * 100;

      // Update the width of the progress bar
      scrollProgress.style.width = `${scrollPercentage}%`;

      // Show or hide the Back To Top button based on scroll position
      if (scrollTop > 300) {
        backToTop.style.display = 'block';
      } else {
        backToTop.style.display = 'none';
      }
    }

    // Function to scroll back to the top
    function scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // Smooth scrolling
      });
    }

    // Attach event listeners
    window.addEventListener('scroll', updateScrollProgress); // Update progress bar on scroll
    backToTop.addEventListener('click', scrollToTop); // Scroll to top on button click
  </script>
</body>
</html>
```
