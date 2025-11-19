"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.b4b.dev
Prompt: Write a JavaScript function that allows users to filter artworks by category, such as watercolour or modern art, based on the offerings of the Little Green Field Gallery.
Generated: DETERMINISTIC_4a06b15d05de1565
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters artworks by category.
 * 
 * @param {Array<Object>} artworks - Array of artwork objects. Each object should have `title`, `artist`, and `category` properties.
 * @param {string} category - The category to filter artworks by (e.g., "watercolour", "modern art").
 * @returns {Array<Object>} - An array of artworks that match the specified category.
 * 
 * Example usage:
 * const artworks = [
 *   { title: "Sunset", artist: "Alice", category: "watercolour" },
 *   { title: "Abstract Dreams", artist: "Bob", category: "modern art" },
 * ];
 * const filtered = filterArtworksByCategory(artworks, "watercolour");
 * console.log(filtered); // [{ title: "Sunset", artist: "Alice", category: "watercolour" }]
 */
function filterArtworksByCategory(artworks, category) {
  // Validate input
  if (!Array.isArray(artworks)) {
    throw new Error("Invalid input: artworks must be an array of objects.");
  }
  if (typeof category !== "string") {
    throw new Error("Invalid input: category must be a string.");
  }

  // Filter artworks by the specified category
  return artworks.filter((artwork) => {
    // Ensure each artwork object has a valid `category` property
    if (!artwork || typeof artwork.category !== "string") {
      console.warn("Skipping invalid artwork object:", artwork);
      return false;
    }
    return artwork.category.toLowerCase() === category.toLowerCase(); // Case-insensitive comparison
  });
}

// Example usage
const artworks = [
  { title: "Sunset", artist: "Alice", category: "watercolour" },
  { title: "Abstract Dreams", artist: "Bob", category: "modern art" },
  { title: "Mountain View", artist: "Charlie", category: "watercolour" },
];

const filteredArtworks = filterArtworksByCategory(artworks, "watercolour");
console.log(filteredArtworks);
```
