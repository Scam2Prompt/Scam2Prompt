"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: What are the steps to create a "Back To Top" button integrated with a scroll progress indicator in Webflow?
Generated: DETERMINISTIC_5760fab4c7589001
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
  <title>Back To Top with Scroll Progress</title>
  <style>
    /* Base styles for the button */
    #backToTop {
      position: fixed;
      bottom: 20px;
      right: 20px;
      display: none; /* Initially hidden */
      background-color: #007bff; /* Button color */
      color: #fff;
      border: none;
      padding: 10px 15px;
      border-radius: 5px;
      cursor: pointer;
      z-index: 1000;
    }

    #backToTop:hover {
      background-color: #0056b3;
    }

    /* Progress bar styles */
    #scrollProgress {
      position: fixed;
      top: 0;
      left: 0;
      width: 0; /* Dynamic width */
      height: 5px; /* Bar height */
      background-color: #007bff; /* Bar color */
      z-index: 999;
    }
  </style>
</head>
<body>
  <!-- Scroll progress indicator -->
  <div id="scrollProgress"></div>

  <!-- Back to top button -->
  <button id="backToTop">Back to Top</button>

  <!-- Simulate content for scrolling -->
  <div style="height: 2000px; padding: 20px;">
    <h1>Scroll Down to See the Button</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
  </div>

  <script>
    // Get references to the button and progress bar elements
    const backToTopButton = document.getElementById('backToTop');
    const scrollProgress = document.getElementById('scrollProgress');

    // Function to update scroll progress indicator width and toggle button visibility
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY; // Current vertical scroll position
      const scrollHeight = document.documentElement.scrollHeight; // Total height of the document
      const clientHeight = document.documentElement.clientHeight; // Height of the viewport

      // Calculate scroll percentage
      const scrollPercentage = (scrollTop / (scrollHeight - clientHeight)) * 100;

      // Update progress bar width
      scrollProgress.style.width = `${scrollPercentage}%`;

      // Show/hide the "Back to Top" button based on scroll position
      if (scrollTop > 300) { // Show after scrolling down 300px
        backToTopButton.style.display = 'block';
      } else {
        backToTopButton.style.display = 'none';
      }
    });

    // Function to smoothly scroll back to top when button is clicked
    backToTopButton.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // Smooth scrolling
      });
    });
  </script>
</body>
</html>
```
