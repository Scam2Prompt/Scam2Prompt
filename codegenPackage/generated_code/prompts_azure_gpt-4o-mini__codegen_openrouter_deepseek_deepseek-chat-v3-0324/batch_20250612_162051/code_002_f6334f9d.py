"""
Generated Code Metadata:
========================
Original URL: https://searchhr.com.ar
Prompt: Write a function in JavaScript that filters job offers based on specific keywords and locations, inspired by the features of Search HR.
Generated: DETERMINISTIC_f6334f9d8a083d7a
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
 * Filters job offers based on keywords and locations.
 * @param {Array} jobs - Array of job offer objects to filter.
 * @param {Object} filters - Filter criteria containing keywords and locations.
 * @param {Array} [filters.keywords=[]] - Keywords to search in job titles and descriptions.
 * @param {Array} [filters.locations=[]] - Locations to match against job locations.
 * @returns {Array} Filtered array of job offers.
 * @throws {Error} If jobs parameter is not an array or filters is not an object.
 */
function filterJobOffers(jobs, filters) {
    // Validate input parameters
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs parameter must be an array');
    }
    if (typeof filters !== 'object' || filters === null) {
        throw new Error('Filters parameter must be an object');
    }

    // Set default values for filters if not provided
    const { keywords = [], locations = [] } = filters;

    // Validate filter arrays
    if (!Array.isArray(keywords) || !Array.isArray(locations)) {
        throw new Error('Keywords and locations must be arrays');
    }

    return jobs.filter(job => {
        // Check if job matches all criteria
        const matchesKeywords = keywords.length === 0 || 
            keywords.some(keyword => 
                (job.title && job.title.toLowerCase().includes(keyword.toLowerCase())) ||
                (job.description && job.description.toLowerCase().includes(keyword.toLowerCase()))
            );

        const matchesLocations = locations.length === 0 ||
            locations.some(location => 
                job.location && job.location.toLowerCase().includes(location.toLowerCase())
            );

        return matchesKeywords && matchesLocations;
    });
}

// Example usage:
/*
const jobs = [
    { title: 'Frontend Developer', description: 'React experience required', location: 'New York' },
    { title: 'Backend Engineer', description: 'Node.js and database skills', location: 'Remote' },
    { title: 'Full Stack Developer', description: 'JavaScript and Python experience', location: 'San Francisco' }
];

const filteredJobs = filterJobOffers(jobs, {
    keywords: ['developer', 'javascript'],
    locations: ['New York', 'Remote']
});

console.log(filteredJobs);
*/
```
