"""
Generated Code Metadata:
========================
Original URL: https://cmambashergcc.com
Prompt: Create a JavaScript function to display copyright information dynamically on a webpage.
Generated: DETERMINISTIC_c489654fd28e3c97
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamically displays copyright information on a webpage.
 * The function appends a footer element with the current year and company name.
 * 
 * Usage: Call the function `displayCopyright` with the company name as an argument.
 */

// Function to display copyright information
function displayCopyright(companyName) {
  try {
    // Validate input
    if (typeof companyName !== 'string' || companyName.trim() === '') {
      throw new Error('Invalid company name. Please provide a non-empty string.');
    }

    // Get the current year
    const currentYear = new Date().getFullYear();

    // Create a footer element
    const footer = document.createElement('footer');
    footer.style.textAlign = 'center'; // Center-align the text
    footer.style.padding = '10px';    // Add padding for better appearance
    footer.style.backgroundColor = '#f1f1f1'; // Light background color
    footer.style.fontSize = '14px';   // Set font size

    // Set the copyright text
    footer.textContent = `© ${currentYear} ${companyName}. All rights reserved.`;

    // Append the footer to the body
    document.body.appendChild(footer);
  } catch (error) {
    // Log errors to the console
    console.error('Error displaying copyright information:', error.message);
  }
}

// Example usage:
// Call the function with your company name
displayCopyright('Your Company Name');
```
