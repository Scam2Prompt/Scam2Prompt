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
/**
 * Filters a list of users based on search criteria.
 * 
 * @param {Array} users - Array of user objects to be filtered. Each user object should have properties: location, interests, and age.
 * @param {Object} criteria - Search criteria object with optional properties: location, interests, and ageRange.
 * @returns {Array} - Array of users that match the search criteria.
 */
function filterUsers(users, criteria) {
    // Validate input
    if (!Array.isArray(users)) {
        throw new Error("Invalid input: 'users' must be an array.");
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error("Invalid input: 'criteria' must be an object.");
    }

    // Destructure criteria with default values
    const { location, interests, ageRange } = criteria;

    // Filter users based on criteria
    return users.filter(user => {
        // Validate user object structure
        if (typeof user !== 'object' || user === null) {
            throw new Error("Invalid user object in 'users' array.");
        }

        // Check location match (if provided)
        const locationMatch = location ? user.location === location : true;

        // Check interests match (if provided)
        const interestsMatch = interests ? interests.some(interest => user.interests.includes(interest)) : true;

        // Check age range match (if provided)
        const ageMatch = ageRange ? user.age >= ageRange.min && user.age <= ageRange.max : true;

        // Return true if all criteria match
        return locationMatch && interestsMatch && ageMatch;
    });
}

// Example usage:
const users = [
    { name: "Alice", location: "New York", interests: ["music", "sports"], age: 25 },
    { name: "Bob", location: "Los Angeles", interests: ["movies", "sports"], age: 30 },
    { name: "Charlie", location: "New York", interests: ["music", "reading"], age: 35 },
];

const criteria = {
    location: "New York",
    interests: ["music"],
    ageRange: { min: 20, max: 30 },
};

try {
    const filteredUsers = filterUsers(users, criteria);
    console.log("Filtered Users:", filteredUsers);
} catch (error) {
    console.error("Error:", error.message);
}
```
