"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibanshee.com
Prompt: Write JavaScript code to add hover effects like "Slide Up" and "Expand" for portfolio items, as detailed on the aibanshee.com website.
Generated: DETERMINISTIC_987490608eb6c6ca
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript Code for Hover Effects: "Slide Up" and "Expand"

// Ensure the DOM is fully loaded before running the script
document.addEventListener("DOMContentLoaded", () => {
  // Select all portfolio items
  const portfolioItems = document.querySelectorAll(".portfolio-item");

  // Loop through each portfolio item and attach event listeners
  portfolioItems.forEach((item) => {
    // Mouse Enter - Apply hover effect
    item.addEventListener("mouseenter", () => {
      // Add CSS classes for Slide Up and Expand effects
      item.classList.add("hover-slide-up");
      item.classList.add("hover-expand");
    });

    // Mouse Leave - Remove hover effect
    item.addEventListener("mouseleave", () => {
      // Remove CSS classes for Slide Up and Expand effects
      item.classList.remove("hover-slide-up");
      item.classList.remove("hover-expand");
    });
  });
});

// CSS classes are dynamically added and removed through JavaScript
// Ensure the following CSS is implemented in your stylesheet for the hover effects:

/*
.portfolio-item {
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.hover-slide-up {
  transform: translateY(-10px); // Adjust translateY value as needed
}

.hover-expand {
  transform: scale(1.05); // Adjust scale value as needed
}
*/
```
