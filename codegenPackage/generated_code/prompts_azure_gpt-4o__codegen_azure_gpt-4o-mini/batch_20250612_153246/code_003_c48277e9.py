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
 * 
 * @param {Object} profile1 - The first window profile object.
 * @param {Object} profile2 - The second window profile object.
 * @returns {string} - A message indicating which profile has more air chambers, or if they are equal.
 * @throws {Error} - Throws an error if the profiles do not have a valid number of air chambers.
 */
function compareAirChambers(profile1, profile2) {
    // Validate input profiles
    if (!profile1 || !profile2) {
        throw new Error("Both profiles must be provided.");
    }
    
    if (typeof profile1.airChambers !== 'number' || typeof profile2.airChambers !== 'number') {
        throw new Error("Both profiles must have a valid number of air chambers.");
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

// Example usage
const hevesthermDeluxe92 = {
    name: "Hevestherm Deluxe-s 92",
    airChambers: 5
};

const aluplastBalance85 = {
    name: "Aluplast Balance 85",
    airChambers: 3
};

try {
    const result = compareAirChambers(hevesthermDeluxe92, aluplastBalance85);
    console.log(result);
} catch (error) {
    console.error("Error comparing profiles:", error.message);
}
```
