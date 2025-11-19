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
 * @param {Array<Object>} tours - Array of tour objects. Each tour object should have `duration`, `experienceType`, and other properties.
 * @param {Object} filters - User preferences for filtering. Supported preferences include `minDuration`, `maxDuration`, and `experienceType`.
 * @returns {Array<Object>} - Array of tours matching the user preferences.
 */
function filterHorseRidingTours(tours, filters) {
  // Validate input parameters
  if (!Array.isArray(tours)) {
    throw new Error("Invalid input: 'tours' must be an array.");
  }
  if (typeof filters !== 'object' || filters === null) {
    throw new Error("Invalid input: 'filters' must be an object.");
  }

  const { minDuration, maxDuration, experienceType } = filters;

  // Filter tours based on user preferences
  return tours.filter(tour => {
    // Ensure the tour has the required properties
    if (typeof tour.duration !== 'number' || typeof tour.experienceType !== 'string') {
      throw new Error("Invalid tour object: Missing required 'duration' or 'experienceType' properties.");
    }

    // Check filters: Duration
    const matchesDuration = 
      (minDuration === undefined || tour.duration >= minDuration) &&
      (maxDuration === undefined || tour.duration <= maxDuration);

    // Check filters: Experience Type
    const matchesExperienceType = 
      experienceType === undefined || tour.experienceType.toLowerCase() === experienceType.toLowerCase();

    // Return true if the tour matches all filters
    return matchesDuration && matchesExperienceType;
  });
}

// Example usage:
try {
  const tours = [
    { id: 1, name: "Mountain Adventure", duration: 3, experienceType: "Adventure" },
    { id: 2, name: "Beach Ride", duration: 2, experienceType: "Relaxation" },
    { id: 3, name: "Forest Trek", duration: 5, experienceType: "Adventure" },
  ];

  const filters = { minDuration: 2, maxDuration: 4, experienceType: "Adventure" };
  
  const filteredTours = filterHorseRidingTours(tours, filters);
  console.log("Filtered Tours:", filteredTours);
} catch (error) {
  console.error("Error filtering tours:", error.message);
}
```
