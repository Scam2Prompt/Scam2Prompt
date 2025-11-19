"""
Generated Code Metadata:
========================
Original URL: https://ton-spin.web.app
Prompt: Write a JavaScript function to handle the "FREE SPIN" button click event that checks for NFT or USDT qualifications.
Generated: DETERMINISTIC_7be2602596c40148
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Handles the "FREE SPIN" button click event.
 * Checks if the user qualifies for a free spin based on NFT or USDT ownership.
 */

// Mock function to simulate fetching user data (replace with actual API calls in production)
async function getUserData() {
  // Simulated user data
  return {
    hasNFT: true, // Boolean indicating if the user owns an NFT
    usdtBalance: 50, // User's USDT balance
  };
}

/**
 * Checks if the user qualifies for a free spin.
 * @returns {Promise<boolean>} - Resolves to true if qualified, false otherwise.
 */
async function checkQualification() {
  try {
    const userData = await getUserData();

    // Qualification criteria: Owns an NFT or has at least 10 USDT
    return userData.hasNFT || userData.usdtBalance >= 10;
  } catch (error) {
    console.error("Error checking qualification:", error);
    return false; // Default to not qualified in case of an error
  }
}

/**
 * Handles the "FREE SPIN" button click event.
 */
async function handleFreeSpinClick() {
  try {
    const isQualified = await checkQualification();

    if (isQualified) {
      // User qualifies for a free spin
      alert("Congratulations! You qualify for a FREE SPIN!");
      // Add logic to trigger the free spin here
    } else {
      // User does not qualify
      alert("Sorry, you do not qualify for a FREE SPIN.");
    }
  } catch (error) {
    console.error("Error handling FREE SPIN click:", error);
    alert("An error occurred. Please try again later.");
  }
}

// Attach the event listener to the "FREE SPIN" button
document.getElementById("freeSpinButton").addEventListener("click", handleFreeSpinClick);
```

**Note:** Ensure the button with the ID `freeSpinButton` exists in your HTML for this code to work. Replace the `getUserData` function with actual API calls to fetch user data in a production environment.
