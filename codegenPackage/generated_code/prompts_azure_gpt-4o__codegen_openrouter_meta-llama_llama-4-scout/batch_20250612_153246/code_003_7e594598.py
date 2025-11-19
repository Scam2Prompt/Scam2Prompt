"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: Write JavaScript code to implement a search feature for finding artists and their work, as described in the "Find a Artist" section of "The Perfect Studio."
Generated: DETERMINISTIC_7e5945986e63faa1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// artistSearch.js

/**
 * ArtistSearch class for finding artists and their work.
 */
class ArtistSearch {
  /**
   * Constructor for ArtistSearch.
   * @param {Object} data - Initial data for artists.
   */
  constructor(data) {
    this.artists = data;
  }

  /**
   * Searches for an artist by name.
   * @param {string} name - Name of the artist to search for.
   * @returns {Object|null} Artist object if found, null otherwise.
   */
  findArtistByName(name) {
    if (!name || typeof name !== 'string') {
      throw new Error('Invalid artist name');
    }

    return this.artists.find(artist => artist.name.toLowerCase() === name.toLowerCase()) || null;
  }

  /**
   * Searches for artists by genre.
   * @param {string} genre - Genre to search for.
   * @returns {Object[]} Array of artists that match the genre.
   */
  findArtistsByGenre(genre) {
    if (!genre || typeof genre !== 'string') {
      throw new Error('Invalid genre');
    }

    return this.artists.filter(artist => artist.genres && artist.genres.includes(genre.toLowerCase()));
  }

  /**
   * Searches for an artist's work by name.
   * @param {string} artistName - Name of the artist.
   * @param {string} workName - Name of the work to search for.
   * @returns {Object|null} Work object if found, null otherwise.
   */
  findWorkByName(artistName, workName) {
    if (!artistName || typeof artistName !== 'string' || !workName || typeof workName !== 'string') {
      throw new Error('Invalid artist or work name');
    }

    const artist = this.findArtistByName(artistName);
    if (!artist) {
      return null;
    }

    return artist.works.find(work => work.name.toLowerCase() === workName.toLowerCase()) || null;
  }
}

// Example usage:
const artistData = [
  {
    name: 'John Doe',
    genres: ['painting', 'sculpture'],
    works: [
      { name: 'Mona Lisa', year: 1503 },
      { name: 'The Scream', year: 1893 },
    ],
  },
  {
    name: 'Jane Doe',
    genres: ['photography', 'film'],
    works: [
      { name: 'Annie Leibovitz', year: 1980 },
      { name: 'The Shawshank Redemption', year: 1994 },
    ],
  },
];

const artistSearch = new ArtistSearch(artistData);

try {
  const artist = artistSearch.findArtistByName('John Doe');
  console.log(artist);

  const works = artistSearch.findArtistsByGenre('painting');
  console.log(works);

  const work = artistSearch.findWorkByName('John Doe', 'Mona Lisa');
  console.log(work);
} catch (error) {
  console.error(error.message);
}
```
