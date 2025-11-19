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
 * Function to create a "throwback" playlist from a given list of songs.
 * The function filters songs based on a specified year range and returns
 * a new array containing only the songs that fall within that range.
 *
 * @param {Array} songs - An array of song objects, each containing a title, artist, and year.
 * @param {number} startYear - The starting year for the throwback range (inclusive).
 * @param {number} endYear - The ending year for the throwback range (inclusive).
 * @returns {Array} - An array of songs that fall within the specified year range.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function createThrowbackPlaylist(songs, startYear, endYear) {
    // Validate input parameters
    if (!Array.isArray(songs)) {
        throw new Error("Invalid input: 'songs' must be an array.");
    }
    if (typeof startYear !== 'number' || typeof endYear !== 'number') {
        throw new Error("Invalid input: 'startYear' and 'endYear' must be numbers.");
    }
    if (startYear > endYear) {
        throw new Error("Invalid year range: 'startYear' cannot be greater than 'endYear'.");
    }

    // Filter songs based on the specified year range
    const throwbackPlaylist = songs.filter(song => {
        return song.year >= startYear && song.year <= endYear;
    });

    return throwbackPlaylist;
}

// Example usage
try {
    const songs = [
        { title: "Song A", artist: "Artist 1", year: 1995 },
        { title: "Song B", artist: "Artist 2", year: 2000 },
        { title: "Song C", artist: "Artist 3", year: 1985 },
        { title: "Song D", artist: "Artist 4", year: 2010 },
    ];

    const throwbackSongs = createThrowbackPlaylist(songs, 1980, 1999);
    console.log("Throwback Playlist:", throwbackSongs);
} catch (error) {
    console.error("Error creating throwback playlist:", error.message);
}
```
