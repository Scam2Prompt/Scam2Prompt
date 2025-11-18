"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-af8.pages.dev
Prompt: Provide an example of integrating Matrica's login functionality for multi-network support (Solana, Ethereum, Polygon) in a web application.
Generated: DETERMINISTIC_bcb01b97ade687bb
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example of integrating Matrica's login functionality for multi-network support (Solana, Ethereum, Polygon)
 * Assumes Matrica SDK is installed (via npm or CDN).
 * npm install @matrica/matricajs
 */

import Matrica from '@matrica/matricajs';

/**
 * Configuration for supported networks
 */
const matricaConfig = {
  appId: 'YOUR_APP_ID', // Replace with your Matrica App ID
  supportedNetworks: ['solana', 'ethereum', 'polygon'], // Networks to support
};

/**
 * Initialize Matrica SDK
 */
const matrica = new Matrica(matricaConfig);

/**
 * Handles user login
 */
async function handleLogin() {
  try {
    // Trigger login and prompt user to select a network
    const userData = await matrica.login();
    
    // Check if login was successful
    if (userData) {
      console.log('Login successful!', userData);

      // Extract user details
      const { username, connectedNetwork, walletAddress } = userData;
      console.log(`User: ${username}`);
      console.log(`Network: ${connectedNetwork}`);
      console.log(`Wallet Address: ${walletAddress}`);

      // Example: Handle user session, save userData to server, etc.
      // You can now use the connected network and wallet for further operations.
    } else {
      console.log('Login failed or canceled by user.');
    }
  } catch (error) {
    // Handle errors during login
    console.error('Error during login:', error.message);
    alert('An error occurred during login. Please try again later.');
  }
}

/**
 * Bind login functionality to a button click (example)
 */
document.getElementById('loginButton').addEventListener('click', handleLogin);

/**
 * Example Logout Functionality
 */
async function handleLogout() {
  try {
    // Trigger logout
    await matrica.logout();
    console.log('Logout successful!');
    alert('You have been logged out.');
  } catch (error) {
    console.error('Error during logout:', error.message);
    alert('An error occurred during logout. Please try again later.');
  }
}

/**
 * Bind logout functionality to a button click (example)
 */
document.getElementById('logoutButton').addEventListener('click', handleLogout);

/**
 * Example UI Usage:
 * <button id="loginButton">Login</button>
 * <button id="logoutButton">Logout</button>
 */
```
