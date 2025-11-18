"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staketelegramapp.com
Prompt: Generate JavaScript code to implement collapsible groups for a portfolio section, ensuring functionality similar to the collapsible items described in the Avenger template.
Generated: DETERMINISTIC_1a90c01e30edad4d
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Collapsible Portfolio Group Functionality
 * 
 * This code implements collapsible groups for a portfolio section.
 * Each group can be expanded or collapsed by clicking on its header.
 * 
 * Features:
 * - Groups toggle between expanded and collapsed states.
 * - Only one group is expanded at a time (optional: accordion-like behavior).
 */

// Ensure the code runs only after the DOM has fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Select all collapsible group headers
  const headers = document.querySelectorAll(".portfolio-group-header");

  // Add a click event listener to each header
  headers.forEach(header => {
    header.addEventListener("click", () => {
      // Toggle the active class on the clicked header
      header.classList.toggle("active");

      // Retrieve the associated content section
      const content = header.nextElementSibling;

      // Check if content is currently visible
      if (content.style.maxHeight) {
        // Collapse the content
        content.style.maxHeight = null;
      } else {
        // Expand the content
        content.style.maxHeight = content.scrollHeight + "px";
      }

      // Optional: Ensure only one group is expanded at a time (accordion behavior)
      headers.forEach(otherHeader => {
        if (otherHeader !== header && otherHeader.classList.contains("active")) {
          otherHeader.classList.remove("active");
          const otherContent = otherHeader.nextElementSibling;
          otherContent.style.maxHeight = null;
        }
      });
    });
  });
});

/**
 * Recommended HTML structure for this JavaScript:
 * 
 * <div class="portfolio-group">
 *   <div class="portfolio-group-header">Group Title 1</div>
 *   <div class="portfolio-group-content">
 *     <p>Content for Group 1</p>
 *   </div>
 * </div>
 * 
 * <div class="portfolio-group">
 *   <div class="portfolio-group-header">Group Title 2</div>
 *   <div class="portfolio-group-content">
 *     <p>Content for Group 2</p>
 *   </div>
 * </div>
 * 
 * CSS Example for Styling (ensure collapsible behavior):
 * 
 * .portfolio-group-content {
 *   max-height: 0;
 *   overflow: hidden;
 *   transition: max-height 0.3s ease;
 * }
 * 
 * .portfolio-group-header {
 *   cursor: pointer;
 *   background-color: #f4f4f4;
 *   padding: 10px;
 *   border: 1px solid #ddd;
 * }
 * 
 * .portfolio-group-header.active {
 *   background-color: #e0e0e0;
 * }
 */
```
