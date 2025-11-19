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
 * @param {Array} tours - Array of tour objects to filter.
 * @param {Object} preferences - User preferences for filtering.
 * @param {string} [preferences.duration] - Desired tour duration ('half-day', 'full-day', 'multi-day').
 * @param {string} [preferences.experience] - Desired experience level ('beginner', 'intermediate', 'advanced').
 * @param {string} [preferences.type] - Desired tour type ('scenic', 'adventure', 'cultural').
 * @returns {Array} Filtered array of tour objects.
 * @throws {Error} If tours is not an array or preferences is not an object.
 */
function filterHorseRidingTours(tours, preferences) {
    // Validate input parameters
    if (!Array.isArray(tours)) {
        throw new Error('Tours must be an array');
    }
    if (typeof preferences !== 'object' || preferences === null) {
        throw new Error('Preferences must be an object');
    }

    // Destructure preferences with default values
    const {
        duration = null,
        experience = null,
        type = null
    } = preferences;

    return tours.filter(tour => {
        // Check if tour matches all specified preferences
        const matchesDuration = !duration || tour.duration === duration;
        const matchesExperience = !experience || tour.experienceLevel === experience;
        const matchesType = !type || tour.tourType === type;

        return matchesDuration && matchesExperience && matchesType;
    });
}

// Example usage:
/*
const tours = [
    {
        id: 1,
        name: 'Scenic Valley Ride',
        duration: 'half-day',
        experienceLevel: 'beginner',
        tourType: 'scenic',
        price: 100
    },
    {
        id: 2,
        name: 'Mountain Adventure',
        duration: 'full-day',
        experienceLevel: 'intermediate',
        tourType: 'adventure',
        price: 200
    },
    {
        id: 3,
        name: 'Cultural Heritage Tour',
        duration: 'multi-day',
        experienceLevel: 'advanced',
        tourType: 'cultural',
        price: 500
    }
];

const preferences = {
    duration: 'full-day',
    experience: 'intermediate'
};

const filteredTours = filterHorseRidingTours(tours, preferences);
console.log(filteredTours);
*/
```
