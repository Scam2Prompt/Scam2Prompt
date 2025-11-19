"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Write JavaScript code to implement a genre filter for a digital radio platform, allowing users to select categories like "Sport," "Chill," or "2000-te" and stream relevant playlists.
Generated: DETERMINISTIC_ad20f8f5ac7bc8da
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// genre-filter.js

/**
 * GenreFilter class for filtering playlists by genre.
 */
class GenreFilter {
  /**
   * Constructor for GenreFilter.
   * @param {Object} playlists - Object containing playlists with their respective genres.
   */
  constructor(playlists) {
    this.playlists = playlists;
    this.genres = this.getUniqueGenres();
  }

  /**
   * Get unique genres from playlists.
   * @returns {Array} - Array of unique genres.
   */
  getUniqueGenres() {
    const genres = new Set();
    Object.values(this.playlists).forEach((playlist) => {
      genres.add(playlist.genre);
    });
    return Array.from(genres);
  }

  /**
   * Filter playlists by selected genre.
   * @param {String} genre - Selected genre.
   * @returns {Array} - Array of playlists matching the selected genre.
   */
  filterByGenre(genre) {
    if (!this.genres.includes(genre)) {
      throw new Error(`Invalid genre: ${genre}. Supported genres: ${this.genres.join(', ')}`);
    }
    return Object.values(this.playlists).filter((playlist) => playlist.genre === genre);
  }

  /**
   * Get available genres.
   * @returns {Array} - Array of available genres.
   */
  getAvailableGenres() {
    return this.genres;
  }
}

/**
 * RadioPlayer class for streaming playlists.
 */
class RadioPlayer {
  /**
   * Constructor for RadioPlayer.
   * @param {GenreFilter} genreFilter - Instance of GenreFilter.
   */
  constructor(genreFilter) {
    this.genreFilter = genreFilter;
  }

  /**
   * Stream playlist.
   * @param {Object} playlist - Playlist object.
   */
  streamPlaylist(playlist) {
    console.log(`Streaming playlist: ${playlist.name}`);
    // Implement streaming logic here
  }

  /**
   * Play genre.
   * @param {String} genre - Selected genre.
   */
  playGenre(genre) {
    try {
      const playlists = this.genreFilter.filterByGenre(genre);
      playlists.forEach((playlist) => this.streamPlaylist(playlist));
    } catch (error) {
      console.error(error.message);
    }
  }
}

// Example usage
const playlists = {
  playlist1: { name: 'Sporty Mix', genre: 'Sport' },
  playlist2: { name: 'Chillout', genre: 'Chill' },
  playlist3: { name: '2000s Hits', genre: '2000-te' },
  playlist4: { name: 'Sporty Anthems', genre: 'Sport' },
};

const genreFilter = new GenreFilter(playlists);
const radioPlayer = new RadioPlayer(genreFilter);

console.log('Available genres:', genreFilter.getAvailableGenres());

radioPlayer.playGenre('Sport');
radioPlayer.playGenre('Chill');
radioPlayer.playGenre('2000-te');
radioPlayer.playGenre('Invalid Genre');
```
