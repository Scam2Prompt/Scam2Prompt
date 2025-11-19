"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write code for a scroll progress indicator that works seamlessly in Webflow without jank.
Generated: DETERMINISTIC_7131b7049ec0c224
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
  <title>Scroll Progress Indicator</title>
  <style>
    /* Style for the progress bar */
    #scroll-progress {
      position: fixed;
      top: 0;
      left: 0;
      width: 0;
      height: 5px;
      background-color: #3498db; /* Progress bar color */
      z-index: 9999; /* Ensure it stays above other elements */
      transition: width 0.1s ease-out; /* Smooth transition for progress updates */
    }
  </style>
</head>
<body>
  <!-- Scroll progress bar -->
  <div id="scroll-progress"></div>

  <!-- Example content to scroll -->
  <div style="height: 3000px; padding: 20px;">
    <h1>Scroll Down to See the Progress Indicator</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel nisi nec justo tincidunt tincidunt. Scroll to test the progress bar.</p>
  </div>

  <script>
    // Select the progress bar element
    const progressBar = document.getElementById('scroll-progress');

    // Function to update the progress bar width based on scroll position
    const updateProgressBar = () => {
      try {
        // Calculate the scroll progress as a percentage
        const scrollTop = window.scrollY; // Current scroll position
        const scrollHeight = document.documentElement.scrollHeight; // Total height of the document
        const clientHeight = document.documentElement.clientHeight; // Height of the viewport
        const scrollableHeight = scrollHeight - clientHeight; // Total scrollable height

        // Ensure scrollableHeight is not zero to avoid division by zero
        if (scrollableHeight > 0) {
          const scrollPercentage = (scrollTop / scrollableHeight) * 100;
          progressBar.style.width = `${scrollPercentage}%`; // Update the width of the progress bar
        }
      } catch (error) {
        console.error('Error updating scroll progress:', error); // Log any errors
      }
    };

    // Attach the scroll event listener to the window
    window.addEventListener('scroll', updateProgressBar);

    // Ensure the progress bar updates on page load
    window.addEventListener('load', updateProgressBar);
  </script>
</body>
</html>
```
