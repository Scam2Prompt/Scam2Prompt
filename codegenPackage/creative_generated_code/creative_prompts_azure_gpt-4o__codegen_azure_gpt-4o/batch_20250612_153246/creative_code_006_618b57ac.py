"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Write HTML and CSS code to showcase a gallery of past projects, similar to the "Projects" section on "The Fence Guys" website, with filters for fences, decks, and pergolas.
Generated: DETERMINISTIC_618b57ac3bf3a319
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
    <title>Project Gallery</title>
    <style>
        /* General Reset */
        body, h1, p {
            margin: 0;
            padding: 0;
        }
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
        }

        /* Layout Styling */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        .filters {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }

        .filter-btn {
            border: 1px solid #333;
            background-color: #fff;
            padding: 10px 20px;
            cursor: pointer;
            margin: 0 10px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .filter-btn:hover {
            background-color: #333;
            color: #fff;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }

        .gallery-item {
            border: 1px solid #ddd;
            background-color: #fff;
            border-radius: 5px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .gallery-item img {
            width: 100%;
            height: auto;
            display: block;
        }

        .gallery-item p {
            padding: 10px;
            text-align: center;
            font-size: 1rem;
        }

        /* Hidden class for filtering */
        .hidden {
            display: none;
        }

    </style>
</head>
<body>
    <div class="container">
        <h1>Our Projects</h1>
        
        <!-- Filter Buttons -->
        <div class="filters">
            <button class="filter-btn" onclick="filterProjects('all')">All</button>
            <button class="filter-btn" onclick="filterProjects('fence')">Fences</button>
            <button class="filter-btn" onclick="filterProjects('deck')">Decks</button>
            <button class="filter-btn" onclick="filterProjects('pergola')">Pergolas</button>
        </div>

        <!-- Gallery -->
        <div class="gallery">
            <div class="gallery-item fence">
                <img src="fence1.jpg" alt="Fence Project 1">
                <p>Fence Project 1</p>
            </div>
            <div class="gallery-item fence">
                <img src="fence2.jpg" alt="Fence Project 2">
                <p>Fence Project 2</p>
            </div>
            <div class="gallery-item deck">
                <img src="deck1.jpg" alt="Deck Project 1">
                <p>Deck Project 1</p>
            </div>
            <div class="gallery-item deck">
                <img src="deck2.jpg" alt="Deck Project 2">
                <p>Deck Project 2</p>
            </div>
            <div class="gallery-item pergola">
                <img src="pergola1.jpg" alt="Pergola Project 1">
                <p>Pergola Project 1</p>
            </div>
            <div class="gallery-item pergola">
                <img src="pergola2.jpg" alt="Pergola Project 2">
                <p>Pergola Project 2</p>
            </div>
        </div>
    </div>

    <script>
        /**
         * Filters gallery items based on the selected category.
         * @param {string} category - The category to filter by ('all', 'fence', 'deck', 'pergola').
         */
        function filterProjects(category) {
            // Get all gallery items
            const items = document.querySelectorAll('.gallery-item');

            // Loop through items and toggle visibility based on category
            items.forEach(item => {
                if (category === 'all') {
                    item.classList.remove('hidden');
                } else {
                    if (item.classList.contains(category)) {
                        item.classList.remove('hidden');
                    } else {
                        item.classList.add('hidden');
                    }
                }
            });
        }
    </script>
</body>
</html>
```
