"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Write code in JavaScript to implement a search feature that allows users to find schools offering specific extracurricular activities, such as "Tot Hop" or "Active Athletes," based on the Endeavor Schools Plus site.
Generated: DETERMINISTIC_f486f31e21e01aa5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SchoolSearch.js

/**
 * SchoolSearch class to handle searching for schools based on extracurricular activities.
 */
class SchoolSearch {
    constructor(schools) {
        // Initialize with a list of schools
        this.schools = schools;
    }

    /**
     * Searches for schools offering a specific extracurricular activity.
     * @param {string} activity - The name of the extracurricular activity to search for.
     * @returns {Array} - An array of schools offering the specified activity.
     */
    searchByActivity(activity) {
        // Validate input
        if (typeof activity !== 'string' || activity.trim() === '') {
            throw new Error('Invalid activity name. Please provide a valid string.');
        }

        // Normalize the activity name for case-insensitive comparison
        const normalizedActivity = activity.toLowerCase();

        // Filter schools that offer the specified activity
        const results = this.schools.filter(school => 
            school.activities && school.activities.some(act => 
                act.toLowerCase() === normalizedActivity
            )
        );

        return results;
    }
}

// Example usage
const schools = [
    { name: 'Endeavor Academy', activities: ['Tot Hop', 'Active Athletes'] },
    { name: 'Future Leaders School', activities: ['Art Club', 'Active Athletes'] },
    { name: 'Creative Minds Academy', activities: ['Drama', 'Music'] },
];

// Create an instance of SchoolSearch
const schoolSearch = new SchoolSearch(schools);

// Search for schools offering "Active Athletes"
try {
    const searchResults = schoolSearch.searchByActivity('Active Athletes');
    console.log('Schools offering Active Athletes:', searchResults);
} catch (error) {
    console.error('Error during search:', error.message);
}
```
