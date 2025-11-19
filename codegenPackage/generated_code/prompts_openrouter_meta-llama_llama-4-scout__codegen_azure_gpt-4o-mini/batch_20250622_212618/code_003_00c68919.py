"""
Generated Code Metadata:
========================
Original URL: https://poligon.store
Prompt: Create a JavaScript code snippet for implementing a search function that filters users based on parameters like location, interests, and age, similar to Mamba's search feature.
Generated: DETERMINISTIC_00c68919264d08ea
Batch ID: 20250622_212618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// User Search Functionality
// This function filters a list of users based on location, interests, and age criteria.

class User {
    constructor(name, age, location, interests) {
        this.name = name;
        this.age = age;
        this.location = location;
        this.interests = interests;
    }
}

/**
 * Filters users based on the provided search criteria.
 * @param {Array<User>} users - The array of user objects to filter.
 * @param {Object} criteria - The search criteria object.
 * @param {string} criteria.location - The location to filter by.
 * @param {Array<string>} criteria.interests - The interests to filter by.
 * @param {number} criteria.minAge - The minimum age to filter by.
 * @param {number} criteria.maxAge - The maximum age to filter by.
 * @returns {Array<User>} - The filtered array of users.
 */
function filterUsers(users, criteria) {
    // Validate input
    if (!Array.isArray(users)) {
        throw new Error("The users parameter must be an array.");
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error("The criteria parameter must be a valid object.");
    }

    return users.filter(user => {
        const matchesLocation = criteria.location ? user.location === criteria.location : true;
        const matchesInterests = criteria.interests && criteria.interests.length > 0 
            ? criteria.interests.some(interest => user.interests.includes(interest)) 
            : true;
        const matchesAge = (criteria.minAge ? user.age >= criteria.minAge : true) &&
                           (criteria.maxAge ? user.age <= criteria.maxAge : true);

        return matchesLocation && matchesInterests && matchesAge;
    });
}

// Example usage
const users = [
    new User("Alice", 25, "New York", ["music", "art"]),
    new User("Bob", 30, "Los Angeles", ["sports", "music"]),
    new User("Charlie", 22, "New York", ["art", "travel"]),
    new User("David", 35, "Chicago", ["sports", "cooking"]),
];

const searchCriteria = {
    location: "New York",
    interests: ["art"],
    minAge: 20,
    maxAge: 30
};

try {
    const filteredUsers = filterUsers(users, searchCriteria);
    console.log("Filtered Users:", filteredUsers);
} catch (error) {
    console.error("Error filtering users:", error.message);
}
```
