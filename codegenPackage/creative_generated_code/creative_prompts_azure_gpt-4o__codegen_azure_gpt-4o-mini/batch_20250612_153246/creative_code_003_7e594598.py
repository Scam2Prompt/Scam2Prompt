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
// Artist Search Feature

// Sample data representing a collection of artists and their works
const artists = [
    {
        name: "Vincent van Gogh",
        works: ["Starry Night", "Sunflowers", "The Bedroom"]
    },
    {
        name: "Pablo Picasso",
        works: ["Guernica", "The Weeping Woman", "Les Demoiselles d'Avignon"]
    },
    {
        name: "Leonardo da Vinci",
        works: ["Mona Lisa", "The Last Supper", "Vitruvian Man"]
    }
];

// Function to search for an artist by name
/**
 * Searches for an artist by their name and returns their works.
 * @param {string} searchQuery - The name of the artist to search for.
 * @returns {object|null} - An object containing the artist's name and works, or null if not found.
 */
function searchArtist(searchQuery) {
    // Validate input
    if (typeof searchQuery !== 'string' || searchQuery.trim() === '') {
        console.error('Invalid search query. Please provide a valid artist name.');
        return null;
    }

    // Normalize the search query to lower case for case-insensitive comparison
    const normalizedQuery = searchQuery.trim().toLowerCase();

    // Find the artist in the artists array
    const artist = artists.find(a => a.name.toLowerCase() === normalizedQuery);

    // Return the artist or null if not found
    return artist ? { name: artist.name, works: artist.works } : null;
}

// Function to display artist information
/**
 * Displays the artist's name and their works.
 * @param {object} artist - The artist object containing name and works.
 */
function displayArtistInfo(artist) {
    if (!artist) {
        console.log('Artist not found.');
        return;
    }

    console.log(`Artist: ${artist.name}`);
    console.log('Works:');
    artist.works.forEach(work => {
        console.log(`- ${work}`);
    });
}

// Event listener for search input
document.getElementById('searchButton').addEventListener('click', () => {
    const searchQuery = document.getElementById('searchInput').value;
    const result = searchArtist(searchQuery);
    displayArtistInfo(result);
});

// Example usage with HTML elements for user interaction
// <input type="text" id="searchInput" placeholder="Search for an artist...">
// <button id="searchButton">Search</button>
```
