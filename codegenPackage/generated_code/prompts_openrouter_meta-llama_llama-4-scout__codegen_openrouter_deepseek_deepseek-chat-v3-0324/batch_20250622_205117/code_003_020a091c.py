"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Develop a JavaScript function to implement a "throwback" playlist feature, similar to the "S2 Throwback" playlist on Radio S.
Generated: DETERMINISTIC_020a091c38d878fd
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates a throwback playlist based on the given criteria.
 * 
 * @param {Array} songs - Array of song objects with properties: title, artist, year, genre, popularity
 * @param {number} yearsAgo - Number of years to look back for throwback songs
 * @param {number} minPopularity - Minimum popularity score (0-100) for songs to include
 * @param {number} maxSongs - Maximum number of songs to include in the playlist
 * @returns {Array} Array of song objects sorted by popularity (descending)
 * @throws {Error} If invalid input parameters are provided
 */
function generateThrowbackPlaylist(songs, yearsAgo = 10, minPopularity = 70, maxSongs = 30) {
    // Input validation
    if (!Array.isArray(songs)) {
        throw new Error('Songs must be an array');
    }
    if (typeof yearsAgo !== 'number' || yearsAgo <= 0) {
        throw new Error('yearsAgo must be a positive number');
    }
    if (typeof minPopularity !== 'number' || minPopularity < 0 || minPopularity > 100) {
        throw new Error('minPopularity must be between 0 and 100');
    }
    if (typeof maxSongs !== 'number' || maxSongs <= 0) {
        throw new Error('maxSongs must be a positive number');
    }

    const currentYear = new Date().getFullYear();
    const targetYear = currentYear - yearsAgo;

    // Filter songs from the target year with sufficient popularity
    const throwbackSongs = songs.filter(song => {
        if (!song || typeof song !== 'object') return false;
        
        const hasRequiredFields = song.title && song.artist && song.year && song.popularity;
        if (!hasRequiredFields) return false;

        return song.year === targetYear && song.popularity >= minPopularity;
    });

    // Sort by popularity (descending)
    throwbackSongs.sort((a, b) => b.popularity - a.popularity);

    // Limit to maxSongs
    return throwbackSongs.slice(0, maxSongs);
}

// Example usage:
/*
const allSongs = [
    { title: "Song A", artist: "Artist 1", year: 2013, genre: "Pop", popularity: 85 },
    { title: "Song B", artist: "Artist 2", year: 2013, genre: "Rock", popularity: 72 },
    { title: "Song C", artist: "Artist 3", year: 2020, genre: "Hip Hop", popularity: 90 },
    { title: "Song D", artist: "Artist 4", year: 2013, genre: "Pop", popularity: 65 }
];

const throwbackPlaylist = generateThrowbackPlaylist(allSongs, 10, 70, 5);
console.log(throwbackPlaylist);
*/
```
