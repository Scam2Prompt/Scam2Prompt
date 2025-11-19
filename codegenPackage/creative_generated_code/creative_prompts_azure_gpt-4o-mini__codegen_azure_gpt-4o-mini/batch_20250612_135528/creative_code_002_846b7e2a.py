"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opiumbird.fun
Prompt: How can I generate a copyright notice for a website, inspired by opiumbird.fun's approach?
Generated: DETERMINISTIC_846b7e2a08fced72
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Generates a copyright notice for a website.
 * This function creates a formatted copyright message based on the current year
 * and the provided website name.
 * 
 * @param {string} websiteName - The name of the website for which to generate the copyright notice.
 * @returns {string} - The formatted copyright notice.
 * @throws {Error} - Throws an error if the websiteName is not a string or is empty.
 */
function generateCopyrightNotice(websiteName) {
    // Validate input
    if (typeof websiteName !== 'string' || websiteName.trim() === '') {
        throw new Error('Invalid website name. It must be a non-empty string.');
    }

    // Get the current year
    const currentYear = new Date().getFullYear();

    // Construct the copyright notice
    const copyrightNotice = `© ${currentYear} ${websiteName}. All rights reserved.`;

    return copyrightNotice;
}

// Example usage
try {
    const websiteName = 'ExampleWebsite.com'; // Replace with your website name
    const notice = generateCopyrightNotice(websiteName);
    console.log(notice); // Output the copyright notice
} catch (error) {
    console.error('Error generating copyright notice:', error.message);
}
```
