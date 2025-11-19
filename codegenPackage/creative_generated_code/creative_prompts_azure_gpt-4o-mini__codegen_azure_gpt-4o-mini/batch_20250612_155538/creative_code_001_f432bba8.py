"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hianime.baby
Prompt: Write a JavaScript function that filters anime titles by genre on the HiAnime platform, ensuring a user-friendly interface.
Generated: DETERMINISTIC_f432bba8cb9aec8f
Batch ID: 20250612_155538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters anime titles by genre on the HiAnime platform.
 * 
 * @param {Array} animeList - The list of anime objects to filter.
 * @param {string} selectedGenre - The genre to filter by (case-sensitive).
 * @returns {Array} - An array of anime objects that match the selected genre.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function filterAnimeByGenre(animeList, selectedGenre) {
    // Validate input parameters
    if (!Array.isArray(animeList)) {
        throw new Error('animeList must be an array');
    }
    if (typeof selectedGenre !== 'string') {
        throw new Error('selectedGenre must be a string');
    }

    // Filter the anime list by the selected genre
    const filteredAnime = animeList.filter(anime => {
        // Check if the anime has a genres property
        if (!anime.genres || !Array.isArray(anime.genres)) {
            return false; // Skip if genres is not defined or not an array
        }
        // Return true if the selected genre is found in the anime's genres
        return anime.genres.includes(selectedGenre);
    });

    return filteredAnime;
}

// Example usage
try {
    const animeList = [
        { title: 'My Hero Academia', genres: ['Action', 'Adventure'] },
        { title: 'Death Note', genres: ['Mystery', 'Psychological'] },
        { title: 'Attack on Titan', genres: ['Action', 'Drama'] },
        { title: 'Fruits Basket', genres: ['Romance', 'Drama'] },
    ];
    
    const selectedGenre = 'Action';
    const actionAnime = filterAnimeByGenre(animeList, selectedGenre);
    console.log('Filtered Anime:', actionAnime);
} catch (error) {
    console.error('Error filtering anime:', error.message);
}
```
