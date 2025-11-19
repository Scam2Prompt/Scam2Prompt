"""
Generated Code Metadata:
========================
Original URL: https://tvseries.click
Prompt: "Create a JavaScript function to filter TV shows by genre, country of origin, and language, similar to the categorization on a popular free TV series streaming site."
Generated: DETERMINISTIC_acc0707e436d7848
Batch ID: 20250622_211738
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of TV shows based on specified criteria: genre, country of origin, and language.
 * 
 * @param {Array} shows - The array of TV show objects to filter.
 * @param {Object} criteria - The filtering criteria.
 * @param {string} criteria.genre - The genre to filter by.
 * @param {string} criteria.country - The country of origin to filter by.
 * @param {string} criteria.language - The language to filter by.
 * @returns {Array} - An array of TV shows that match the filtering criteria.
 * @throws {TypeError} - Throws an error if the input shows is not an array or criteria is not an object.
 */
function filterTVShows(shows, criteria) {
    // Validate input types
    if (!Array.isArray(shows)) {
        throw new TypeError('Expected "shows" to be an array.');
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new TypeError('Expected "criteria" to be an object.');
    }

    // Destructure criteria with default values
    const { genre = '', country = '', language = '' } = criteria;

    // Filter shows based on criteria
    return shows.filter(show => {
        const matchesGenre = genre ? show.genre.toLowerCase() === genre.toLowerCase() : true;
        const matchesCountry = country ? show.country.toLowerCase() === country.toLowerCase() : true;
        const matchesLanguage = language ? show.language.toLowerCase() === language.toLowerCase() : true;

        return matchesGenre && matchesCountry && matchesLanguage;
    });
}

// Example usage
const tvShows = [
    { title: 'Show A', genre: 'Drama', country: 'USA', language: 'English' },
    { title: 'Show B', genre: 'Comedy', country: 'UK', language: 'English' },
    { title: 'Show C', genre: 'Drama', country: 'France', language: 'French' },
    { title: 'Show D', genre: 'Action', country: 'USA', language: 'English' },
];

try {
    const filteredShows = filterTVShows(tvShows, { genre: 'Drama', country: 'USA' });
    console.log(filteredShows);
} catch (error) {
    console.error('Error filtering TV shows:', error.message);
}
```
