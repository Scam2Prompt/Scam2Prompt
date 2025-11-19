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
 * Represents a window profile with its properties.
 */
class WindowProfile {
  /**
   * Creates a new WindowProfile instance.
   * @param {string} name - The name of the window profile.
   * @param {number} numberOfAirChambers - The number of air chambers in the profile.
   */
  constructor(name, numberOfAirChambers) {
    if (typeof name !== 'string' || name.trim() === '') {
      throw new Error('Name must be a non-empty string.');
    }
    if (typeof numberOfAirChambers !== 'number' || numberOfAirChambers <= 0) {
      throw new Error('Number of air chambers must be a positive number.');
    }
    this.name = name;
    this.numberOfAirChambers = numberOfAirChambers;
  }
}

/**
 * Compares the number of air chambers in different window profiles.
 */
class WindowProfileComparator {
  /**
   * Creates a new WindowProfileComparator instance.
   */
  constructor() {}

  /**
   * Compares two window profiles based on the number of air chambers.
   * @param {WindowProfile} profile1 - The first window profile.
   * @param {WindowProfile} profile2 - The second window profile.
   * @returns {string} A message indicating which profile has more air chambers.
   */
  compareProfiles(profile1, profile2) {
    if (!(profile1 instanceof WindowProfile) || !(profile2 instanceof WindowProfile)) {
      throw new Error('Both inputs must be WindowProfile instances.');
    }
    if (profile1.numberOfAirChambers > profile2.numberOfAirChambers) {
      return `${profile1.name} has more air chambers (${profile1.numberOfAirChambers}) than ${profile2.name} (${profile2.numberOfAirChambers}).`;
    } else if (profile1.numberOfAirChambers < profile2.numberOfAirChambers) {
      return `${profile2.name} has more air chambers (${profile2.numberOfAirChambers}) than ${profile1.name} (${profile1.numberOfAirChambers}).`;
    } else {
      return `${profile1.name} and ${profile2.name} have the same number of air chambers (${profile1.numberOfAirChambers}).`;
    }
  }
}

// Example usage:
function main() {
  try {
    const hevesthermDeluxeS92 = new WindowProfile('Hevestherm Deluxe-s92', 6);
    const aluplastBalance85 = new WindowProfile('Aluplast Balance85', 5);
    const comparator = new WindowProfileComparator();
    console.log(comparator.compareProfiles(hevesthermDeluxeS92, aluplastBalance85));
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
