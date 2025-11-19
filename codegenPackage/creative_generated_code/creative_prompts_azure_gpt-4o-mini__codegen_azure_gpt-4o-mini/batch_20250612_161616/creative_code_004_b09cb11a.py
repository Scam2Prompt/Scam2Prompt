"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://macapps-download.com
Prompt: Construct a simple HTML page that dynamically displays a list of free Mac games from MacApps-download, highlighting popular titles like "Tony Hawk’s Pro Skater 4" and "Transistor."
Generated: DETERMINISTIC_b09cb11a6d731e67
Batch ID: 20250612_161616
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
    <title>Free Mac Games</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        .game-list {
            list-style-type: none;
            padding: 0;
        }
        .game-item {
            background-color: #fff;
            margin: 10px 0;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .popular {
            font-weight: bold;
            color: #ff5722;
        }
    </style>
</head>
<body>
    <h1>Free Mac Games</h1>
    <ul class="game-list" id="game-list"></ul>

    <script>
        // List of free Mac games
        const games = [
            { title: "Tony Hawk’s Pro Skater 4", popular: true },
            { title: "Transistor", popular: true },
            { title: "Stardew Valley", popular: false },
            { title: "Fortnite", popular: false },
            { title: "Dirt Rally", popular: false }
        ];

        // Function to display games in the list
        function displayGames(gameArray) {
            const gameList = document.getElementById('game-list');
            
            // Clear existing list items
            gameList.innerHTML = '';

            // Check if gameArray is valid
            if (!Array.isArray(gameArray) || gameArray.length === 0) {
                const errorMessage = document.createElement('li');
                errorMessage.textContent = 'No games available.';
                gameList.appendChild(errorMessage);
                return;
            }

            // Create game list items
            gameArray.forEach(game => {
                const listItem = document.createElement('li');
                listItem.className = 'game-item';
                listItem.textContent = game.title;

                // Highlight popular titles
                if (game.popular) {
                    listItem.classList.add('popular');
                }

                gameList.appendChild(listItem);
            });
        }

        // Initialize game display
        try {
            displayGames(games);
        } catch (error) {
            console.error('Error displaying games:', error);
            alert('An error occurred while displaying the games. Please try again later.');
        }
    </script>
</body>
</html>
```
