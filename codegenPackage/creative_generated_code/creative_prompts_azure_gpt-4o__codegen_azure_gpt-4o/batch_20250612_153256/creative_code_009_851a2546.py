"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hianime.baby
Prompt: Generate code for implementing a user-friendly search bar with autocomplete functionality for an anime platform, referencing HiAnime's search filters.
Generated: DETERMINISTIC_851a2546f9ed19e3
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anime Search Bar</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="search-container">
    <input
      type="text"
      id="anime-search"
      placeholder="Search for anime..."
      autocomplete="off"
    />
    <div id="autocomplete-list" class="autocomplete-items"></div>
  </div>
  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the search container */
.search-container {
  position: relative;
  width: 100%;
  max-width: 400px;
  margin: 20px auto;
}

#anime-search {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* Styling for autocomplete suggestions */
.autocomplete-items {
  position: absolute;
  border: 1px solid #ccc;
  border-top: none;
  z-index: 99;
  top: 100%;
  left: 0;
  right: 0;
  background-color: #fff;
  max-height: 200px;
  overflow-y: auto;
}

.autocomplete-items div {
  padding: 10px;
  cursor: pointer;
  background-color: #fff;
}

.autocomplete-items div:hover {
  background-color: #f0f0f0;
}
```

```javascript
// script.js

/**
 * Mock data simulating anime titles.
 * In production, this data would come from an API.
 */
const animeTitles = [
  "Naruto",
  "One Piece",
  "Attack on Titan",
  "My Hero Academia",
  "Demon Slayer",
  "Dragon Ball Z",
  "Bleach",
  "Hunter x Hunter",
  "Death Note",
  "Jujutsu Kaisen",
];

/**
 * Error-safe function to clear autocomplete suggestions.
 */
function clearSuggestions() {
  const suggestions = document.getElementById("autocomplete-list");
  if (suggestions) {
    suggestions.innerHTML = "";
  }
}

/**
 * Function to handle the autocomplete feature.
 * Updates the suggestions based on user input.
 */
function autocomplete(input) {
  // Clear previous suggestions
  clearSuggestions();

  const query = input.value.toLowerCase();
  if (!query) {
    return;
  }

  // Filter the anime titles based on the query
  const filteredTitles = animeTitles.filter((title) =>
    title.toLowerCase().startsWith(query)
  );

  // Display filtered results
  const listContainer = document.getElementById("autocomplete-list");
  filteredTitles.forEach((title) => {
    const suggestionDiv = document.createElement("div");
    suggestionDiv.textContent = title;

    // Clicking sets the input value to the selected suggestion
    suggestionDiv.addEventListener("click", () => {
      input.value = title;
      clearSuggestions();
    });

    listContainer.appendChild(suggestionDiv);
  });
}

// Attach event listeners to the search bar input field
const searchInput = document.getElementById("anime-search");

searchInput.addEventListener("input", () => autocomplete(searchInput));

// Hide suggestions when clicking outside of the search bar
document.addEventListener("click", (event) => {
  if (event.target !== searchInput) {
    clearSuggestions();
  }
});
```
