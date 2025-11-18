"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as-media.rs
Prompt: Write JavaScript code to implement a genre filter for a digital radio platform, allowing users to select categories like "Sport," "Chill," or "2000-te" and stream relevant playlists.
Generated: DETERMINISTIC_ad20f8f5ac7bc8da
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// GenreFilter class to manage genre selections and streaming playlists
class GenreFilter {
    constructor() {
        // Initialize an empty array to store selected genres
        this.selectedGenres = [];
        // Example playlists for each genre
        this.playlists = {
            Sport: ['Sports Radio 1', 'Sports Talk 2', 'Live Sports Broadcast'],
            Chill: ['Chill Vibes', 'Relaxing Music', 'Evening Chill'],
            '2000s': ['2000s Hits', 'Throwback 2000s', 'Millennium Mix']
        };
    }

    /**
     * Select a genre for filtering playlists
     * @param {string} genre - The genre to select
     * @throws Will throw an error if the genre is invalid
     */
    selectGenre(genre) {
        if (!this.playlists[genre]) {
            throw new Error(`Invalid genre: ${genre}. Available genres: ${Object.keys(this.playlists).join(', ')}`);
        }
        // Avoid duplicates
        if (!this.selectedGenres.includes(genre)) {
            this.selectedGenres.push(genre);
        }
    }

    /**
     * Deselect a genre
     * @param {string} genre - The genre to deselect
     * @throws Will throw an error if the genre is not selected
     */
    deselectGenre(genre) {
        const index = this.selectedGenres.indexOf(genre);
        if (index === -1) {
            throw new Error(`Genre not selected: ${genre}`);
        }
        this.selectedGenres.splice(index, 1);
    }

    /**
     * Retrieve the playlists based on selected genres
     * @returns {Array} - Array of playlists matching selected genres
     */
    getPlaylists() {
        // Flatten the playlists based on selected genres
        return this.selectedGenres.flatMap(genre => this.playlists[genre]);
    }

    /**
     * Clear all selected genres
     */
    clearGenres() {
        this.selectedGenres = [];
    }
}

// Example usage:
try {
    const genreFilter = new GenreFilter();

    // Selecting genres
    genreFilter.selectGenre('Sport');
    genreFilter.selectGenre('Chill');
    
    // Logging playlists based on selected genres
    console.log('Playlists:', genreFilter.getPlaylists());

    // Deselecting a genre
    genreFilter.deselectGenre('Chill');

    // Logging updated playlists
    console.log('Updated Playlists:', genreFilter.getPlaylists());

    // Clear all genres
    genreFilter.clearGenres();
    console.log('Cleared Playlists:', genreFilter.getPlaylists());
} catch (error) {
    console.error('Error:', error.message);
}
```
