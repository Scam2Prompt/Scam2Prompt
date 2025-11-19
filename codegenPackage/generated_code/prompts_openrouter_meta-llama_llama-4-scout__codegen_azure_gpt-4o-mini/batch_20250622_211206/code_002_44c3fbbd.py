"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: "Generate a code snippet in JavaScript to create a simple filtering system for a community directory, allowing users to search by profession (e.g., 'Artist', 'Medical', 'Business Owner') and location."
Generated: DETERMINISTIC_44c3fbbd6a0f2720
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Community Directory Filtering System

// Sample data representing community members
const communityMembers = [
    { name: 'Alice', profession: 'Artist', location: 'New York' },
    { name: 'Bob', profession: 'Medical', location: 'Los Angeles' },
    { name: 'Charlie', profession: 'Business Owner', location: 'Chicago' },
    { name: 'David', profession: 'Artist', location: 'San Francisco' },
    { name: 'Eve', profession: 'Medical', location: 'New York' },
];

// Function to filter community members by profession and location
/**
 * Filters community members based on the provided profession and location.
 * @param {Array} members - The array of community members to filter.
 * @param {string} profession - The profession to filter by.
 * @param {string} location - The location to filter by.
 * @returns {Array} - An array of filtered community members.
 */
function filterMembers(members, profession, location) {
    try {
        // Validate input parameters
        if (!Array.isArray(members)) {
            throw new TypeError('Expected an array of members.');
        }
        if (typeof profession !== 'string' || typeof location !== 'string') {
            throw new TypeError('Profession and location must be strings.');
        }

        // Filter members based on profession and location
        return members.filter(member => 
            member.profession.toLowerCase() === profession.toLowerCase() &&
            member.location.toLowerCase() === location.toLowerCase()
        );
    } catch (error) {
        console.error('Error filtering members:', error.message);
        return []; // Return an empty array in case of error
    }
}

// Example usage of the filterMembers function
const professionToSearch = 'Artist';
const locationToSearch = 'New York';
const filteredMembers = filterMembers(communityMembers, professionToSearch, locationToSearch);

// Display the filtered results
console.log('Filtered Members:', filteredMembers);
```
