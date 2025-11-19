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
 * Generates a "throwback" playlist based on a given list of songs and a target year range.
 * 
 * @param {Array} songs - An array of song objects. Each object should have the following structure:
 *                        { title: string, artist: string, year: number }
 * @param {number} startYear - The start of the target year range (inclusive).
 * @param {number} endYear - The end of the target year range (inclusive).
 * @param {number} maxSongs - The maximum number of songs to include in the playlist.
 * @returns {Array} - A filtered and shuffled array of song objects representing the throwback playlist.
 */
function generateThrowbackPlaylist(songs, startYear, endYear, maxSongs) {
    // Validate input parameters
    if (!Array.isArray(songs)) {
        throw new Error("Invalid input: 'songs' must be an array.");
    }
    if (typeof startYear !== 'number' || typeof endYear !== 'number' || typeof maxSongs !== 'number') {
        throw new Error("Invalid input: 'startYear', 'endYear', and 'maxSongs' must be numbers.");
    }
    if (startYear > endYear) {
        throw new Error("Invalid input: 'startYear' must be less than or equal to 'endYear'.");
    }
    if (maxSongs <= 0) {
        throw new Error("Invalid input: 'maxSongs' must be greater than 0.");
    }

    // Filter songs based on the target year range
    const filteredSongs = songs.filter(song => {
        return song.year >= startYear && song.year <= endYear;
    });

    // Shuffle the filtered songs using Fisher-Yates algorithm
    for (let i = filteredSongs.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [filteredSongs[i], filteredSongs[j]] = [filteredSongs[j], filteredSongs[i]];
    }

    // Limit the playlist to the specified maximum number of songs
    const playlist = filteredSongs.slice(0, maxSongs);

    return playlist;
}

// Example usage:
const songs = [
    { title: "Song A", artist: "Artist 1", year: 1995 },
    { title: "Song B", artist: "Artist 2", year: 2000 },
    { title: "Song C", artist: "Artist 3", year: 1985 },
    { title: "Song D", artist: "Artist 4", year: 1990 },
    { title: "Song E", artist: "Artist 5", year: 1999 },
];

try {
    const throwbackPlaylist = generateThrowbackPlaylist(songs, 1980, 2000, 3);
    console.log("Throwback Playlist:", throwbackPlaylist);
} catch (error) {
    console.error("Error generating playlist:", error.message);
}
```
