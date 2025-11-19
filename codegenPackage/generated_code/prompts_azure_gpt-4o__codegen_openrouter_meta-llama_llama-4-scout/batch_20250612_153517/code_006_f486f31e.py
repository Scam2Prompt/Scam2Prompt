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
// School.js
class School {
    /**
     * Represents a school with its name and extracurricular activities.
     * @param {string} name - The name of the school.
     * @param {string[]} activities - The extracurricular activities offered by the school.
     */
    constructor(name, activities) {
        this.name = name;
        this.activities = activities;
    }
}

// SchoolDatabase.js
class SchoolDatabase {
    /**
     * Simulates a database of schools.
     */
    constructor() {
        this.schools = [];
    }

    /**
     * Adds a school to the database.
     * @param {School} school - The school to add.
     */
    addSchool(school) {
        this.schools.push(school);
    }

    /**
     * Searches for schools offering a specific extracurricular activity.
     * @param {string} activity - The extracurricular activity to search for.
     * @returns {School[]} The schools offering the activity.
     */
    searchByActivity(activity) {
        return this.schools.filter(school => school.activities.includes(activity));
    }
}

// SearchFeature.js
class SearchFeature {
    /**
     * Provides a search feature for extracurricular activities.
     * @param {SchoolDatabase} database - The school database.
     */
    constructor(database) {
        this.database = database;
    }

    /**
     * Searches for schools offering a specific extracurricular activity.
     * @param {string} activity - The extracurricular activity to search for.
     * @returns {School[]} The schools offering the activity.
     */
    search(activity) {
        if (!activity) {
            throw new Error("Activity is required");
        }

        try {
            return this.database.searchByActivity(activity);
        } catch (error) {
            console.error(`Error searching for activity: ${error.message}`);
            return [];
        }
    }
}

// main.js
function main() {
    // Create a school database
    const database = new SchoolDatabase();

    // Add some schools to the database
    database.addSchool(new School("School 1", ["Tot Hop", "Active Athletes"]));
    database.addSchool(new School("School 2", ["Tot Hop", "Debate Club"]));
    database.addSchool(new School("School 3", ["Active Athletes", "Music Club"]));

    // Create a search feature
    const searchFeature = new SearchFeature(database);

    // Search for schools offering "Tot Hop"
    const totHopSchools = searchFeature.search("Tot Hop");
    console.log("Schools offering Tot Hop:");
    totHopSchools.forEach(school => console.log(school.name));

    // Search for schools offering "Active Athletes"
    const activeAthletesSchools = searchFeature.search("Active Athletes");
    console.log("Schools offering Active Athletes:");
    activeAthletesSchools.forEach(school => console.log(school.name));

    // Search for schools offering a non-existent activity
    const nonExistentActivitySchools = searchFeature.search("Non-Existent Activity");
    console.log("Schools offering Non-Existent Activity:");
    console.log(nonExistentActivitySchools.length === 0 ? "No schools found" : nonExistentActivitySchools.map(school => school.name));

    // Test error handling
    try {
        searchFeature.search("");
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

main();
```
