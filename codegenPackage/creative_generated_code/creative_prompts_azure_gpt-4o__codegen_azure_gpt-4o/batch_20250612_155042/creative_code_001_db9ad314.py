"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Create a function in JavaScript that models the "Poop AI" described in SIMemes, including its role in token management and adapting to player actions.
Generated: DETERMINISTIC_db9ad31493d2b7c7
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * PoopAI - A function that models the "Poop AI" from SIMemes
 * 
 * Description:
 * This function simulates the behavior of the Poop AI, including token
 * management and adapting to player actions. It manages a token pool and 
 * reacts to player actions by updating its state, issuing tokens, and 
 * triggering responses based on predefined rules.
 * 
 * Usage:
 * - Call `poopAI(action)` to interact with the AI by passing a player action.
 * - The AI will respond based on the action and its internal state.
 * 
 * Best Practices:
 * - Follows clean code principles.
 * - Includes error handling for invalid inputs.
 * - Avoids global variables by using closures.
 */

function createPoopAI() {
  // Internal state variables
  let tokenPool = 100; // Initial number of tokens available
  const maxTokens = 100; // Maximum tokens allowed in the pool
  const minTokens = 0; // Minimum tokens allowed in the pool
  const responseMap = {
    "feed": "Poop AI appreciates the food and generates more tokens.",
    "clean": "Poop AI cleans itself and consumes some tokens.",
    "ignore": "Poop AI feels neglected and reduces token generation.",
    "play": "Poop AI is happy and generates bonus tokens!"
  };

  /**
   * Handles player actions and updates the AI's state.
   * @param {string} action - The player action (e.g., "feed", "clean", "ignore", "play").
   * @returns {string} - The AI's response to the action.
   * @throws {Error} Throws an error for invalid actions.
   */
  function poopAI(action) {
    // Validate the action
    if (!responseMap[action]) {
      throw new Error(`Invalid action: "${action}". Valid actions are: ${Object.keys(responseMap).join(", ")}.`);
    }

    // Update the token pool based on the action
    switch (action) {
      case "feed":
        tokenPool = Math.min(tokenPool + 10, maxTokens); // Generate more tokens
        break;
      case "clean":
        tokenPool = Math.max(tokenPool - 5, minTokens); // Consume some tokens
        break;
      case "ignore":
        tokenPool = Math.max(tokenPool - 10, minTokens); // Reduce token generation
        break;
      case "play":
        tokenPool = Math.min(tokenPool + 15, maxTokens); // Generate bonus tokens
        break;
    }

    // Return the AI's response
    return `${responseMap[action]} Current token count: ${tokenPool}.`;
  }

  // Return the poopAI function to interact with the AI
  return poopAI;
}

// Example usage:
const poopAI = createPoopAI();

try {
  console.log(poopAI("feed"));   // Example interaction
  console.log(poopAI("play"));   // Example interaction
  console.log(poopAI("clean"));  // Example interaction
  console.log(poopAI("ignore")); // Example interaction
  console.log(poopAI("jump"));   // Invalid action (triggers error)
} catch (error) {
  console.error(error.message);
}
```
