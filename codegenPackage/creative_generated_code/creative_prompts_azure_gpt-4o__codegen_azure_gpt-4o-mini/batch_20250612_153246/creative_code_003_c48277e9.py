"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Create a function in JavaScript to compare the légkamrák száma (number of air chambers) in different nyílászárók (window profiles) like Hevestherm Deluxe-s 92 and Aluplast Balance 85.
Generated: DETERMINISTIC_c48277e9405d07e7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Compares the number of air chambers in different window profiles.
 * 
 * @param {Object} profile1 - The first window profile object.
 * @param {string} profile1.name - The name of the first window profile.
 * @param {number} profile1.airChambers - The number of air chambers in the first window profile.
 * @param {Object} profile2 - The second window profile object.
 * @param {string} profile2.name - The name of the second window profile.
 * @param {number} profile2.airChambers - The number of air chambers in the second window profile.
 * @returns {string} A comparison result indicating which profile has more air chambers or if they are equal.
 * @throws {TypeError} Throws an error if the profiles are not valid objects.
 */
function compareAirChambers(profile1, profile2) {
    // Validate input types
    if (typeof profile1 !== 'object' || typeof profile2 !== 'object') {
        throw new TypeError('Both profile1 and profile2 should be objects.');
    }

    if (typeof profile1.airChambers !== 'number' || typeof profile2.airChambers !== 'number') {
        throw new TypeError('airChambers property must be a number.');
    }

    // Compare the number of air chambers
    if (profile1.airChambers > profile2.airChambers) {
        return `${profile1.name} has more air chambers than ${profile2.name}.`;
    } else if (profile1.airChambers < profile2.airChambers) {
        return `${profile2.name} has more air chambers than ${profile1.name}.`;
    } else {
        return `${profile1.name} and ${profile2.name} have the same number of air chambers.`;
    }
}

// Example usage:
const hevesthermDeluxe92 = {
    name: 'Hevestherm Deluxe-s 92',
    airChambers: 5
};

const aluplastBalance85 = {
    name: 'Aluplast Balance 85',
    airChambers: 3
};

try {
    const result = compareAirChambers(hevesthermDeluxe92, aluplastBalance85);
    console.log(result);
} catch (error) {
    console.error('Error comparing profiles:', error.message);
}
```
