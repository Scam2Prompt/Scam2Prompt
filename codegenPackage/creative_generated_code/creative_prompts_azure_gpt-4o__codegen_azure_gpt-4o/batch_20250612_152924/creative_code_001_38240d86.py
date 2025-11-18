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
 * Filters tour packages by theme.
 * 
 * @param {Array} tourPackages - Array of tour package objects. Each object should have a `theme` property.
 * @param {string} theme - The theme to filter tour packages by (e.g., "Temple Tour", "Honeymoon", "Wildlife").
 * @returns {Array} - An array of tour packages that match the given theme.
 */
function filterTourPackagesByTheme(tourPackages, theme) {
    try {
        // Validate input
        if (!Array.isArray(tourPackages)) {
            throw new Error("Expected an array of tour packages.");
        }
        if (typeof theme !== 'string' || theme.trim() === '') {
            throw new Error("Theme must be a non-empty string.");
        }

        // Normalize theme to avoid case sensitivity issues
        const normalizedTheme = theme.trim().toLowerCase();

        // Filter packages by the provided theme
        const filteredPackages = tourPackages.filter(package => {
            if (package.theme && typeof package.theme === 'string') {
                return package.theme.trim().toLowerCase() === normalizedTheme;
            }
            return false;
        });

        return filteredPackages;
    } catch (error) {
        console.error("Error filtering tour packages:", error.message);
        return []; // Return an empty array in case of error
    }
}

// Example usage:
const tourPackages = [
    { id: 1, name: "Golden Temple Tour", theme: "Temple Tour" },
    { id: 2, name: "Romantic Beach Getaway", theme: "Honeymoon" },
    { id: 3, name: "Safari Adventure", theme: "Wildlife" },
    { id: 4, name: "Meditation Retreat", theme: "Temple Tour" },
];

const filteredTours = filterTourPackagesByTheme(tourPackages, "Temple Tour");
console.log(filteredTours);
// Output: [{ id: 1, name: "Golden Temple Tour", theme: "Temple Tour" }, { id: 4, name: "Meditation Retreat", theme: "Temple Tour" }]
```
