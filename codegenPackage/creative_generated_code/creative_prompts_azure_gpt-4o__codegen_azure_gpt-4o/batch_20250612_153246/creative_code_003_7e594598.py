"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorsshadows.com
Prompt: Write JavaScript code to implement a search feature for finding artists and their work, as described in the "Find a Artist" section of "The Perfect Studio."
Generated: DETERMINISTIC_7e5945986e63faa1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Artist search feature for "The Perfect Studio".
 * This code allows users to search for artists and their works.
 * It is designed to be clean, efficient, and production-ready.
 */

// Example dataset: Array of artists and their works
const artists = [
  { name: 'Leonardo da Vinci', works: ['Mona Lisa', 'The Last Supper'] },
  { name: 'Vincent van Gogh', works: ['Starry Night', 'Sunflowers'] },
  { name: 'Pablo Picasso', works: ['Guernica', 'The Weeping Woman'] },
  { name: 'Claude Monet', works: ['Water Lilies', 'Impression, Sunrise'] },
];

/**
 * Function to search for artists and their works.
 * @param {string} query - The search query (artist name or work name).
 * @returns {Array} - A list of matching artists with their works.
 */
function searchArtists(query) {
  try {
    // Validate input query
    if (typeof query !== 'string' || query.trim() === '') {
      throw new Error('Search query must be a non-empty string.');
    }

    const normalizedQuery = query.toLowerCase();

    // Filter artists based on name or works
    const results = artists.filter(artist =>
      artist.name.toLowerCase().includes(normalizedQuery) ||
      artist.works.some(work => work.toLowerCase().includes(normalizedQuery))
    );

    // Return results or notify if no match was found
    if (results.length === 0) {
      console.log('No artists or works matched your query.');
      return [];
    }

    return results;
  } catch (error) {
    // Log error and return an empty array
    console.error(`Error during search: ${error.message}`);
    return [];
  }
}

// Example usage
const userQuery = 'starry'; // Replace with user input
const searchResults = searchArtists(userQuery);

if (searchResults.length > 0) {
  console.log(`Found ${searchResults.length} result(s):`);
  searchResults.forEach(artist => {
    console.log(`Artist: ${artist.name}`);
    console.log(`Works: ${artist.works.join(', ')}`);
  });
}
```
