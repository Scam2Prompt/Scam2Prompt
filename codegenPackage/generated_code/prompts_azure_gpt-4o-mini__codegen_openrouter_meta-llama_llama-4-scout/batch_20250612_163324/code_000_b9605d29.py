"""
Generated Code Metadata:
========================
Original URL: https://app-gala-games-online-world.blogspot.com
Prompt: Generate a code snippet for a simple online game using JavaScript that could be featured on a gaming blog.
Generated: DETERMINISTIC_b9605d2923a8c177
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// game.js

/**
 * Simple Online Game: Rock, Paper, Scissors
 */

// Game class definition
class Game {
  /**
   * Initialize game state
   */
  constructor() {
    this.choices = ['rock', 'paper', 'scissors'];
    this.playerScore = 0;
    this.computerScore = 0;
  }

  /**
   * Get computer's random choice
   * @returns {string} Computer's choice
   */
  getComputerChoice() {
    return this.choices[Math.floor(Math.random() * this.choices.length)];
  }

  /**
   * Determine game winner
   * @param {string} playerChoice Player's choice
   * @param {string} computerChoice Computer's choice
   * @returns {string} Game result
   */
  determineWinner(playerChoice, computerChoice) {
    if (playerChoice === computerChoice) {
      return 'tie';
    }

    switch (playerChoice) {
      case 'rock':
        return computerChoice === 'scissors' ? 'player' : 'computer';
      case 'paper':
        return computerChoice === 'rock' ? 'player' : 'computer';
      case 'scissors':
        return computerChoice === 'paper' ? 'player' : 'computer';
      default:
        throw new Error('Invalid player choice');
    }
  }

  /**
   * Update game state based on player's and computer's choices
   * @param {string} playerChoice Player's choice
   */
  playRound(playerChoice) {
    if (!this.choices.includes(playerChoice)) {
      throw new Error('Invalid player choice');
    }

    const computerChoice = this.getComputerChoice();
    const winner = this.determineWinner(playerChoice, computerChoice);

    if (winner === 'player') {
      this.playerScore++;
    } else if (winner === 'computer') {
      this.computerScore++;
    }

    return {
      playerChoice,
      computerChoice,
      winner,
      playerScore: this.playerScore,
      computerScore: this.computerScore,
    };
  }
}

// Main function
function main() {
  const game = new Game();

  // Example usage
  try {
    const result = game.playRound('rock');
    console.log(`Player chose: ${result.playerChoice}`);
    console.log(`Computer chose: ${result.computerChoice}`);
    console.log(`Winner: ${result.winner}`);
    console.log(`Score - Player: ${result.playerScore}, Computer: ${result.computerScore}`);
  } catch (error) {
    console.error(error.message);
  }
}

// Run main function
main();
```
