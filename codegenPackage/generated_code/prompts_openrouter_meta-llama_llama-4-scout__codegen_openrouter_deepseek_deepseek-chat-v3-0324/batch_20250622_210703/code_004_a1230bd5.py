"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Develop a simple game in JavaScript that teaches English vocabulary using the Topic Based Vocab section from Learn English Simply, focusing on Metal and Mineral vocabulary.
Generated: DETERMINISTIC_a1230bd5a5ae8efb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Vocabulary Game - Metal and Minerals
 * A simple game to teach English vocabulary related to metals and minerals.
 */

// Vocabulary data - Metals and Minerals
const vocabulary = [
    { word: "Gold", definition: "A yellow precious metal, the chemical element of atomic number 79." },
    { word: "Silver", definition: "A precious shiny grayish-white metal, the chemical element of atomic number 47." },
    { word: "Iron", definition: "A strong, hard magnetic silvery-gray metal, the chemical element of atomic number 26." },
    { word: "Copper", definition: "A red-brown metal, the chemical element of atomic number 29." },
    { word: "Aluminum", definition: "A light, silvery-white metal, the chemical element of atomic number 13." },
    { word: "Diamond", definition: "A precious stone consisting of a clear and colorless crystalline form of pure carbon." },
    { word: "Quartz", definition: "A hard mineral consisting of silica, found widely in igneous and metamorphic rocks." },
    { word: "Graphite", definition: "A gray, crystalline form of carbon used in pencils and as a lubricant." },
    { word: "Platinum", definition: "A heavy, malleable, ductile, precious gray-white metal." },
    { word: "Mercury", definition: "A heavy, silvery d-block element, liquid at room temperature." }
];

// Game state
let currentWordIndex = 0;
let score = 0;
let gameActive = false;

// DOM elements
const startButton = document.getElementById('start-btn');
const wordDisplay = document.getElementById('word-display');
const definitionDisplay = document.getElementById('definition-display');
const nextButton = document.getElementById('next-btn');
const scoreDisplay = document.getElementById('score');
const gameContainer = document.getElementById('game-container');

// Initialize the game
function initGame() {
    startButton.addEventListener('click', startGame);
    nextButton.addEventListener('click', nextWord);
}

// Start the game
function startGame() {
    gameActive = true;
    score = 0;
    currentWordIndex = 0;
    updateScore();
    
    // Hide start button and show game elements
    startButton.style.display = 'none';
    gameContainer.style.display = 'block';
    
    // Display first word
    displayCurrentWord();
}

// Display current word and definition
function displayCurrentWord() {
    if (currentWordIndex < vocabulary.length) {
        const currentWord = vocabulary[currentWordIndex];
        wordDisplay.textContent = currentWord.word;
        definitionDisplay.textContent = '';
    } else {
        endGame();
    }
}

// Show definition and prepare for next word
function nextWord() {
    if (!gameActive) return;
    
    // Show definition
    definitionDisplay.textContent = vocabulary[currentWordIndex].definition;
    
    // Increment score and index
    score++;
    currentWordIndex++;
    updateScore();
    
    // Delay next word display
    setTimeout(() => {
        displayCurrentWord();
    }, 2000);
}

// Update score display
function updateScore() {
    scoreDisplay.textContent = `Score: ${score}/${vocabulary.length}`;
}

// End the game
function endGame() {
    gameActive = false;
    wordDisplay.textContent = 'Game Over!';
    definitionDisplay.textContent = `Final Score: ${score}/${vocabulary.length}`;
    nextButton.style.display = 'none';
    
    // Show restart button after delay
    setTimeout(() => {
        startButton.textContent = 'Play Again';
        startButton.style.display = 'block';
    }, 1500);
}

// Initialize the game when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    initGame();
});
```

HTML template to use with the JavaScript:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metal and Mineral Vocabulary Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        #game-container {
            display: none;
            margin-top: 20px;
        }
        #word-display {
            font-size: 2em;
            margin: 20px 0;
            font-weight: bold;
        }
        #definition-display {
            min-height: 100px;
            margin: 20px 0;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            font-size: 1em;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        #score {
            font-size: 1.2em;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Metal and Mineral Vocabulary Game</h1>
    <p>Learn English vocabulary related to metals and minerals!</p>
    
    <button id="start-btn">Start Game</button>
    
    <div id="game-container">
        <div id="score">Score: 0/10</div>
        <div id="word-display"></div>
        <div id="definition-display"></div>
        <button id="next-btn">Show Definition</button>
    </div>

    <script src="game.js"></script>
</body>
</html>
```
