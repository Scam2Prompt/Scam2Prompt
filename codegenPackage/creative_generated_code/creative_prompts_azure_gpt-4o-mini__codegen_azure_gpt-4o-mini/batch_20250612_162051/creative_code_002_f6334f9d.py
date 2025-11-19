"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://searchhr.com.ar
Prompt: Write a function in JavaScript that filters job offers based on specific keywords and locations, inspired by the features of Search HR.
Generated: DETERMINISTIC_f6334f9d8a083d7a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters job offers based on specified keywords and locations.
 *
 * @param {Array<Object>} jobOffers - Array of job offer objects to filter.
 * @param {Array<string>} keywords - Array of keywords to filter job titles/descriptions.
 * @param {Array<string>} locations - Array of locations to filter job offers.
 * @returns {Array<Object>} - An array of filtered job offers that match the criteria.
 */
function filterJobOffers(jobOffers, keywords, locations) {
    try {
        // Check if the input parameters are valid
        if (!Array.isArray(jobOffers) || !Array.isArray(keywords) || !Array.isArray(locations)) {
            throw new TypeError('Invalid input: jobOffers, keywords, and locations must be arrays.');
        }

        // Convert keywords and locations to lower case for case insensitive search
        const lowerCaseKeywords = keywords.map(keyword => keyword.toLowerCase());
        const lowerCaseLocations = locations.map(location => location.toLowerCase());

        // Filter job offers based on keywords and locations
        const filteredOffers = jobOffers.filter(offer => {
            const jobTitleLower = offer.title.toLowerCase();
            const jobDescriptionLower = offer.description.toLowerCase();
            const jobLocationLower = offer.location.toLowerCase();

            // Check for matching keywords and locations
            const matchesKeywords = lowerCaseKeywords.some(keyword => 
                jobTitleLower.includes(keyword) || jobDescriptionLower.includes(keyword)
            );
            const matchesLocation = lowerCaseLocations.includes(jobLocationLower);

            return matchesKeywords && matchesLocation;
        });

        return filteredOffers;
    } catch (error) {
        console.error('Error filtering job offers:', error);
        return []; // Return an empty array on error
    }
}

// Example usage
const jobOffers = [
    { title: 'Software Engineer', description: 'Develop amazing applications', location: 'New York' },
    { title: 'Product Manager', description: 'Lead product development', location: 'San Francisco' },
    { title: 'Data Scientist', description: 'Analyze data and insights', location: 'New York' }
];

const keywords = ['software', 'data'];
const locations = ['new york'];

const filteredOffers = filterJobOffers(jobOffers, keywords, locations);
console.log(filteredOffers);
```
