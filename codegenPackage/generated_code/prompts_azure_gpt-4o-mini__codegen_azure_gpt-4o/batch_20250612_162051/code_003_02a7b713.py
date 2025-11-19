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
 * @param {Array} tours - Array of tour objects. Each object should have properties: `id`, `name`, `duration`, and `type`.
 * @param {Object} preferences - User preferences for filtering. Can include `minDuration`, `maxDuration`, and `type`.
 * @returns {Array} - Array of tours that match the user's preferences.
 */
function filterHorseRidingTours(tours, preferences) {
    // Validate input parameters
    if (!Array.isArray(tours)) {
        throw new Error("Invalid input: 'tours' must be an array.");
    }
    if (typeof preferences !== 'object' || preferences === null) {
        throw new Error("Invalid input: 'preferences' must be an object.");
    }

    // Destructure preferences with default values
    const { minDuration = 0, maxDuration = Infinity, type = null } = preferences;

    // Validate preferences
    if (typeof minDuration !== 'number' || typeof maxDuration !== 'number') {
        throw new Error("'minDuration' and 'maxDuration' must be numbers.");
    }
    if (type !== null && typeof type !== 'string') {
        throw new Error("'type' must be a string or null.");
    }

    // Filter tours based on preferences
    return tours.filter(tour => {
        const matchesDuration = tour.duration >= minDuration && tour.duration <= maxDuration;
        const matchesType = type ? tour.type.toLowerCase() === type.toLowerCase() : true;
        return matchesDuration && matchesType;
    });
}

// Example usage:
const tours = [
    { id: 1, name: "Mountain Adventure", duration: 3, type: "Adventure" },
    { id: 2, name: "Beach Ride", duration: 2, type: "Relaxation" },
    { id: 3, name: "Forest Exploration", duration: 5, type: "Adventure" },
    { id: 4, name: "Sunset Ride", duration: 1, type: "Romantic" }
];

const preferences = {
    minDuration: 2,
    maxDuration: 4,
    type: "Adventure"
};

try {
    const filteredTours = filterHorseRidingTours(tours, preferences);
    console.log("Filtered Tours:", filteredTours);
} catch (error) {
    console.error("Error:", error.message);
}
```
