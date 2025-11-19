"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Write a JavaScript script to implement a search bar with autocomplete functionality for furniture collections, similar to the search feature described on Nodo Italia's website.
Generated: DETERMINISTIC_7393c555b6640f13
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Furniture Collection Search</title>
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
        #suggestions {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            background: white;
            z-index: 1000;
            display: none; /* Hidden by default */
        }
        .suggestion-item {
            padding: 10px;
            cursor: pointer;
        }
        .suggestion-item:hover {
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>

<div id="search-container">
    <input type="text" id="search-input" placeholder="Search for furniture..." />
    <div id="suggestions"></div>
</div>

<script>
    // Sample furniture collection data
    const furnitureCollection = [
        "Sofa",
        "Dining Table",
        "Coffee Table",
        "Bookshelf",
        "Chair",
        "Bed",
        "Wardrobe",
        "Desk",
        "Nightstand",
        "Dresser"
    ];

    // Get references to DOM elements
    const searchInput = document.getElementById('search-input');
    const suggestionsContainer = document.getElementById('suggestions');

    // Function to filter furniture items based on user input
    function filterFurniture(query) {
        return furnitureCollection.filter(item => 
            item.toLowerCase().includes(query.toLowerCase())
        );
    }

    // Function to display suggestions
    function displaySuggestions(suggestions) {
        // Clear previous suggestions
        suggestionsContainer.innerHTML = '';
        if (suggestions.length === 0) {
            suggestionsContainer.style.display = 'none';
            return;
        }

        // Create suggestion items
        suggestions.forEach(suggestion => {
            const suggestionItem = document.createElement('div');
            suggestionItem.className = 'suggestion-item';
            suggestionItem.textContent = suggestion;

            // Add click event to suggestion item
            suggestionItem.addEventListener('click', () => {
                searchInput.value = suggestion; // Set input value to selected suggestion
                suggestionsContainer.style.display = 'none'; // Hide suggestions
            });

            suggestionsContainer.appendChild(suggestionItem);
        });

        // Show suggestions
        suggestionsContainer.style.display = 'block';
    }

    // Event listener for input changes
    searchInput.addEventListener('input', () => {
        const query = searchInput.value.trim();
        if (query) {
            const filteredSuggestions = filterFurniture(query);
            displaySuggestions(filteredSuggestions);
        } else {
            suggestionsContainer.style.display = 'none'; // Hide suggestions if input is empty
        }
    });

    // Event listener to hide suggestions when clicking outside
    document.addEventListener('click', (event) => {
        if (!searchInput.contains(event.target) && !suggestionsContainer.contains(event.target)) {
            suggestionsContainer.style.display = 'none'; // Hide suggestions
        }
    });
</script>

</body>
</html>
```
