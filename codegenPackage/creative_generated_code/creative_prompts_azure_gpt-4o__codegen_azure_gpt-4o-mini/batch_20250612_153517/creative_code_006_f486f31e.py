"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Write code in JavaScript to implement a search feature that allows users to find schools offering specific extracurricular activities, such as "Tot Hop" or "Active Athletes," based on the Endeavor Schools Plus site.
Generated: DETERMINISTIC_f486f31e21e01aa5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SchoolSearch.js

/**
 * Represents a school.
 * @class
 */
class School {
    constructor(name, activities) {
        this.name = name; // Name of the school
        this.activities = activities; // Array of extracurricular activities
    }
}

/**
 * School search functionality to find schools based on extracurricular activities.
 * @class
 */
class SchoolSearch {
    constructor(schools) {
        this.schools = schools; // Array of School objects
    }

    /**
     * Searches for schools offering a specific extracurricular activity.
     * @param {string} activity - The activity to search for.
     * @returns {School[]} - An array of schools offering the specified activity.
     * @throws {Error} - Throws an error if the input is not valid.
     */
    searchByActivity(activity) {
        if (typeof activity !== 'string' || activity.trim() === '') {
            throw new Error('Invalid activity name. Please provide a valid string.');
        }

        const lowerCasedActivity = activity.toLowerCase();

        // Filter schools based on the provided activity
        const results = this.schools.filter(school => 
            school.activities.map(act => act.toLowerCase()).includes(lowerCasedActivity)
        );

        return results;
    }
}

// Example school data setup
const schools = [
    new School('Endeavor Academy', ['Tot Hop', 'Active Athletes']),
    new School('Bright Future School', ['Art Club', 'Science Fair']),
    new School('Creative Minds Academy', ['Tot Hop', 'Dance']),
    new School('Active Learners Institute', ['Active Athletes', 'Robotics']),
];

// Initialize the search feature with the school data
const schoolSearch = new SchoolSearch(schools);

// Example search function
try {
    const activityToSearch = 'Tot Hop'; // Change this to search for different activities
    const foundSchools = schoolSearch.searchByActivity(activityToSearch);

    // Display results
    if (foundSchools.length > 0) {
        console.log(`Schools offering "${activityToSearch}":`);
        foundSchools.forEach(school => console.log(`- ${school.name}`));
    } else {
        console.log(`No schools found offering "${activityToSearch}".`);
    }
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
