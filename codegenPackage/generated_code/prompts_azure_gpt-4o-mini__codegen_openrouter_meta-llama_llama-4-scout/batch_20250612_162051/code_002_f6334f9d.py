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
 * Filters job offers based on specific keywords and locations.
 * 
 * @param {Object[]} jobOffers - An array of job offer objects.
 * @param {string[]} keywords - An array of keywords to filter by.
 * @param {string[]} locations - An array of locations to filter by.
 * @returns {Object[]} An array of filtered job offers.
 */
function filterJobOffers(jobOffers, keywords, locations) {
    // Check if jobOffers is an array
    if (!Array.isArray(jobOffers)) {
        throw new Error('Job offers must be an array');
    }

    // Check if keywords and locations are arrays
    if (!Array.isArray(keywords) || !Array.isArray(locations)) {
        throw new Error('Keywords and locations must be arrays');
    }

    // Filter job offers based on keywords and locations
    return jobOffers.filter(job => {
        // Check if job offer title or description contains any of the keywords
        const keywordMatch = keywords.some(keyword => 
            job.title.toLowerCase().includes(keyword.toLowerCase()) || 
            job.description.toLowerCase().includes(keyword.toLowerCase())
        );

        // Check if job offer location matches any of the locations
        const locationMatch = locations.some(location => 
            job.location.toLowerCase().includes(location.toLowerCase())
        );

        // Return true if both keyword and location match, or if no filters are applied
        return (keywords.length === 0 || keywordMatch) && (locations.length === 0 || locationMatch);
    });
}

// Example usage:
const jobOffers = [
    { title: 'Software Engineer', description: 'Develop software applications', location: 'New York' },
    { title: 'Data Scientist', description: 'Analyze data and build models', location: 'San Francisco' },
    { title: 'Product Manager', description: 'Manage product development', location: 'New York' },
];

const keywords = ['software', 'data'];
const locations = ['New York'];

try {
    const filteredJobOffers = filterJobOffers(jobOffers, keywords, locations);
    console.log(filteredJobOffers);
} catch (error) {
    console.error(error.message);
}
```
