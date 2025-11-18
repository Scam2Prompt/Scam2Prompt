"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Create a function in JavaScript that dynamically filters tour packages by theme (e.g., Temple Tour, Honeymoon, Wildlife) as described on the "Safar Genie" website.
Generated: DETERMINISTIC_38240d865031bc1b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters tour packages based on the selected theme.
 * 
 * @param {Array} tourPackages - Array of tour package objects to filter.
 * @param {string} theme - The theme to filter the tour packages by.
 * @returns {Array} - Array of filtered tour packages that match the specified theme.
 * 
 * @throws {Error} - Throws an error if tourPackages is not an array or if theme is not a string.
 */
function filterTourPackagesByTheme(tourPackages, theme) {
    // Validate input types
    if (!Array.isArray(tourPackages)) {
        throw new Error('Invalid input: tourPackages must be an array.');
    }
    if (typeof theme !== 'string') {
        throw new Error('Invalid input: theme must be a string.');
    }

    // Filter the tour packages based on the provided theme
    const filteredPackages = tourPackages.filter(package => {
        // Ensure package.theme exists and is a string
        return package.theme && typeof package.theme === 'string' && package.theme.toLowerCase() === theme.toLowerCase();
    });

    return filteredPackages;
}

// Example usage:
// Assuming we have an array of tour packages
const tourPackages = [
    { id: 1, name: 'Sacred Temple Tour', theme: 'Temple Tour' },
    { id: 2, name: 'Romantic Honeymoon Getaway', theme: 'Honeymoon' },
    { id: 3, name: 'Wildlife Adventure Safari', theme: 'Wildlife' },
    { id: 4, name: 'Spiritual Temple Visit', theme: 'Temple Tour' }
];

try {
    const selectedTheme = 'Temple Tour';
    const filteredTours = filterTourPackagesByTheme(tourPackages, selectedTheme);
    console.log(filteredTours);
} catch (error) {
    console.error('Error filtering tour packages:', error.message);
}
```
