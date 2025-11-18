"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Develop a slot machine simulation in JavaScript, incorporating themes and payout rules similar to the "Nổ Hũ" games on S666.
Generated: DETERMINISTIC_daa2959262d3c755
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Slot Machine Simulation in JavaScript
// This program simulates a simple slot machine game with themes, symbols, and payout rules.

// Constants for the game configuration
const SYMBOLS = ["🍒", "🍋", "🍇", "🔔", "💎", "⭐"]; // Thematic symbols
const REELS_COUNT = 3; // Number of reels in the slot machine
const PAYOUT_MULTIPLIERS = {
  "🍒🍒🍒": 10, // Cherry triple
  "🍋🍋🍋": 5, // Lemon triple
  "🍇🍇🍇": 8, // Grapes triple
  "🔔🔔🔔": 15, // Bell triple
  "💎💎💎": 50, // Diamond triple
  "⭐⭐⭐": 100, // Star triple (highest payout)
};
const INITIAL_BALANCE = 100; // Starting balance for the user
const SPIN_COST = 5; // Cost per spin

// Function to spin the slot machine
function spinReels() {
  // Randomly selects a symbol for each reel
  return Array.from({ length: REELS_COUNT }, () => SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)]);
}

// Function to calculate winnings based on the result
function calculatePayout(reels) {
  const resultString = reels.join(""); // Concatenate reels into a string
  return PAYOUT_MULTIPLIERS[resultString] || 0; // Return payout multiplier if match exists, else 0
}

// Main game logic
function playSlotMachine() {
  let balance = INITIAL_BALANCE; // Initialize user balance

  console.log("Welcome to the Slot Machine Game!");
  console.log(`Your starting balance is $${balance}.`);

  // Main game loop
  while (balance >= SPIN_COST) {
    console.log("\nSpinning the reels...");

    // Deduct spin cost and spin the reels
    balance -= SPIN_COST;
    const reels = spinReels();

    // Display the reels result
    console.log("Reels:", reels.join(" | "));

    // Calculate winnings and update balance
    const payoutMultiplier = calculatePayout(reels);
    const winnings = payoutMultiplier * SPIN_COST;
    balance += winnings;

    // Display result of the spin
    if (payoutMultiplier > 0) {
      console.log(`Congratulations! You won $${winnings} with a payout multiplier of x${payoutMultiplier}.`);
    } else {
      console.log("No win this time. Better luck next spin!");
    }

    console.log(`Your current balance is $${balance}.`);

    // Check if the user wants to continue playing
    if (balance >= SPIN_COST) {
      const continuePlaying = prompt("Do you want to spin again? (yes/no): ").toLowerCase();
      if (continuePlaying !== "yes") {
        console.log("Thanks for playing! Your final balance is $", balance);
        return; // End the game
      }
    } else {
      console.log("You don't have enough balance to spin again. Game over!");
      return; // End the game
    }
  }
}

// Run the game
playSlotMachine();
```

**Note:** The `prompt` function is used for user input, which works in the browser environment. For Node.js, you would need to use a library like `readline` for similar functionality.
