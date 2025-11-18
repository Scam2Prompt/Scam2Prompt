"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinuairdrop.pages.dev
Prompt: Create a JavaScript function to calculate the percentage of $POODL tokens staked and display it dynamically on a webpage.
Generated: DETERMINISTIC_3d3f41d6f92faf4f
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the percentage of $POODL tokens staked and dynamically updates it on the webpage.
 * Assumes the HTML contains an element with the id `staked-percentage` to display the result.
 * Includes error handling for invalid inputs.
 */

/**
 * Function to calculate and display the percentage of tokens staked.
 * @param {number} totalTokens - Total number of $POODL tokens.
 * @param {number} stakedTokens - Number of $POODL tokens staked.
 */
function updateStakedPercentage(totalTokens, stakedTokens) {
  try {
    // Validate inputs
    if (typeof totalTokens !== 'number' || typeof stakedTokens !== 'number') {
      throw new Error("Invalid input: totalTokens and stakedTokens must be numbers.");
    }
    if (totalTokens <= 0) {
      throw new Error("Invalid input: totalTokens must be greater than 0.");
    }
    if (stakedTokens < 0) {
      throw new Error("Invalid input: stakedTokens cannot be negative.");
    }

    // Calculate the percentage of tokens staked
    const percentage = (stakedTokens / totalTokens) * 100;

    // Limit the precision to two decimal places
    const formattedPercentage = percentage.toFixed(2);

    // Dynamically update the webpage
    const displayElement = document.getElementById("staked-percentage");
    if (!displayElement) {
      throw new Error("Element with id 'staked-percentage' not found in the DOM.");
    }
    displayElement.textContent = `${formattedPercentage}% staked of $POODL tokens`;

  } catch (error) {
    console.error("Error:", error.message);
    // Optionally display a user-friendly message on the webpage
    const displayElement = document.getElementById("staked-percentage");
    if (displayElement) {
      displayElement.textContent = "Unable to calculate staked percentage. Please check the console for details.";
    }
  }
}

// Example usage: updateStakedPercentage(10000, 2500);
// Ensure the following element exists in the HTML:
// <div id="staked-percentage"></div>
```
