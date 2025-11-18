"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write a Webflow-specific tutorial for adding a radial scroll progress indicator with dynamic updates and "Back to Top" functionality, as featured on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_74246b66e5627c7f
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Webflow Radial Scroll Progress Indicator with "Back to Top" Functionality
 * 
 * This script creates a radial scroll progress indicator that dynamically updates
 * based on scroll progress. It also includes a "Back to Top" button functionality.
 * Ensure to include a matching HTML structure in your Webflow project, including:
 * - A circular progress bar (SVG or div)
 * - A "Back to Top" button
 * Customize IDs and classes below as needed.
 */

document.addEventListener("DOMContentLoaded", () => {
  // Configuration: Customize selectors for indicator and "Back to Top" button
  const progressIndicator = document.querySelector("#scroll-progress-indicator"); // Replace with your progress indicator's ID or class
  const backToTopButton = document.querySelector("#back-to-top-button"); // Replace with your button's ID or class

  // Validate that required elements exist
  if (!progressIndicator || !backToTopButton) {
    console.error("Error: Progress indicator or Back to Top button not found. Check your selectors.");
    return;
  }

  // Function to update the radial progress indicator based on scroll position
  const updateScrollIndicator = () => {
    const scrollTop = window.scrollY; // Current scroll position
    const documentHeight = document.documentElement.scrollHeight; // Full document height
    const windowHeight = window.innerHeight; // Height of the viewport
    const scrollPercentage = (scrollTop / (documentHeight - windowHeight)) * 100; // Calculate scroll progress percentage

    // Update radial progress indicator value (adjust logic based on your implementation)
    progressIndicator.style.background = `conic-gradient(
      #00f ${scrollPercentage}%, 
      #ccc ${scrollPercentage}%
    )`;
  };

  // Function to scroll the page back to the top
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" }); // Scroll to top with smooth behavior
  };

  // Event listener for scroll updates
  window.addEventListener("scroll", updateScrollIndicator);

  // Event listener for "Back to Top" button click
  backToTopButton.addEventListener("click", scrollToTop);

  // Initial call to update radial indicator on page load
  updateScrollIndicator();
});
```

**HTML Structure Example**:
```html
<div id="scroll-progress-indicator" style="width: 50px; height: 50px; border-radius: 50%; background: conic-gradient(#00f 0%, #ccc 0%);">
</div>
<button id="back-to-top-button" style="position: fixed; bottom: 20px; right: 20px;">Back to Top</button>
```

**CSS Example**:
```css
/* Style for the radial progress indicator */
#scroll-progress-indicator {
  position: fixed;
  bottom: 20px;
  left: 20px;
  z-index: 1000;
}

/* Style for the "Back to Top" button */
#back-to-top-button {
  background-color: #00f;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  cursor: pointer;
}

#back-to-top-button:hover {
  background-color: #0057ff;
}
```

This code is production-ready and adheres to best practices. Adjust the selectors and styles as needed for your Webflow project.
