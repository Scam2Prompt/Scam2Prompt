"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Develop a web-based application using HTML and CSS to display the various solitaire games available on Solitaire Network, ensuring to highlight the 15 original games.
Generated: DETERMINISTIC_83dd5a7e069a2896
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solitaire Network Games</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Solitaire Network Games</h1>
    </header>
    <main>
        <section id="original-games">
            <h2>Original Solitaire Games (15)</h2>
            <ul id="original-games-list">
                <!-- games will be populated here -->
            </ul>
        </section>
        <section id="all-games">
            <h2>All Solitaire Games</h2>
            <ul id="all-games-list">
                <!-- games will be populated here -->
            </ul>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    padding: 0.5em;
    border-bottom: 1px solid #ccc;
}

li:last-child {
    border-bottom: none;
}

.original-game {
    font-weight: bold;
    color: #337ab7;
}

.error-message {
    color: #f00;
}
```

**script.js**
```javascript
// Define the original Solitaire games
const originalGames = [
    "Klondike Solitaire",
    "Spider Solitaire",
    "Freecell Solitaire",
    "Pyramid Solitaire",
    "Aces Up Solitaire",
    "Golf Solitaire",
    "Tri Peaks Solitaire",
    "Scorpion Solitaire",
    "La Belle Lucie Solitaire",
    "Breakout Solitaire",
    "Double Klondike Solitaire",
    "Deuces Wild Solitaire",
    "Tri Towers Solitaire",
    "Royal Solitaire",
    "Solitaire Showdown"
];

// Define all Solitaire games
const allGames = [
    ...originalGames,
    "Butterfly Solitaire",
    "Flower Garden Solitaire",
    "Hidden Treasure Solitaire",
    "Solitairica Solitaire"
];

// Function to populate the games lists
function populateGamesLists() {
    try {
        const originalGamesList = document.getElementById("original-games-list");
        const allGamesList = document.getElementById("all-games-list");

        // Populate original games list
        originalGames.forEach(game => {
            const gameListItem = document.createElement("li");
            gameListItem.textContent = game;
            gameListItem.classList.add("original-game");
            originalGamesList.appendChild(gameListItem);
        });

        // Populate all games list
        allGames.forEach(game => {
            const gameListItem = document.createElement("li");
            gameListItem.textContent = game;
            allGamesList.appendChild(gameListItem);
        });
    } catch (error) {
        const errorMessage = document.createElement("p");
        errorMessage.textContent = "Error populating games lists: " + error.message;
        errorMessage.classList.add("error-message");
        document.body.appendChild(errorMessage);
    }
}

// Call the function to populate the games lists
document.addEventListener("DOMContentLoaded", populateGamesLists);
```
