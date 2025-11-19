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
 * @param {Array<Object>} jobOffers - Array of job offer objects. Each object should have `title`, `description`, and `location` properties.
 * @param {Array<string>} keywords - Array of keywords to filter job offers by. Matches are case-insensitive.
 * @param {Array<string>} locations - Array of locations to filter job offers by. Matches are case-insensitive.
 * @returns {Array<Object>} - Array of job offers that match the specified keywords and locations.
 */
function filterJobOffers(jobOffers, keywords, locations) {
    // Validate input parameters
    if (!Array.isArray(jobOffers) || !Array.isArray(keywords) || !Array.isArray(locations)) {
        throw new Error("Invalid input: jobOffers, keywords, and locations must be arrays.");
    }

    // Normalize keywords and locations for case-insensitive comparison
    const normalizedKeywords = keywords.map(keyword => keyword.toLowerCase());
    const normalizedLocations = locations.map(location => location.toLowerCase());

    // Filter job offers
    return jobOffers.filter(offer => {
        // Validate job offer structure
        if (!offer.title || !offer.description || !offer.location) {
            console.warn("Skipping invalid job offer:", offer);
            return false;
        }

        // Check if the job offer matches any of the keywords
        const matchesKeyword = normalizedKeywords.some(keyword =>
            offer.title.toLowerCase().includes(keyword) ||
            offer.description.toLowerCase().includes(keyword)
        );

        // Check if the job offer matches any of the locations
        const matchesLocation = normalizedLocations.some(location =>
            offer.location.toLowerCase().includes(location)
        );

        // Return true if both conditions are met
        return matchesKeyword && matchesLocation;
    });
}

// Example usage:
const jobOffers = [
    { title: "Software Engineer", description: "Develop web applications", location: "New York" },
    { title: "Data Scientist", description: "Analyze data and build models", location: "San Francisco" },
    { title: "Product Manager", description: "Manage product lifecycle", location: "Remote" }
];

const keywords = ["engineer", "data"];
const locations = ["new york", "san francisco"];

const filteredOffers = filterJobOffers(jobOffers, keywords, locations);
console.log(filteredOffers);
```
