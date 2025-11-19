"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Design a token utility system using JavaScript that allows holders to access exclusive content, participate in contests, and exchange tokens for real-world prizes, as described in METAL's token utility.
Generated: DETERMINISTIC_defbc9fd53e8e779
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Token Utility System for METAL's Token Utility
// This system allows token holders to access exclusive content, participate in contests, and exchange tokens for real-world prizes.

// Define the TokenUtility class
class TokenUtility {
  constructor() {
    // Initialize token holders and their balances
    this.tokenHolders = new Map(); // Map to store user balances
    this.exclusiveContent = []; // Array to store exclusive content
    this.contests = []; // Array to store active contests
    this.prizes = []; // Array to store available prizes
  }

  // Add a new token holder
  addTokenHolder(userId, initialBalance = 0) {
    if (this.tokenHolders.has(userId)) {
      throw new Error("User already exists.");
    }
    this.tokenHolders.set(userId, initialBalance);
  }

  // Get the token balance of a user
  getTokenBalance(userId) {
    if (!this.tokenHolders.has(userId)) {
      throw new Error("User not found.");
    }
    return this.tokenHolders.get(userId);
  }

  // Add tokens to a user's balance
  addTokens(userId, amount) {
    if (!this.tokenHolders.has(userId)) {
      throw new Error("User not found.");
    }
    if (amount <= 0) {
      throw new Error("Amount must be greater than zero.");
    }
    const currentBalance = this.tokenHolders.get(userId);
    this.tokenHolders.set(userId, currentBalance + amount);
  }

  // Deduct tokens from a user's balance
  deductTokens(userId, amount) {
    if (!this.tokenHolders.has(userId)) {
      throw new Error("User not found.");
    }
    if (amount <= 0) {
      throw new Error("Amount must be greater than zero.");
    }
    const currentBalance = this.tokenHolders.get(userId);
    if (currentBalance < amount) {
      throw new Error("Insufficient balance.");
    }
    this.tokenHolders.set(userId, currentBalance - amount);
  }

  // Add exclusive content
  addExclusiveContent(content) {
    if (!content || typeof content !== "string") {
      throw new Error("Invalid content.");
    }
    this.exclusiveContent.push(content);
  }

  // Get all exclusive content
  getExclusiveContent() {
    return this.exclusiveContent;
  }

  // Add a contest
  addContest(contestDetails) {
    if (!contestDetails || typeof contestDetails !== "string") {
      throw new Error("Invalid contest details.");
    }
    this.contests.push(contestDetails);
  }

  // Get all active contests
  getContests() {
    return this.contests;
  }

  // Add a prize
  addPrize(prizeDetails) {
    if (!prizeDetails || typeof prizeDetails !== "string") {
      throw new Error("Invalid prize details.");
    }
    this.prizes.push(prizeDetails);
  }

  // Get all available prizes
  getPrizes() {
    return this.prizes;
  }

  // Exchange tokens for a prize
  exchangeTokensForPrize(userId, prizeIndex, tokenCost) {
    if (!this.tokenHolders.has(userId)) {
      throw new Error("User not found.");
    }
    if (prizeIndex < 0 || prizeIndex >= this.prizes.length) {
      throw new Error("Invalid prize index.");
    }
    if (tokenCost <= 0) {
      throw new Error("Token cost must be greater than zero.");
    }
    const currentBalance = this.tokenHolders.get(userId);
    if (currentBalance < tokenCost) {
      throw new Error("Insufficient balance.");
    }
    // Deduct tokens and return the prize
    this.tokenHolders.set(userId, currentBalance - tokenCost);
    return this.prizes[prizeIndex];
  }
}

// Example usage
try {
  const tokenUtility = new TokenUtility();

  // Add token holders
  tokenUtility.addTokenHolder("user1", 100);
  tokenUtility.addTokenHolder("user2", 50);

  // Add exclusive content
  tokenUtility.addExclusiveContent("Exclusive Video 1");
  tokenUtility.addExclusiveContent("Exclusive Article 1");

  // Add contests
  tokenUtility.addContest("Contest 1: Win a trip to Hawaii");
  tokenUtility.addContest("Contest 2: Win a gaming console");

  // Add prizes
  tokenUtility.addPrize("Prize 1: $50 Gift Card");
  tokenUtility.addPrize("Prize 2: Custom METAL Merchandise");

  // Exchange tokens for a prize
  const prize = tokenUtility.exchangeTokensForPrize("user1", 0, 50);
  console.log(`User1 exchanged tokens for: ${prize}`);

  // Get token balance
  console.log(`User1's remaining balance: ${tokenUtility.getTokenBalance("user1")}`);

  // Get exclusive content
  console.log("Exclusive Content:", tokenUtility.getExclusiveContent());

  // Get contests
  console.log("Active Contests:", tokenUtility.getContests());

  // Get prizes
  console.log("Available Prizes:", tokenUtility.getPrizes());
} catch (error) {
  console.error("Error:", error.message);
}
```
