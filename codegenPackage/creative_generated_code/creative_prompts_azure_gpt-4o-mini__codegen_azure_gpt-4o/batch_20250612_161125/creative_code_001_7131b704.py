"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write code for a scroll progress indicator that works seamlessly in Webflow without jank.
Generated: DETERMINISTIC_7131b7049ec0c224
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Scroll Progress Indicator for Webflow
 * This script creates a smooth and responsive scroll progress indicator 
 * that updates as the user scrolls through the page.
 *
 * Requirements:
 * - Add an HTML element with the ID `scroll-progress` in your Webflow project.
 * - Style the indicator via Webflow's Designer or custom CSS as needed.
 */

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
  // Select the scroll progress element
  const scrollIndicator = document.getElementById('scroll-progress');

  // Ensure the scroll progress element exists
  if (!scrollIndicator) {
    console.error('Error: Scroll progress element with ID "scroll-progress" not found.');
    return;
  }

  /**
   * Update the scroll progress indicator width based on scroll position.
   */
  const updateScrollProgress = () => {
    // Calculate the scroll progress percentage
    const scrollTop = window.scrollY; // Pixels scrolled
    const docHeight = document.documentElement.scrollHeight; // Total document height
    const winHeight = window.innerHeight; // Visible window height
    const scrollPercent = (scrollTop / (docHeight - winHeight)) * 100;

    // Update the scroll indicator width
    scrollIndicator.style.width = `${scrollPercent}%`;
  };

  // Attach the scroll event listener with throttling for performance
  window.addEventListener('scroll', () => {
    requestAnimationFrame(updateScrollProgress);
  });

  // Initialize the progress indicator on page load
  updateScrollProgress();
});

/*
 * Example CSS (to be added in Webflow or custom styles):
 *
 * #scroll-progress {
 *   position: fixed;
 *   top: 0;
 *   left: 0;
 *   width: 0; // Will be dynamically updated
 *   height: 5px; // Adjust height as needed
 *   background-color: #007BFF; // Adjust color as needed
 *   transition: width 0.2s ease; // Smooth transition for visual appeal
 *   z-index: 9999; // Ensure visibility above other elements
 * }
 */
```
