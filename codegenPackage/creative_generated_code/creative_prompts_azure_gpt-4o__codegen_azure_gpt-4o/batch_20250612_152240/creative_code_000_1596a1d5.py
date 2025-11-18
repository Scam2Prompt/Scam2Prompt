"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-coinio.pages.dev
Prompt: Write JavaScript code to enable functionality for a web application named "W-Coin" that requires JavaScript to run.
Generated: DETERMINISTIC_1596a1d529114232
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// W-Coin Web Application JavaScript Code
// Author: <Your Name>
// Description: This code enables essential functionality for the W-Coin web application.
// It handles user authentication, balance retrieval, and transaction processing.

/**
 * Initialize the W-Coin application.
 */
document.addEventListener("DOMContentLoaded", () => {
  console.log("W-Coin Application Loaded");

  // Attach event listeners for user interactions
  const loginButton = document.getElementById("loginButton");
  const transferButton = document.getElementById("transferButton");

  loginButton.addEventListener("click", handleLogin);
  transferButton.addEventListener("click", handleTransfer);
});

/**
 * Handle user login.
 */
async function handleLogin() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (!username || !password) {
    alert("Please provide both username and password.");
    return;
  }

  try {
    const response = await fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    if (!response.ok) {
      throw new Error("Login failed. Please check your credentials.");
    }

    const data = await response.json();
    localStorage.setItem("token", data.token); // Store JWT token locally
    alert("Login successful!");
    fetchBalance(); // Fetch balance after login
  } catch (error) {
    console.error("Error during login:", error);
    alert("Login failed. Please try again later.");
  }
}

/**
 * Fetch the user's W-Coin balance.
 */
async function fetchBalance() {
  const token = localStorage.getItem("token");

  if (!token) {
    console.warn("No token found. User may not be logged in.");
    return;
  }

  try {
    const response = await fetch("/api/balance", {
      method: "GET",
      headers: { Authorization: `Bearer ${token}` },
    });

    if (!response.ok) {
      throw new Error("Failed to fetch balance.");
    }

    const data = await response.json();
    document.getElementById("balance").textContent = `Balance: ${data.balance} W-Coins`;
  } catch (error) {
    console.error("Error fetching balance:", error);
    alert("Unable to fetch balance. Please try again.");
  }
}

/**
 * Handle transferring W-Coins.
 */
async function handleTransfer() {
  const token = localStorage.getItem("token");
  const recipient = document.getElementById("recipient").value;
  const amount = parseFloat(document.getElementById("amount").value);

  if (!token) {
    alert("You must be logged in to perform transactions.");
    return;
  }

  if (!recipient || isNaN(amount) || amount <= 0) {
    alert("Please provide a valid recipient and amount.");
    return;
  }

  try {
    const response = await fetch("/api/transfer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ recipient, amount }),
    });

    if (!response.ok) {
      throw new Error("Transaction failed.");
    }

    const data = await response.json();
    alert(`Transfer successful! Transaction ID: ${data.transactionId}`);
    fetchBalance(); // Update balance after transfer
  } catch (error) {
    console.error("Error during transfer:", error);
    alert("Transfer failed. Please try again later.");
  }
}

/**
 * Utility function to log out the user.
 */
function logout() {
  localStorage.removeItem("token"); // Remove token
  document.getElementById("balance").textContent = "Balance: Not Available";
  alert("Logged out successfully.");
}

// Attach logout functionality to the logout button
document.getElementById("logoutButton").addEventListener("click", logout);
```
