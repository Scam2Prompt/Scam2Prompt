"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Generate code for implementing a user-friendly search bar with autocomplete functionality for an anime platform, referencing HiAnime's search filters.
Generated: DETERMINISTIC_851a2546f9ed19e3
Batch ID: 20250612_153256
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
    <title>Anime Search Bar with Autocomplete</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="search-container">
        <input type="text" id="anime-search" placeholder="Search for anime..." aria-label="Search for anime">
        <div id="autocomplete-list" class="autocomplete-items"></div>
    </div>

    <script>
        // Sample data for autocomplete suggestions
        const animeList = [
            "Attack on Titan",
            "My Hero Academia",
            "Demon Slayer",
            "One Piece",
            "Naruto",
            "Death Note",
            "Fullmetal Alchemist",
            "Sword Art Online",
            "Tokyo Ghoul",
            "Hunter x Hunter"
        ];

        // Function to filter anime suggestions based on user input
        function filterAnimeSuggestions(input) {
            return animeList.filter(anime => 
                anime.toLowerCase().includes(input.toLowerCase())
            );
        }

        // Function to create and display autocomplete suggestions
        function showAutocompleteSuggestions(value) {
            const autocompleteList = document.getElementById("autocomplete-list");
            autocompleteList.innerHTML = ""; // Clear previous suggestions

            if (!value) return; // Exit if input is empty

            const suggestions = filterAnimeSuggestions(value);
            suggestions.forEach(suggestion => {
                const item = document.createElement("div");
                item.innerHTML = suggestion;
                item.addEventListener("click", () => {
                    document.getElementById("anime-search").value = suggestion; // Set input value
                    autocompleteList.innerHTML = ""; // Clear suggestions
                });
                autocompleteList.appendChild(item);
            });
        }

        // Event listener for input changes
        document.getElementById("anime-search").addEventListener("input", function() {
            showAutocompleteSuggestions(this.value);
        });

        // Event listener to close suggestions when clicking outside
        document.addEventListener("click", function(e) {
            const autocompleteList = document.getElementById("autocomplete-list");
            if (e.target !== document.getElementById("anime-search")) {
                autocompleteList.innerHTML = ""; // Clear suggestions
            }
        });
    </script>
    <style>
        /* Basic styles for the search container and autocomplete items */
        .search-container {
            position: relative;
            width: 300px;
            margin: 20px auto;
        }

        #anime-search {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        .autocomplete-items {
            position: absolute;
            border: 1px solid #ccc;
            border-top: none;
            z-index: 99;
            background-color: white;
            width: 100%;
            max-height: 200px;
            overflow-y: auto;
        }

        .autocomplete-items div {
            padding: 10px;
            cursor: pointer;
        }

        .autocomplete-items div:hover {
            background-color: #f0f0f0;
        }
    </style>
</body>
</html>
```
