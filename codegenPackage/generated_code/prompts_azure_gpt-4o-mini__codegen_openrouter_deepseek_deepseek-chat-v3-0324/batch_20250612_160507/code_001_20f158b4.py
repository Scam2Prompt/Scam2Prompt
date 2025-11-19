"""
Generated Code Metadata:
========================
Original URL: https://wazfnynow.com
Prompt: Write a JavaScript function that filters job postings on the وظفني الان site by job type and location.
Generated: DETERMINISTIC_20f158b48ba5883d
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters job postings by job type and location on the وظفني الان site.
 * @param {Array} jobPostings - Array of job posting objects to filter.
 * @param {string} jobType - The type of job to filter by (e.g., 'full-time', 'part-time').
 * @param {string} location - The location to filter by (e.g., 'Riyadh', 'Jeddah').
 * @returns {Array} Filtered array of job postings matching the criteria.
 * @throws {Error} If jobPostings is not an array or if required filters are missing.
 */
function filterJobPostings(jobPostings, jobType, location) {
    // Validate input parameters
    if (!Array.isArray(jobPostings)) {
        throw new Error('jobPostings must be an array');
    }
    if (!jobType && !location) {
        throw new Error('At least one filter (jobType or location) must be provided');
    }

    // Normalize filter values for case-insensitive comparison
    const normalizedJobType = jobType ? jobType.toLowerCase().trim() : null;
    const normalizedLocation = location ? location.toLowerCase().trim() : null;

    return jobPostings.filter(posting => {
        // Check if posting has required properties
        if (!posting.type || !posting.location) {
            console.warn('Job posting is missing type or location property:', posting);
            return false;
        }

        // Normalize posting values for comparison
        const postingType = posting.type.toLowerCase().trim();
        const postingLocation = posting.location.toLowerCase().trim();

        // Apply filters
        const typeMatch = normalizedJobType ? postingType.includes(normalizedJobType) : true;
        const locationMatch = normalizedLocation ? postingLocation.includes(normalizedLocation) : true;

        return typeMatch && locationMatch;
    });
}

// Example usage:
/*
const jobPostings = [
    { id: 1, title: 'Software Engineer', type: 'Full-time', location: 'Riyadh' },
    { id: 2, title: 'Data Analyst', type: 'Part-time', location: 'Jeddah' },
    { id: 3, title: 'Project Manager', type: 'Full-time', location: 'Dammam' }
];

const filteredJobs = filterJobPostings(jobPostings, 'full-time', 'Riyadh');
console.log(filteredJobs);
*/
```
