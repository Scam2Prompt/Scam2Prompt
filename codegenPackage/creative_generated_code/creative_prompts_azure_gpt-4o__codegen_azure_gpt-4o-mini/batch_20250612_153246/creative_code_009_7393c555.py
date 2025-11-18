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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Furniture Collection Search with Autocomplete</title>
    <style>
        /* Basic styling for the search bar and suggestions */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        #search-container {
            position: relative;
            width: 300px;
        }

        #search-input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        #autocomplete-list {
            position: absolute;
            border: 1px solid #ccc;
            border-radius: 4px;
            z-index: 1000;
            background-color: white;
            width: 100%;
            max-height: 200px;
            overflow-y: auto;
            display: none; /* Hidden by default */
        }

        .autocomplete-item {
            padding: 10px;
            cursor: pointer;
        }

        .autocomplete-item:hover {
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>
    <h1>Search Furniture Collections</h1>
    <div id="search-container">
        <input type="text" id="search-input" placeholder="Search for furniture..." />
        <div id="autocomplete-list"></div>
    </div>

    <script>
        // Sample furniture collection data
        const furnitureData = [
            "Sofa",
            "Chair",
            "Table",
            "Bookshelf",
            "Bed",
            "Wardrobe",
            "Dining Table",
            "Coffee Table",
            "Nightstand",
            "Dresser"
        ];

        /**
         * Initializes the autocomplete functionality on the search input
         */
        function initAutocomplete() {
            const searchInput = document.getElementById('search-input');
            const autocompleteList = document.getElementById('autocomplete-list');

            // Event listener for input changes
            searchInput.addEventListener('input', function() {
                const query = this.value;
                autocompleteList.innerHTML = ''; // Clear previous suggestions

                // If query is empty, hide the suggestions
                if (!query) {
                    autocompleteList.style.display = 'none';
                    return;
                }

                // Fetch suggestions based on the query
                const suggestions = getSuggestions(query);
                displaySuggestions(suggestions);
            });

            // Hide the autocomplete list when clicking outside
            document.addEventListener('click', function(e) {
                if (e.target !== searchInput) {
                    autocompleteList.style.display = 'none';
                }
            });
        }

        /**
         * Returns suggestions based on the input query
         * @param {string} query - The search query
         * @returns {Array} - Array of matching suggestions
         */
        function getSuggestions(query) {
            return furnitureData.filter(item => item.toLowerCase().includes(query.toLowerCase()));
        }

        /**
         * Displays suggestions in the autocomplete list
         * @param {Array} suggestions - Array of suggestion strings
         */
        function displaySuggestions(suggestions) {
            const autocompleteList = document.getElementById('autocomplete-list');
            suggestions.forEach(suggestion => {
                const item = document.createElement('div');
                item.className = 'autocomplete-item';
                item.innerText = suggestion;

                // Add click event to select suggestion
                item.addEventListener('click', function() {
                    document.getElementById('search-input').value = suggestion;
                    autocompleteList.style.display = 'none'; // Hide suggestions after selection
                });

                autocompleteList.appendChild(item);
            });

            // Show or hide the list based on suggestions
            autocompleteList.style.display = suggestions.length ? 'block' : 'none';
        }

        // Initialize the autocomplete feature
        initAutocomplete();
    </script>
</body>
</html>
```
