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
/**
 * GenreFilter - A digital radio platform genre filter component.
 * Allows users to filter playlists by genre and stream relevant content.
 */

class GenreFilter {
  /**
   * @constructor
   * @param {Object} options - Configuration options
   * @param {HTMLElement} options.container - DOM element to mount the filter
   * @param {Array} options.genres - List of available genres
   * @param {Function} options.onGenreSelect - Callback when genre is selected
   */
  constructor(options) {
    this.container = options.container;
    this.genres = options.genres || [];
    this.onGenreSelect = options.onGenreSelect || (() => {});
    this.selectedGenre = null;
    
    if (!this.container) {
      throw new Error('Container element is required');
    }
    
    this.init();
  }

  /**
   * Initialize the genre filter component
   */
  init() {
    this.render();
    this.bindEvents();
  }

  /**
   * Render the genre filter UI
   */
  render() {
    if (!this.genres.length) {
      this.container.innerHTML = '<p>No genres available</p>';
      return;
    }

    const genreList = this.genres.map(genre => `
      <button 
        class="genre-btn ${this.selectedGenre === genre.id ? 'active' : ''}" 
        data-genre-id="${genre.id}"
      >
        ${genre.name}
      </button>
    `).join('');

    this.container.innerHTML = `
      <div class="genre-filter">
        <h3>Filter by Genre</h3>
        <div class="genre-buttons">${genreList}</div>
      </div>
    `;
  }

  /**
   * Bind event listeners
   */
  bindEvents() {
    const buttons = this.container.querySelectorAll('.genre-btn');
    buttons.forEach(btn => {
      btn.addEventListener('click', (e) => this.handleGenreClick(e));
    });
  }

  /**
   * Handle genre button click
   * @param {Event} e - Click event
   */
  handleGenreClick(e) {
    const genreId = e.currentTarget.getAttribute('data-genre-id');
    const genre = this.genres.find(g => g.id === genreId);
    
    if (!genre) {
      console.error('Genre not found');
      return;
    }

    this.selectedGenre = genreId;
    this.render();
    this.onGenreSelect(genre);
  }

  /**
   * Update available genres
   * @param {Array} genres - New list of genres
   */
  updateGenres(genres) {
    if (!Array.isArray(genres)) {
      console.error('Genres must be an array');
      return;
    }
    
    this.genres = genres;
    this.selectedGenre = null;
    this.render();
  }
}

// Example usage:
/*
const genres = [
  { id: 'sport', name: 'Sport' },
  { id: 'chill', name: 'Chill' },
  { id: '2000s', name: '2000-te' }
];

const filter = new GenreFilter({
  container: document.getElementById('genre-filter'),
  genres: genres,
  onGenreSelect: (genre) => {
    console.log('Selected genre:', genre.name);
    // Here you would typically fetch and play the relevant playlist
    // For example: player.loadPlaylist(genre.id);
  }
});

// To update genres later:
// filter.updateGenres(newGenres);
*/
```
