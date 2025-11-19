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
 * Filters job offers based on specific keywords and locations.
 * 
 * @param {Array<Object>} jobOffers - Array of job offers. Each offer should be an object containing keys like `title`, `description`, and `location`.
 * @param {Array<string>} keywords - Array of keywords used for filtering (e.g., ["developer", "remote"]).
 * @param {Array<string>} locations - Array of preferred locations (e.g., ["New York", "San Francisco"]).
 * @returns {Array<Object>} - Array of filtered job offers that match the criteria.
 */
function filterJobOffers(jobOffers, keywords, locations) {
    // Validate input parameters
    if (!Array.isArray(jobOffers) || !Array.isArray(keywords) || !Array.isArray(locations)) {
        throw new Error("Invalid input: All inputs must be arrays.");
    }

    // Perform filtering based on keywords and locations
    return jobOffers.filter(offer => {
        if (typeof offer.title !== "string" || typeof offer.description !== "string" || typeof offer.location !== "string") {
            throw new Error("Invalid job offer format: Each job offer must have `title`, `description`, and `location` as strings.");
        }

        // Check if any keyword is present in the title or description
        const matchesKeyword = keywords.some(keyword =>
            offer.title.toLowerCase().includes(keyword.toLowerCase()) ||
            offer.description.toLowerCase().includes(keyword.toLowerCase())
        );

        // Check if location matches any of the preferred locations
        const matchesLocation = locations.some(location =>
            offer.location.toLowerCase() === location.toLowerCase()
        );

        // Include the job offer if it matches at least one keyword and location
        return matchesKeyword && matchesLocation;
    });
}

// Example usage:
const jobOffers = [
    { title: "Software Developer", description: "Looking for a skilled JavaScript developer.", location: "New York" },
    { title: "Data Analyst", description: "Experience with Python and SQL.", location: "San Francisco" },
    { title: "Remote Developer", description: "Fully remote position for a full-stack developer.", location: "Remote" },
];

const keywords = ["developer", "remote"];
const locations = ["New York", "Remote"];

try {
    const filteredOffers = filterJobOffers(jobOffers, keywords, locations);
    console.log("Filtered Job Offers:", filteredOffers);
} catch (error) {
    console.error("Error:", error.message);
}
```
