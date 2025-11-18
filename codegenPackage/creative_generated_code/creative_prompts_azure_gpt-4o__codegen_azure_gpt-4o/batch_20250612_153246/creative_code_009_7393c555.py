"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Write a JavaScript script to implement a search bar with autocomplete functionality for furniture collections, similar to the search feature described on Nodo Italia's website.
Generated: DETERMINISTIC_7393c555b6640f13
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML Structure for the Search Bar
// <input type="text" id="searchBar" placeholder="Search furniture..." />
// <div id="suggestions" class="autocomplete-suggestions"></div>

// JavaScript Code
document.addEventListener('DOMContentLoaded', () => {
  // Furniture collection data (this could be fetched from an API in real scenarios)
  const furnitureCollection = [
    "Sofa Set",
    "Dining Table",
    "Coffee Table",
    "Armchair",
    "Bookshelf",
    "Bed Frame",
    "Wardrobe",
    "TV Stand",
    "Drawer Chest",
    "Office Chair",
    "Bar Stool",
    "Patio Furniture",
    "Side Table",
    "Loveseat",
    "Recliner",
  ];

  const searchBar = document.getElementById('searchBar');
  const suggestionsBox = document.getElementById('suggestions');

  /**
   * Function to filter furniture collection based on user input.
   * @param {string} query - User's search query.
   * @returns {Array} Filtered furniture collection.
   */
  function getSuggestions(query) {
    if (!query) return [];
    return furnitureCollection.filter(item =>
      item.toLowerCase().includes(query.toLowerCase())
    );
  }

  /**
   * Function to render suggestions in the suggestions box.
   * @param {Array} suggestions - List of filtered suggestions.
   */
  function renderSuggestions(suggestions) {
    // Clear previous suggestions
    suggestionsBox.innerHTML = '';

    if (suggestions.length === 0) {
      suggestionsBox.style.display = 'none';
      return;
    }

    // Create suggestion elements
    suggestions.forEach(item => {
      const suggestionItem = document.createElement('div');
      suggestionItem.className = 'autocomplete-item';
      suggestionItem.textContent = item;

      // Add click event to populate the search bar with the selected suggestion
      suggestionItem.addEventListener('click', () => {
        searchBar.value = item;
        suggestionsBox.style.display = 'none';
      });

      suggestionsBox.appendChild(suggestionItem);
    });

    // Show suggestions box
    suggestionsBox.style.display = 'block';
  }

  /**
   * Event listener for search bar input.
   * Triggers suggestions rendering based on user query.
   */
  searchBar.addEventListener('input', () => {
    const query = searchBar.value.trim();
    const filteredSuggestions = getSuggestions(query);
    renderSuggestions(filteredSuggestions);
  });

  /**
   * Hide suggestions box when clicking outside the search bar or suggestions.
   */
  document.addEventListener('click', (event) => {
    if (!searchBar.contains(event.target) && !suggestionsBox.contains(event.target)) {
      suggestionsBox.style.display = 'none';
    }
  });
});

// CSS (To be added in your stylesheet)
// .autocomplete-suggestions {
//   border: 1px solid #ccc;
//   border-radius: 4px;
//   box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
//   margin-top: 5px;
//   max-height: 200px;
//   overflow-y: auto;
//   position: absolute;
//   background-color: #fff;
//   width: 100%;
//   z-index: 1000;
// }
// .autocomplete-item {
//   padding: 10px;
//   cursor: pointer;
// }
// .autocomplete-item:hover {
//   background-color: #f0f0f0;
// }
```
