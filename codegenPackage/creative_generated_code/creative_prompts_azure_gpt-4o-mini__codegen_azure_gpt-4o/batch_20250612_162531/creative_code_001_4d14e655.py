"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claiming.website
Prompt: Write a function to automatically update copyright information on a website footer using JavaScript.
Generated: DETERMINISTIC_4d14e65540f76c9f
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to automatically update the copyright year in the website footer.
 * This function assumes there is a footer element with the ID "footer-copyright".
 * It updates the text content of the element to reflect the current year.
 */
function updateCopyrightFooter() {
  try {
    // Get the current year
    const currentYear = new Date().getFullYear();

    // Select the footer element by its ID
    const footerElement = document.getElementById("footer-copyright");

    // Validate if the element exists
    if (!footerElement) {
      console.error("Footer element with ID 'footer-copyright' not found.");
      return;
    }

    // Update the footer text content
    footerElement.textContent = `© ${currentYear} Your Company Name. All rights reserved.`;
  } catch (error) {
    // Log any unexpected errors
    console.error("An error occurred while updating the copyright footer:", error);
  }
}

// Ensure the function is executed after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", updateCopyrightFooter);
```
