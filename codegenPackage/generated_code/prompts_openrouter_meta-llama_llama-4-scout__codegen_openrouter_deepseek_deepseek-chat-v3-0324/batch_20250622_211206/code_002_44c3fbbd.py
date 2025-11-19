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
/**
 * Community Directory Filtering System
 * 
 * This script provides filtering functionality for a community directory,
 * allowing users to search by profession and location.
 */

// Sample data - in a real application, this would likely come from an API or database
const communityMembers = [
    { name: 'John Doe', profession: 'Artist', location: 'New York' },
    { name: 'Jane Smith', profession: 'Medical', location: 'Los Angeles' },
    { name: 'Bob Johnson', profession: 'Business Owner', location: 'Chicago' },
    { name: 'Alice Williams', profession: 'Artist', location: 'New York' },
    { name: 'Charlie Brown', profession: 'Medical', location: 'Chicago' },
];

/**
 * Filters community members based on profession and location
 * @param {string} profession - Profession to filter by (e.g., 'Artist')
 * @param {string} location - Location to filter by (e.g., 'New York')
 * @returns {Array} Filtered array of community members
 */
function filterMembers(profession = '', location = '') {
    try {
        // Validate inputs
        if (typeof profession !== 'string' || typeof location !== 'string') {
            throw new Error('Profession and location must be strings');
        }

        // Convert inputs to lowercase for case-insensitive comparison
        const professionLower = profession.toLowerCase();
        const locationLower = location.toLowerCase();

        return communityMembers.filter(member => {
            const memberProfession = member.profession.toLowerCase();
            const memberLocation = member.location.toLowerCase();

            // Check if member matches both filters (if provided)
            const professionMatch = professionLower === '' || memberProfession.includes(professionLower);
            const locationMatch = locationLower === '' || memberLocation.includes(locationLower);

            return professionMatch && locationMatch;
        });
    } catch (error) {
        console.error('Error filtering members:', error.message);
        return []; // Return empty array on error
    }
}

/**
 * Displays filtered results in the console
 * @param {Array} results - Array of filtered members
 */
function displayResults(results) {
    if (!Array.isArray(results)) {
        console.error('Invalid results format');
        return;
    }

    if (results.length === 0) {
        console.log('No matching members found');
        return;
    }

    console.log('Filtered Results:');
    results.forEach(member => {
        console.log(`- ${member.name}: ${member.profession} in ${member.location}`);
    });
}

// Example usage:
// const filtered = filterMembers('artist', 'new york');
// displayResults(filtered);

// For browser implementation, you would typically connect this to DOM elements:
document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const professionInput = document.getElementById('profession');
    const locationInput = document.getElementById('location');
    const resultsContainer = document.getElementById('results');

    if (searchForm && professionInput && locationInput && resultsContainer) {
        searchForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const profession = professionInput.value.trim();
            const location = locationInput.value.trim();
            
            const filteredMembers = filterMembers(profession, location);
            
            // Clear previous results
            resultsContainer.innerHTML = '';
            
            if (filteredMembers.length === 0) {
                resultsContainer.innerHTML = '<p>No matching members found</p>';
                return;
            }
            
            // Create and append results
            const resultsList = document.createElement('ul');
            filteredMembers.forEach(member => {
                const item = document.createElement('li');
                item.textContent = `${member.name}: ${member.profession} in ${member.location}`;
                resultsList.appendChild(item);
            });
            
            resultsContainer.appendChild(resultsList);
        });
    }
});
```
