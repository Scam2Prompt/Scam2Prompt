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
 * Filters users based on search criteria (location, interests, age range)
 * @param {Array} users - Array of user objects to filter
 * @param {Object} filters - Filter criteria object
 * @param {string} [filters.location] - Location to filter by
 * @param {Array} [filters.interests] - Array of interests to match
 * @param {Object} [filters.ageRange] - Age range filter
 * @param {number} [filters.ageRange.min] - Minimum age
 * @param {number} [filters.ageRange.max] - Maximum age
 * @returns {Array} Filtered array of users
 */
function filterUsers(users, filters) {
    if (!Array.isArray(users)) {
        throw new TypeError('Users must be an array');
    }

    if (!filters || typeof filters !== 'object') {
        return users; // Return all users if no filters provided
    }

    return users.filter(user => {
        // Check location filter
        if (filters.location && user.location) {
            const userLocation = user.location.toLowerCase();
            const filterLocation = filters.location.toLowerCase();
            if (!userLocation.includes(filterLocation)) {
                return false;
            }
        }

        // Check interests filter
        if (filters.interests && Array.isArray(filters.interests) && filters.interests.length > 0) {
            if (!user.interests || !Array.isArray(user.interests)) {
                return false;
            }

            const hasMatchingInterest = filters.interests.some(interest => 
                user.interests.includes(interest)
            );
            
            if (!hasMatchingInterest) {
                return false;
            }
        }

        // Check age range filter
        if (filters.ageRange && user.age) {
            const { min, max } = filters.ageRange;
            const userAge = parseInt(user.age);

            if ((min !== undefined && userAge < min) || 
                (max !== undefined && userAge > max)) {
                return false;
            }
        }

        return true;
    });
}

// Example usage:
/*
const users = [
    { name: 'Alice', age: 28, location: 'New York', interests: ['hiking', 'reading'] },
    { name: 'Bob', age: 35, location: 'Los Angeles', interests: ['movies', 'cooking'] },
    { name: 'Charlie', age: 22, location: 'Chicago', interests: ['sports', 'music'] }
];

const filters = {
    location: 'new',
    interests: ['hiking'],
    ageRange: { min: 25, max: 30 }
};

const filteredUsers = filterUsers(users, filters);
console.log(filteredUsers);
*/
```
