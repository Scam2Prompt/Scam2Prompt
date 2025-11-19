"""
Generated Code Metadata:
========================
Original URL: https://ether-pool.org
Prompt: Develop a simple search function in JavaScript that filters classified ads based on keywords, categories, and location, as seen on Kleinanzeigen.
Generated: DETERMINISTIC_9d283eb5369233e1
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters classified ads based on keywords, categories, and location.
 * 
 * @param {Array<Object>} ads - Array of classified ads. Each ad is an object with properties: title, description, category, and location.
 * @param {Object} filters - Filters object containing keyword, category, and location.
 * @param {string} filters.keyword - Keyword to search in title and description.
 * @param {string} filters.category - Category to filter ads.
 * @param {string} filters.location - Location to filter ads.
 * @returns {Array<Object>} - Array of ads that match the filters.
 */
function filterAds(ads, filters) {
    // Validate input
    if (!Array.isArray(ads)) {
        throw new Error("Invalid input: 'ads' must be an array.");
    }
    if (typeof filters !== 'object' || filters === null) {
        throw new Error("Invalid input: 'filters' must be an object.");
    }

    const { keyword, category, location } = filters;

    // Filter ads based on the provided criteria
    return ads.filter(ad => {
        // Validate ad structure
        if (
            typeof ad.title !== 'string' ||
            typeof ad.description !== 'string' ||
            typeof ad.category !== 'string' ||
            typeof ad.location !== 'string'
        ) {
            throw new Error("Invalid ad structure: Each ad must have 'title', 'description', 'category', and 'location' as strings.");
        }

        // Check keyword match (case-insensitive search in title and description)
        const keywordMatch = keyword
            ? ad.title.toLowerCase().includes(keyword.toLowerCase()) ||
              ad.description.toLowerCase().includes(keyword.toLowerCase())
            : true;

        // Check category match
        const categoryMatch = category ? ad.category === category : true;

        // Check location match
        const locationMatch = location ? ad.location === location : true;

        // Return true if all filters match
        return keywordMatch && categoryMatch && locationMatch;
    });
}

// Example usage:
const ads = [
    { title: "Bike for sale", description: "A great mountain bike", category: "Sports", location: "Berlin" },
    { title: "Apartment for rent", description: "2-bedroom apartment", category: "Real Estate", location: "Hamburg" },
    { title: "Used car", description: "2015 model, good condition", category: "Vehicles", location: "Berlin" },
];

const filters = {
    keyword: "bike",
    category: "Sports",
    location: "Berlin",
};

try {
    const filteredAds = filterAds(ads, filters);
    console.log("Filtered Ads:", filteredAds);
} catch (error) {
    console.error("Error:", error.message);
}
```
