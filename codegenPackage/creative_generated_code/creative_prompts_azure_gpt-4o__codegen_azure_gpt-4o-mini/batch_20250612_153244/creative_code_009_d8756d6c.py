"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galagames-rewards.com
Prompt: Create a simple web-based "Emoji Matching" game inspired by Mynet's "Emojile" game.
Generated: DETERMINISTIC_d8756d6ca5cd6aae
Batch ID: 20250612_153244
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
    <title>Emoji Matching Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(4, 100px);
            grid-gap: 10px;
        }
        .card {
            width: 100px;
            height: 100px;
            background-color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            border: 1px solid #ccc;
            cursor: pointer;
            user-select: none;
        }
        .matched {
            background-color: #aaffaa;
        }
        .flipped {
            background-color: #ffcc00;
        }
        .hidden {
            visibility: hidden;
        }
        #message {
            margin-top: 20px;
            font-size: 1.5rem;
        }
    </style>
</head>
<body>

<h1>Emoji Matching Game</h1>
<div class="grid" id="grid"></div>
<div id="message"></div>
<button id="restart" class="hidden">Restart Game</button>

<script>
    // Emoji Matching Game Implementation
    const emojis = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', 
                   '😊', '😇', '🥰', '😍', '🤩', '😘', '😗', '😚'];
    const gameEmojis = [...emojis.slice(0, 8), ...emojis.slice(0, 8)];
    let flippedCards = [];
    let matchedCount = 0;
    const grid = document.getElementById('grid');
    const message = document.getElementById('message');
    const restartButton = document.getElementById('restart');

    // Shuffle the emoji array
    function shuffle(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    // Initialize the game
    function initGame() {
        matchedCount = 0;
        flippedCards = [];
        message.textContent = '';
        grid.innerHTML = '';
        shuffle(gameEmojis).forEach(emoji => {
            const card = document.createElement('div');
            card.classList.add('card');
            card.dataset.emoji = emoji;
            card.addEventListener('click', flipCard);
            grid.appendChild(card);
        });
        restartButton.classList.add('hidden');
    }

    // Handle card flipping
    function flipCard() {
        if (flippedCards.length < 2 && !this.classList.contains('flipped') && !this.classList.contains('matched')) {
            this.classList.add('flipped');
            this.textContent = this.dataset.emoji;
            flippedCards.push(this);

            if (flippedCards.length === 2) {
                setTimeout(checkMatch, 1000);
            }
        }
    }

    // Check for a match
    function checkMatch() {
        const [firstCard, secondCard] = flippedCards;
        if (firstCard.dataset.emoji === secondCard.dataset.emoji) {
            firstCard.classList.add('matched');
            secondCard.classList.add('matched');
            matchedCount += 2;
            if (matchedCount === gameEmojis.length) {
                message.textContent = 'Congratulations! You matched all emojis!';
                restartButton.classList.remove('hidden');
            }
        } else {
            firstCard.classList.remove('flipped');
            secondCard.classList.remove('flipped');
            firstCard.textContent = '';
            secondCard.textContent = '';
        }
        flippedCards = [];
    }

    // Restart the game
    restartButton.addEventListener('click', initGame);

    // Start the game on page load
    document.addEventListener('DOMContentLoaded', initGame);
</script>

</body>
</html>
```
