"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cint.privacykeeper.cc
Prompt: Generate a code snippet for handling broken links in a web application using JavaScript.
Generated: DETERMINISTIC_a6a3cc0b35f89292
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This function checks for broken links in a web application.
 * It iterates through all anchor tags in the document and verifies
 * if the links are reachable. If a link is broken, it logs the error 
 * and updates the UI to reflect the broken status.
 */
async function checkBrokenLinks() {
    // Get all anchor tags in the document
    const links = document.querySelectorAll('a');

    // Array to store promises for link status
    const linkStatusPromises = Array.from(links).map(async (link) => {
        try {
            // Fetch the link's URL to check its status
            const response = await fetch(link.href, { method: 'HEAD', mode: 'no-cors' });

            // Check if the response status is OK (200-299)
            if (!response.ok) {
                throw new Error(`Broken link: ${link.href}`);
            }
        } catch (error) {
            // Log the error and update the UI for broken links
            console.error(error.message);
            link.style.color = 'red'; // Change link color to indicate a broken link
            link.title = 'This link is broken'; // Provide a tooltip for broken links
        }
    });

    // Wait for all link status checks to complete
    await Promise.all(linkStatusPromises);
}

// Run the function to check for broken links when the document is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    checkBrokenLinks().catch((error) => {
        console.error('Error checking broken links:', error);
    });
});
```
