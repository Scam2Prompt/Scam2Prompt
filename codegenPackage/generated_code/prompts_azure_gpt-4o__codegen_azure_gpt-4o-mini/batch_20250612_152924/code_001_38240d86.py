"""
Generated Code Metadata:
========================
Original URL: https://safargenie.com
Prompt: Create a function in JavaScript that dynamically filters tour packages by theme (e.g., Temple Tour, Honeymoon, Wildlife) as described on the "Safar Genie" website.
Generated: DETERMINISTIC_38240d865031bc1b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters tour packages based on the selected theme.
 * 
 * @param {Array} tourPackages - An array of tour package objects.
 * @param {string} theme - The theme to filter by (e.g., "Temple Tour", "Honeymoon", "Wildlife").
 * @returns {Array} - An array of tour packages that match the specified theme.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterTourPackagesByTheme(tourPackages, theme) {
    // Validate input types
    if (!Array.isArray(tourPackages)) {
        throw new Error('Invalid input: tourPackages must be an array.');
    }
    if (typeof theme !== 'string') {
        throw new Error('Invalid input: theme must be a string.');
    }

    // Normalize the theme to lowercase for case-insensitive comparison
    const normalizedTheme = theme.toLowerCase();

    // Filter the tour packages based on the theme
    const filteredPackages = tourPackages.filter(package => {
        // Check if the package has a theme property and compare it
        return package.theme && package.theme.toLowerCase() === normalizedTheme;
    });

    return filteredPackages;
}

// Example usage
const tourPackages = [
    { id: 1, name: 'Spiritual Journey', theme: 'Temple Tour' },
    { id: 2, name: 'Romantic Getaway', theme: 'Honeymoon' },
    { id: 3, name: 'Wild Safari', theme: 'Wildlife' },
    { id: 4, name: 'Cultural Exploration', theme: 'Temple Tour' },
];

// Filtering tour packages by theme
try {
    const selectedTheme = 'Temple Tour';
    const result = filterTourPackagesByTheme(tourPackages, selectedTheme);
    console.log('Filtered Tour Packages:', result);
} catch (error) {
    console.error('Error filtering tour packages:', error.message);
}
```
