"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://private-gomble.pages.dev
Prompt: Write JavaScript code for a simple event-based game where users can "heat a balloon" and track its height, inspired by the mechanics described in GOMBLE's "Heat the Balloon" game.
Generated: DETERMINISTIC_2ff97f4bcf99347b
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Balloon Heating Game
// This is a simple game where users can "heat" a balloon to increase its height.
// The game tracks the height of the balloon, and if it gets too high, the balloon pops.

// Constants for the game
const MAX_HEIGHT = 100; // Maximum height before the balloon pops
const HEAT_INCREMENT = 5; // Height increase per heat
const GAME_INTERVAL = 100; // Game update interval in milliseconds

// Variables to track game state
let balloonHeight = 0; // Current height of the balloon
let gameRunning = true; // Is the game currently running?

// DOM Elements
const balloonElement = document.getElementById('balloon'); // Balloon display element
const heightElement = document.getElementById('height'); // Height display element
const messageElement = document.getElementById('message'); // Message display element
const heatButton = document.getElementById('heatButton'); // Button to heat the balloon

// Function to heat the balloon
function heatBalloon() {
  if (!gameRunning) return; // Do nothing if the game is over

  balloonHeight += HEAT_INCREMENT; // Increase the balloon's height
  updateBalloonDisplay(); // Update the UI

  // Check if the balloon has popped
  if (balloonHeight >= MAX_HEIGHT) {
    balloonPopped();
  }
}

// Function to handle when the balloon pops
function balloonPopped() {
  gameRunning = false; // Stop the game
  messageElement.textContent = 'The balloon popped! Game over.'; // Display game over message
  heatButton.disabled = true; // Disable the heat button
}

// Function to update the balloon height on the UI
function updateBalloonDisplay() {
  heightElement.textContent = `Height: ${balloonHeight}`; // Update height display
  balloonElement.style.transform = `translateY(${-balloonHeight}px)`; // Move the balloon up visually
}

// Function to reset the game
function resetGame() {
  balloonHeight = 0; // Reset height
  gameRunning = true; // Restart the game
  messageElement.textContent = ''; // Clear the message
  heatButton.disabled = false; // Enable the heat button
  updateBalloonDisplay(); // Update the UI
}

// Event Listener for Heating the Balloon
heatButton.addEventListener('click', heatBalloon);

// Optional: Reset game manually (add this functionality in your HTML if needed)
// document.getElementById('resetButton').addEventListener('click', resetGame);

// Initial UI Update
updateBalloonDisplay();
```

HTML structure example for the code to work:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heat the Balloon Game</title>
  <style>
    #gameContainer {
      text-align: center;
      margin-top: 50px;
    }
    #balloon {
      width: 50px;
      height: 70px;
      background-color: red;
      border-radius: 50%;
      margin: 0 auto;
      position: relative;
    }
    #heatButton, #resetButton {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div id="gameContainer">
    <div id="balloon"></div>
    <p id="height">Height: 0</p>
    <p id="message"></p>
    <button id="heatButton">Heat Balloon</button>
    <button id="resetButton" onclick="resetGame()">Reset Game</button>
  </div>
  <script src="game.js"></script>
</body>
</html>
```
