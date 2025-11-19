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
 * Filters job offers based on specified keywords and locations.
 * 
 * @param {Array<Object>} jobOffers - An array of job offer objects.
 * @param {Array<string>} keywords - An array of keywords to filter job titles and descriptions.
 * @param {Array<string>} locations - An array of locations to filter job offers.
 * @returns {Array<Object>} - An array of filtered job offers that match the keywords and locations.
 * 
 * @throws {TypeError} - Throws an error if jobOffers is not an array or if keywords/locations are not arrays.
 */
function filterJobOffers(jobOffers, keywords, locations) {
    // Validate input types
    if (!Array.isArray(jobOffers)) {
        throw new TypeError('Expected jobOffers to be an array.');
    }
    if (!Array.isArray(keywords)) {
        throw new TypeError('Expected keywords to be an array.');
    }
    if (!Array.isArray(locations)) {
        throw new TypeError('Expected locations to be an array.');
    }

    // Convert keywords and locations to lowercase for case-insensitive matching
    const lowerCaseKeywords = keywords.map(keyword => keyword.toLowerCase());
    const lowerCaseLocations = locations.map(location => location.toLowerCase());

    // Filter job offers based on keywords and locations
    return jobOffers.filter(job => {
        const jobTitle = job.title.toLowerCase();
        const jobDescription = job.description.toLowerCase();
        const jobLocation = job.location.toLowerCase();

        // Check if any keyword matches the job title or description
        const matchesKeywords = lowerCaseKeywords.some(keyword => 
            jobTitle.includes(keyword) || jobDescription.includes(keyword)
        );

        // Check if the job location matches any of the specified locations
        const matchesLocation = lowerCaseLocations.includes(jobLocation);

        // Return true if both conditions are met
        return matchesKeywords && matchesLocation;
    });
}

// Example usage
const jobOffers = [
    { title: 'Software Engineer', description: 'Develop web applications', location: 'New York' },
    { title: 'Data Scientist', description: 'Analyze data and build models', location: 'San Francisco' },
    { title: 'Frontend Developer', description: 'Create user interfaces', location: 'New York' },
];

const keywords = ['engineer', 'developer'];
const locations = ['new york'];

try {
    const filteredOffers = filterJobOffers(jobOffers, keywords, locations);
    console.log(filteredOffers);
} catch (error) {
    console.error('Error filtering job offers:', error.message);
}
```
