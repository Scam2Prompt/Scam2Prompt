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
// Vocabulary Game: Metal and Mineral Vocabulary
// This game helps users learn English vocabulary related to metals and minerals.
// Users are presented with a word and must select the correct definition from multiple choices.

// List of vocabulary words and their definitions
const vocabulary = [
  { word: "Iron", definition: "A strong, hard magnetic metal used in construction and manufacturing." },
  { word: "Copper", definition: "A reddish-brown metal used in electrical wiring and coins." },
  { word: "Gold", definition: "A precious yellow metal valued for its beauty and rarity." },
  { word: "Silver", definition: "A shiny white metal used in jewelry and tableware." },
  { word: "Aluminum", definition: "A lightweight, silvery metal used in packaging and construction." },
  { word: "Quartz", definition: "A hard, crystalline mineral often used in watches and electronics." },
  { word: "Diamond", definition: "A precious gemstone made of pure carbon, known for its hardness." },
  { word: "Lead", definition: "A heavy, soft metal used in batteries and radiation shielding." },
  { word: "Zinc", definition: "A bluish-white metal used to galvanize steel and in alloys." },
  { word: "Platinum", definition: "A rare, silvery-white metal used in jewelry and industrial applications." }
];

// Shuffle array utility function
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

// Game state
let currentWordIndex = 0;
let score = 0;

// DOM elements
const wordElement = document.getElementById("word");
const choicesElement = document.getElementById("choices");
const scoreElement = document.getElementById("score");
const messageElement = document.getElementById("message");

// Initialize the game
function startGame() {
  currentWordIndex = 0;
  score = 0;
  scoreElement.textContent = `Score: ${score}`;
  messageElement.textContent = "";
  loadNextWord();
}

// Load the next word and choices
function loadNextWord() {
  if (currentWordIndex >= vocabulary.length) {
    endGame();
    return;
  }

  const currentWord = vocabulary[currentWordIndex];
  wordElement.textContent = `Word: ${currentWord.word}`;

  // Generate choices (correct + random incorrect definitions)
  const choices = [currentWord.definition];
  while (choices.length < 4) {
    const randomIndex = Math.floor(Math.random() * vocabulary.length);
    const randomDefinition = vocabulary[randomIndex].definition;
    if (!choices.includes(randomDefinition)) {
      choices.push(randomDefinition);
    }
  }

  // Shuffle choices
  shuffleArray(choices);

  // Render choices
  choicesElement.innerHTML = "";
  choices.forEach((choice) => {
    const button = document.createElement("button");
    button.textContent = choice;
    button.addEventListener("click", () => handleChoice(choice));
    choicesElement.appendChild(button);
  });
}

// Handle user's choice
function handleChoice(selectedDefinition) {
  const currentWord = vocabulary[currentWordIndex];
  if (selectedDefinition === currentWord.definition) {
    score++;
    messageElement.textContent = "Correct!";
  } else {
    messageElement.textContent = `Incorrect! The correct answer was: ${currentWord.definition}`;
  }

  scoreElement.textContent = `Score: ${score}`;
  currentWordIndex++;
  setTimeout(() => {
    messageElement.textContent = "";
    loadNextWord();
  }, 2000);
}

// End the game
function endGame() {
  wordElement.textContent = "Game Over!";
  choicesElement.innerHTML = "";
  messageElement.textContent = `Your final score is: ${score}`;
}

// Start the game when the page loads
document.addEventListener("DOMContentLoaded", () => {
  startGame();
});
```

### HTML Structure (to be used with the JavaScript code above):
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vocabulary Game</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 20px;
    }
    #choices button {
      margin: 5px;
      padding: 10px 20px;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <h1>Metal and Mineral Vocabulary Game</h1>
  <div id="word"></div>
  <div id="choices"></div>
  <div id="score"></div>
  <div id="message"></div>
  <script src="game.js"></script>
</body>
</html>
```
