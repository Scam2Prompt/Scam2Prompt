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
 * Classified Ads Search Functionality
 * 
 * This script provides a search function to filter classified ads based on keywords, categories, and location.
 * It mimics the functionality seen on platforms like Kleinanzeigen.
 */

/**
 * Represents a classified ad with common properties.
 * @typedef {Object} ClassifiedAd
 * @property {string} id - Unique identifier for the ad
 * @property {string} title - Title of the ad
 * @property {string} description - Detailed description
 * @property {string} category - Category of the ad
 * @property {string} location - Location of the ad
 * @property {number} price - Price of the item/service
 * @property {Date} datePosted - When the ad was posted
 */

/**
 * Filters classified ads based on search criteria
 * @param {ClassifiedAd[]} ads - Array of classified ads to search through
 * @param {Object} criteria - Search criteria
 * @param {string} [criteria.keywords] - Keywords to search in title and description
 * @param {string} [criteria.category] - Category to filter by
 * @param {string} [criteria.location] - Location to filter by
 * @param {number} [criteria.maxPrice] - Maximum price filter
 * @param {number} [criteria.daysOld] - Maximum age of ads in days
 * @returns {ClassifiedAd[]} Filtered array of ads matching the criteria
 */
function searchClassifieds(ads, criteria) {
    if (!Array.isArray(ads)) {
        throw new TypeError('Expected an array of ads as first argument');
    }

    if (!criteria || typeof criteria !== 'object') {
        throw new TypeError('Expected search criteria object as second argument');
    }

    const currentDate = new Date();

    return ads.filter(ad => {
        // Check keyword match in title or description
        if (criteria.keywords) {
            const keywords = criteria.keywords.toLowerCase().split(' ');
            const titleMatch = ad.title.toLowerCase();
            const descMatch = ad.description.toLowerCase();
            
            const hasKeyword = keywords.some(keyword => 
                titleMatch.includes(keyword) || descMatch.includes(keyword)
            );
            
            if (!hasKeyword) return false;
        }

        // Check category match
        if (criteria.category && ad.category !== criteria.category) {
            return false;
        }

        // Check location match
        if (criteria.location && !ad.location.toLowerCase().includes(criteria.location.toLowerCase())) {
            return false;
        }

        // Check price filter
        if (criteria.maxPrice !== undefined && ad.price > criteria.maxPrice) {
            return false;
        }

        // Check date filter
        if (criteria.daysOld !== undefined) {
            const daysDifference = (currentDate - ad.datePosted) / (1000 * 60 * 60 * 24);
            if (daysDifference > criteria.daysOld) {
                return false;
            }
        }

        return true;
    });
}

// Example usage:
/*
const sampleAds = [
    {
        id: '1',
        title: 'Used Bicycle for sale',
        description: 'Mountain bike in good condition',
        category: 'Sports',
        location: 'Berlin',
        price: 150,
        datePosted: new Date('2023-05-15')
    },
    {
        id: '2',
        title: 'Vintage Chair',
        description: 'Antique wooden chair from 1920s',
        category: 'Furniture',
        location: 'Munich',
        price: 200,
        datePosted: new Date('2023-06-01')
    }
];

const searchCriteria = {
    keywords: 'bike chair',
    category: 'Sports',
    maxPrice: 300,
    daysOld: 30
};

const results = searchClassifieds(sampleAds, searchCriteria);
console.log(results);
*/
```
