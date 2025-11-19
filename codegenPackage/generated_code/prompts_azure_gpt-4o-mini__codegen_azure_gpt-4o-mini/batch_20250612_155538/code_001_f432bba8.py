"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Write a JavaScript function that filters anime titles by genre on the HiAnime platform, ensuring a user-friendly interface.
Generated: DETERMINISTIC_f432bba8cb9aec8f
Batch ID: 20250612_155538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters anime titles by genre on the HiAnime platform.
 * 
 * @param {Array} animeList - An array of anime objects to filter.
 * @param {string} genre - The genre to filter the anime titles by.
 * @returns {Array} - An array of anime titles that match the specified genre.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterAnimeByGenre(animeList, genre) {
    // Validate input parameters
    if (!Array.isArray(animeList)) {
        throw new Error('Invalid input: animeList must be an array.');
    }
    if (typeof genre !== 'string') {
        throw new Error('Invalid input: genre must be a string.');
    }

    // Filter the anime list based on the specified genre
    const filteredAnime = animeList.filter(anime => {
        // Check if the anime has a genres property and if it includes the specified genre
        return anime.genres && Array.isArray(anime.genres) && anime.genres.includes(genre);
    });

    // Return the filtered list of anime titles
    return filteredAnime.map(anime => anime.title);
}

// Example usage
try {
    const animeList = [
        { title: 'Attack on Titan', genres: ['Action', 'Drama'] },
        { title: 'My Hero Academia', genres: ['Action', 'Superhero'] },
        { title: 'Your Name', genres: ['Romance', 'Drama'] },
        { title: 'One Piece', genres: ['Adventure', 'Action'] }
    ];

    const genreToFilter = 'Action';
    const actionAnimeTitles = filterAnimeByGenre(animeList, genreToFilter);
    console.log('Filtered Anime Titles:', actionAnimeTitles);
} catch (error) {
    console.error('Error:', error.message);
}
```
