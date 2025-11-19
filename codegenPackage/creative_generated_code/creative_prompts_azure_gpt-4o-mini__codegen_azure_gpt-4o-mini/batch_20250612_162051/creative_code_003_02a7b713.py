"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Develop a JavaScript function that allows users to filter horse riding tours based on their preferences, such as duration and type of experience, as seen on the Chile Horse Riding website.
Generated: DETERMINISTIC_02a7b713473021b6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters horse riding tours based on user preferences.
 * 
 * @param {Array} tours - An array of tour objects to filter.
 * @param {Object} preferences - An object containing user preferences.
 * @param {number} preferences.minDuration - Minimum duration of the tour in hours.
 * @param {number} preferences.maxDuration - Maximum duration of the tour in hours.
 * @param {string} preferences.experienceType - Desired type of experience (e.g., "adventure", "leisure").
 * @returns {Array} - An array of filtered tour objects that match the user's preferences.
 * @throws {Error} - Throws an error if tours is not an array or if preferences is not an object.
 */
function filterHorseRidingTours(tours, preferences) {
    // Validate input types
    if (!Array.isArray(tours)) {
        throw new Error('Invalid input: tours must be an array.');
    }
    if (typeof preferences !== 'object' || preferences === null) {
        throw new Error('Invalid input: preferences must be an object.');
    }

    const { minDuration, maxDuration, experienceType } = preferences;

    // Filter tours based on user preferences
    return tours.filter(tour => {
        // Validate tour properties
        const isValidDuration = typeof tour.duration === 'number';
        const isValidExperienceType = typeof tour.experienceType === 'string';

        // Check duration criteria
        const durationCondition = isValidDuration &&
            tour.duration >= (minDuration || 0) &&
            tour.duration <= (maxDuration || Infinity);

        // Check experience type criteria
        const experienceCondition = !experienceType || 
            (isValidExperienceType && tour.experienceType === experienceType);

        return durationCondition && experienceCondition;
    });
}

// Example usage:

const tours = [
    { id: 1, duration: 3, experienceType: 'adventure' },
    { id: 2, duration: 2, experienceType: 'leisure' },
    { id: 3, duration: 5, experienceType: 'adventure' },
    { id: 4, duration: 4, experienceType: 'leisure' },
];

const userPreferences = {
    minDuration: 2,
    maxDuration: 4,
    experienceType: 'leisure'
};

try {
    const filteredTours = filterHorseRidingTours(tours, userPreferences);
    console.log('Filtered Tours:', filteredTours);
} catch (error) {
    console.error('Error filtering tours:', error.message);
}
```
