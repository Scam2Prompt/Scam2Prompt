"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: Create a function in JavaScript to compare the légkamrák száma (number of air chambers) in different nyílászárók (window profiles) like Hevestherm Deluxe-s 92 and Aluplast Balance 85.
Generated: DETERMINISTIC_c48277e9405d07e7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Compares the number of air chambers in different window profiles.
 * @param {Object[]} profiles - Array of window profile objects to compare.
 * @param {string} profiles[].name - Name of the window profile.
 * @param {number} profiles[].airChambers - Number of air chambers in the profile.
 * @returns {Object} Comparison result with details and the profile with most chambers.
 * @throws {Error} If input is invalid or empty.
 */
function compareAirChambers(profiles) {
    // Validate input
    if (!Array.isArray(profiles) || profiles.length === 0) {
        throw new Error('Input must be a non-empty array of profiles');
    }

    // Check each profile has required properties
    const invalidProfiles = profiles.filter(profile => 
        !profile.name || typeof profile.airChambers !== 'number'
    );
    
    if (invalidProfiles.length > 0) {
        throw new Error('Each profile must have a name and numeric airChambers property');
    }

    // Find profile with maximum air chambers
    const maxChambersProfile = profiles.reduce((max, current) => 
        current.airChambers > max.airChambers ? current : max
    );

    // Calculate comparison data
    const comparison = profiles.map(profile => ({
        name: profile.name,
        airChambers: profile.airChambers,
        differenceFromMax: maxChambersProfile.airChambers - profile.airChambers,
        isMax: profile.name === maxChambersProfile.name
    }));

    return {
        profiles: comparison,
        maxChambersProfile: maxChambersProfile,
        maxChambers: maxChambersProfile.airChambers
    };
}

// Example usage:
/*
const windowProfiles = [
    { name: 'Hevestherm Deluxe-s 92', airChambers: 6 },
    { name: 'Aluplast Balance 85', airChambers: 5 }
];

try {
    const result = compareAirChambers(windowProfiles);
    console.log(result);
} catch (error) {
    console.error('Error:', error.message);
}
*/
```
