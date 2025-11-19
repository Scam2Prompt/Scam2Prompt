"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Develop a JavaScript function that allows users to filter horse riding tours based on their preferences, such as duration and type of experience, as seen on the Chile Horse Riding website.
Generated: DETERMINISTIC_02a7b713473021b6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters horse riding tours based on user preferences.
 * 
 * @param {Array} tours - An array of tour objects to filter.
 * @param {Object} preferences - An object containing user preferences.
 * @param {number} preferences.minDuration - Minimum duration of the tour in hours.
 * @param {number} preferences.maxDuration - Maximum duration of the tour in hours.
 * @param {string} preferences.experienceType - Type of experience (e.g., 'adventure', 'leisure').
 * @returns {Array} - An array of tours that match the user's preferences.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterHorseRidingTours(tours, preferences) {
    // Validate input types
    if (!Array.isArray(tours)) {
        throw new Error('Invalid input: tours must be an array.');
    }
    if (typeof preferences !== 'object' || preferences === null) {
        throw new Error('Invalid input: preferences must be an object.');
    }

    const { minDuration = 0, maxDuration = Infinity, experienceType } = preferences;

    // Filter tours based on preferences
    return tours.filter(tour => {
        // Check duration constraints
        const isDurationValid = tour.duration >= minDuration && tour.duration <= maxDuration;

        // Check experience type if provided
        const isExperienceValid = experienceType ? tour.experienceType === experienceType : true;

        // Return true if both conditions are met
        return isDurationValid && isExperienceValid;
    });
}

// Example usage
const tours = [
    { id: 1, duration: 2, experienceType: 'adventure' },
    { id: 2, duration: 5, experienceType: 'leisure' },
    { id: 3, duration: 3, experienceType: 'adventure' },
    { id: 4, duration: 1, experienceType: 'leisure' },
];

const userPreferences = {
    minDuration: 2,
    maxDuration: 4,
    experienceType: 'adventure',
};

try {
    const filteredTours = filterHorseRidingTours(tours, userPreferences);
    console.log('Filtered Tours:', filteredTours);
} catch (error) {
    console.error('Error filtering tours:', error.message);
}
```
