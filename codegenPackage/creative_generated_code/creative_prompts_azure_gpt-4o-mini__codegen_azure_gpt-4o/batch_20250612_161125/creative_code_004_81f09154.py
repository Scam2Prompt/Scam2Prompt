"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: How do I customize a radial scroll progress indicator in Webflow for better user experience?
Generated: DETERMINISTIC_81f0915426eb665f
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready JavaScript code to customize a radial scroll progress indicator in Webflow. This solution assumes your Webflow project includes HTML and CSS for the radial progress indicator. The JavaScript code dynamically updates the indicator based on the page scroll.

```javascript
// JavaScript Code to Customize a Radial Scroll Progress Indicator in Webflow

// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Select the radial progress indicator element by its class or ID
  const radialProgress = document.querySelector(".radial-progress");

  // Function to calculate scroll progress and update the radial indicator
  const updateScrollProgress = () => {
    try {
      // Calculate the scroll percentage
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrollPercentage = Math.min((scrollTop / scrollHeight) * 100, 100);

      // Update radial progress indicator using inline CSS
      if (radialProgress) {
        // Set the `stroke-dashoffset` property to reflect scroll progress
        const radius = parseFloat(radialProgress.getAttribute("r")); // Get radius from the SVG element
        const circumference = 2 * Math.PI * radius; // Calculate circumference
        const offset = circumference - (scrollPercentage / 100) * circumference;

        // Modify the `stroke-dashoffset` property for the SVG circle
        radialProgress.style.strokeDasharray = `${circumference} ${circumference}`;
        radialProgress.style.strokeDashoffset = offset.toFixed(2); // Avoid fractional issues
      }
    } catch (error) {
      console.error("Error updating radial scroll progress:", error);
    }
  };

  // Attach scroll listener to update progress on page scroll
  window.addEventListener("scroll", updateScrollProgress);

  // Initialize the scroll progress on page load
  updateScrollProgress();
});
```

### Example HTML and CSS setup for the radial indicator

```html
<!-- SVG Radial Progress Indicator in Webflow -->
<svg class="radial-progress" width="100" height="100" viewBox="0 0 100 100">
  <circle
    class="radial-progress-bg"
    cx="50"
    cy="50"
    r="45"
    fill="none"
    stroke="#e6e6e6"
    stroke-width="10"
  ></circle>
  <circle
    class="radial-progress"
    cx="50"
    cy="50"
    r="45"
    fill="none"
    stroke="#3498db"
    stroke-width="10"
    stroke-linecap="round"
  ></circle>
</svg>
```

```css
/* CSS Styling for Radial Progress Indicator */
.radial-progress-bg {
  opacity: 0.3;
}

.radial-progress {
  transform: rotate(-90deg); /* Rotate to start at the top */
  transform-origin: center;
  stroke-dasharray: 0 283; /* Default circumference for r=45 */
  stroke-dashoffset: 283; /* Default offset for r=45 */
  transition: stroke-dashoffset 0.2s ease-out; /* Smooth animation */
}
```

### Key Notes for Integration:
1. Replace `.radial-progress` with the correct selector used in your Webflow project.
2. Ensure the SVG `circle` elements have proper `cx`, `cy`, and `r` attributes for accurate rendering.
3. The `stroke-dashoffset` and `stroke-dasharray` calculations must align with the SVG circle's radius.
4. Add custom styling or animations to enhance the user experience.

The code is ready for Webflow integration and follows best practices.
