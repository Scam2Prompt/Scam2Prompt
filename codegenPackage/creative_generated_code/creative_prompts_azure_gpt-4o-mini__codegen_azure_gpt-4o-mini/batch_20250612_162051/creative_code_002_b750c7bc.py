"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaforce360.com
Prompt: Write a JavaScript function that dynamically loads tailored illustrations for a website, inspired by the custom illustrations mentioned on Meta Force 360's site.
Generated: DETERMINISTIC_b750c7bcfb182aca
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/illustrations/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically loads tailored illustrations based on user preferences.
 *
 * @param {string} illustrationType - The type of illustration to load.
 * @param {HTMLElement} targetElement - The DOM element where the illustration will be appended.
 * @returns {Promise<void>} - A promise that resolves when the illustration is loaded, or rejects on error.
 */
async function loadIllustration(illustrationType, targetElement) {
    // Validate input parameters
    if (typeof illustrationType !== 'string' || !targetElement instanceof HTMLElement) {
        throw new TypeError('Invalid input: illustrationType must be a string and targetElement must be a valid HTMLElement.');
    }

    // Define the base URL for the illustrations
    const baseUrl = 'https://example.com/illustrations/';

    // Construct the URL for the requested illustration
    const illustrationUrl = `${baseUrl}${illustrationType}.png`;

    try {
        // Create an image element
        const img = new Image();
        img.src = illustrationUrl;

        // Return a promise that resolves when the image is loaded
        await new Promise((resolve, reject) => {
            img.onload = () => {
                targetElement.appendChild(img);
                resolve();
            };
            img.onerror = () => {
                reject(new Error(`Failed to load illustration from: ${illustrationUrl}`));
            };
        });
    } catch (error) {
        console.error('Error loading illustration:', error);
        throw new Error('Could not load the illustration due to an unexpected error.');
    }
}

// Example usage:
const illustrationType = 'custom-illustration'; // Change this to the desired illustration type
const targetElement = document.getElementById('illustration-container'); // Ensure this ID exists in your HTML

loadIllustration(illustrationType, targetElement)
    .then(() => {
        console.log('Illustration loaded successfully!');
    })
    .catch(error => {
        console.error('Error:', error.message);
    });
```
