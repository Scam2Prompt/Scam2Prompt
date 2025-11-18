"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-support-number-pro.blogspot.com
Prompt: Create a function in JavaScript that simulates navigating the Coinbase Support phone menu system based on the information provided on the webpage.
Generated: DETERMINISTIC_944e424fe7aad299
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates navigating the Coinbase Support phone menu system.
 * @param {Array<string>} menuSelections - Array of user selections to navigate through the menu.
 * @returns {string} - Final outcome or message based on user selections.
 */
function navigateCoinbaseSupportMenu(menuSelections) {
  // Define the menu structure as a nested object
  const supportMenu = {
    "1": { // Account and Security
      "1": "Reset Password",
      "2": "Account Verification",
      "3": "Two-Factor Authentication",
    },
    "2": { // Payments and Transfers
      "1": "Bank Account Linking",
      "2": "Troubleshooting Failed Transactions",
      "3": "Refund Inquiry",
    },
    "3": { // Crypto Support
      "1": "Buying Cryptocurrencies",
      "2": "Selling Cryptocurrencies",
      "3": "Wallet Troubleshooting",
    },
    "4": "Speak to a Representative", // Direct option
  };

  try {
    let currentMenu = supportMenu; // Start at the root of the menu

    for (let selection of menuSelections) {
      if (typeof currentMenu === "string") {
        // If we've reached a final option, stop further navigation
        throw new Error("Invalid selection: You cannot navigate further.");
      }

      // Check if the selection exists in the current menu
      if (!currentMenu.hasOwnProperty(selection)) {
        throw new Error("Invalid menu selection. Please try again.");
      }

      // Move to the next level based on the selection
      currentMenu = currentMenu[selection];
    }

    // If the final menu item is a string, we've reached the end
    if (typeof currentMenu === "string") {
      return `You have selected: ${currentMenu}`;
    }

    // If we end on a submenu, it means the user didn't complete a valid navigation
    throw new Error("Incomplete menu navigation. Please select a complete path.");
  } catch (error) {
    return `Error: ${error.message}`;
  }
}

// Example usage:
// User navigates: "Account and Security" -> "Two-Factor Authentication"
const result = navigateCoinbaseSupportMenu(["1", "3"]);
console.log(result); // Output: "You have selected: Two-Factor Authentication"
```
