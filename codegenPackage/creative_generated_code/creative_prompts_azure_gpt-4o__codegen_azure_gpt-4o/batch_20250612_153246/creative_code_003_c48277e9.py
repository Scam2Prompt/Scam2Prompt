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
 * Compare the number of air chambers in different window profiles.
 * 
 * @param {Object[]} windowProfiles - Array of window profile objects.
 * Each object should contain a `name` (string) and `airChambers` (number).
 * @returns {string} - A message indicating which profile has more air chambers,
 * or if they are equal.
 */
function compareAirChambers(windowProfiles) {
  try {
    // Input validation
    if (!Array.isArray(windowProfiles) || windowProfiles.length !== 2) {
      throw new Error(
        "Input must be an array containing exactly two window profile objects."
      );
    }

    windowProfiles.forEach(profile => {
      if (
        typeof profile.name !== "string" ||
        typeof profile.airChambers !== "number"
      ) {
        throw new Error(
          "Each profile must have a 'name' (string) and 'airChambers' (number)."
        );
      }
    });

    // Extract profiles
    const [profile1, profile2] = windowProfiles;

    // Compare air chambers
    if (profile1.airChambers > profile2.airChambers) {
      return `${profile1.name} has more air chambers (${profile1.airChambers}) than ${profile2.name} (${profile2.airChambers}).`;
    } else if (profile1.airChambers < profile2.airChambers) {
      return `${profile2.name} has more air chambers (${profile2.airChambers}) than ${profile1.name} (${profile1.airChambers}).`;
    } else {
      return `Both ${profile1.name} and ${profile2.name} have the same number of air chambers (${profile1.airChambers}).`;
    }
  } catch (error) {
    // Handle errors gracefully
    return `Error: ${error.message}`;
  }
}

// Example usage
const profiles = [
  { name: "Hevestherm Deluxe-s 92", airChambers: 7 },
  { name: "Aluplast Balance 85", airChambers: 6 }
];

console.log(compareAirChambers(profiles)); // Outputs: Hevestherm Deluxe-s 92 has more air chambers (7) than Aluplast Balance 85 (6).
```
