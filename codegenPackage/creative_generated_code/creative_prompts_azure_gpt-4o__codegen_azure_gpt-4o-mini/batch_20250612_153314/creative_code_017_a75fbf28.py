"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betfur.pages.dev
Prompt: Write a JavaScript function to simulate gameplay for BetFury's Tower game, incorporating the Hotkey feature for simplified controls.
Generated: DETERMINISTIC_a75fbf2871d726d1
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Tower Game Simulator for BetFury with Hotkey Feature
class TowerGame {
    constructor() {
        this.level = 0; // Current level
        this.maxLevel = 10; // Maximum level to reach
        this.isGameActive = false; // Flag to check if the game is active
    }

    // Start the game
    startGame() {
        this.level = 0;
        this.isGameActive = true;
        console.log("Game Started! Reach the top of the tower.");
        this.play();
    }

    // Simulate gameplay
    play() {
        if (!this.isGameActive) return;

        console.log(`Current Level: ${this.level}`);
        
        // Simulate a level up
        setTimeout(() => {
            if (this.level < this.maxLevel) {
                this.level++;
                this.play();
            } else {
                this.endGame();
            }
        }, 1000); // Simulate a delay for the next level
    }

    // End the game
    endGame() {
        this.isGameActive = false;
        console.log(`Congratulations! You reached level ${this.maxLevel}. Game Over.`);
    }
    
    // Handle user input for hotkeys
    handleHotkey(key) {
        if (!this.isGameActive) {
            console.log("Game is not active. Please start the game first.");
            return;
        }

        switch (key) {
            case 'r': // Restart the game
                this.startGame();
                break;
            case 'q': // Quit the game
                this.endGame();
                break;
            default:
                console.log("Invalid hotkey. Use 'r' to restart or 'q' to quit.");
        }
    }
}

// Example usage
const towerGame = new TowerGame();
towerGame.startGame();

// Simulate hotkey events for demonstration purposes
setTimeout(() => towerGame.handleHotkey('r'), 5000); // Restart after 5 seconds
setTimeout(() => towerGame.handleHotkey('q'), 15000); // Quit after 15 seconds
```
