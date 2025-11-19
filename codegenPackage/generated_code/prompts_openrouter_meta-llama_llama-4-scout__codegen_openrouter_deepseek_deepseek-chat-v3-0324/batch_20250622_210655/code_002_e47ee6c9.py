"""
Generated Code Metadata:
========================
Original URL: https://karaokeheaven.uk
Prompt: Generate a JavaScript code snippet to implement a karaoke song recommendation system, taking into account the user's preferred language and genre, similar to Karaoke Heaven's extensive music library.
Generated: DETERMINISTIC_e47ee6c9e7dd0a0d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Karaoke Song Recommendation System
 * 
 * This system recommends karaoke songs based on user's preferred language and genre.
 * It mimics the functionality of Karaoke Heaven's music library.
 */

class KaraokeRecommendationSystem {
    /**
     * Initialize the recommendation system with a song library
     * @param {Object[]} songLibrary - Array of song objects
     */
    constructor(songLibrary = []) {
        this.songLibrary = songLibrary;
    }

    /**
     * Add songs to the library
     * @param {Object[]} songs - Array of song objects to add
     */
    addSongs(songs) {
        if (!Array.isArray(songs)) {
            throw new Error('Songs must be provided as an array');
        }
        this.songLibrary = [...this.songLibrary, ...songs];
    }

    /**
     * Get recommendations based on language and genre preferences
     * @param {string} language - Preferred language for songs
     * @param {string} genre - Preferred genre for songs
     * @param {number} limit - Maximum number of recommendations to return
     * @returns {Object[]} Array of recommended song objects
     */
    getRecommendations(language, genre, limit = 10) {
        if (!language || !genre) {
            throw new Error('Both language and genre parameters are required');
        }

        if (typeof limit !== 'number' || limit <= 0) {
            throw new Error('Limit must be a positive number');
        }

        const filteredSongs = this.songLibrary.filter(song => {
            return song.language.toLowerCase() === language.toLowerCase() && 
                   song.genre.toLowerCase() === genre.toLowerCase();
        });

        // Sort by popularity (descending) if available
        if (filteredSongs.length > 0 && filteredSongs[0].popularity !== undefined) {
            filteredSongs.sort((a, b) => b.popularity - a.popularity);
        }

        return filteredSongs.slice(0, limit);
    }

    /**
     * Get all available languages in the library
     * @returns {string[]} Array of unique languages
     */
    getAvailableLanguages() {
        const languages = new Set();
        this.songLibrary.forEach(song => {
            languages.add(song.language);
        });
        return Array.from(languages);
    }

    /**
     * Get all available genres for a specific language
     * @param {string} language - Language to filter genres by
     * @returns {string[]} Array of unique genres for the language
     */
    getAvailableGenres(language) {
        if (!language) {
            throw new Error('Language parameter is required');
        }

        const genres = new Set();
        this.songLibrary.forEach(song => {
            if (song.language.toLowerCase() === language.toLowerCase()) {
                genres.add(song.genre);
            }
        });
        return Array.from(genres);
    }
}

// Example usage:
/*
const songLibrary = [
    { title: "Bohemian Rhapsody", artist: "Queen", language: "English", genre: "Rock", popularity: 95 },
    { title: "Rolling in the Deep", artist: "Adele", language: "English", genre: "Pop", popularity: 90 },
    { title: "Despacito", artist: "Luis Fonsi", language: "Spanish", genre: "Pop", popularity: 85 },
    { title: "Ai no Corrida", artist: "Quincy Jones", language: "Japanese", genre: "Pop", popularity: 80 },
    { title: "Gangnam Style", artist: "PSY", language: "Korean", genre: "Pop", popularity: 88 }
];

const karaokeSystem = new KaraokeRecommendationSystem(songLibrary);
const recommendations = karaokeSystem.getRecommendations("English", "Pop", 5);
console.log(recommendations);
*/
```
