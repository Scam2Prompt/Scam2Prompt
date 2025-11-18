"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learn--metamaskio-web.bravesites.com
Prompt: Recommend best practices for handling private keys and sensitive data when integrating MetaMask login functionality into a Web3 application.
Generated: DETERMINISTIC_489f84fd4c14b242
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const Web3 = require('web3'); // For interacting with the Ethereum blockchain
require('dotenv').config(); // For managing environment variables securely

// Best practices
// 1. Always store sensitive data like private keys in secure environment variables.
// 2. Use MetaMask for private key management instead of handling private keys directly.
// 3. Implement proper error handling.
// 4. Never expose sensitive data such as private keys to the client-side code.

// Initialize Web3 instance
let web3;

// Function to initialize Web3 with MetaMask
async function initializeWeb3() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
      // Use MetaMask's provider
      web3 = new Web3(window.ethereum);

      // Request access to accounts
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      console.log('MetaMask connected successfully.');
    } else {
      throw new Error('MetaMask is not installed. Please install MetaMask and try again.');
    }
  } catch (error) {
    console.error('Error initializing Web3:', error.message);
    throw error; // Rethrow the error for further handling
  }
}

// Function to get the current MetaMask account
async function getCurrentAccount() {
  try {
    // Ensure Web3 has been initialized
    if (!web3) {
      throw new Error('Web3 not initialized. Call initializeWeb3() first.');
    }

    // Get accounts from MetaMask
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
      throw new Error('No accounts found. Ensure MetaMask is unlocked and an account is selected.');
    }

    console.log('Current MetaMask account:', accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error('Error fetching accounts:', error.message);
    throw error; // Rethrow the error for further handling
  }
}

// Example: Calling the functions
(async () => {
  try {
    // Initialize MetaMask connection
    await initializeWeb3();

    // Get the logged-in MetaMask account
    const account = await getCurrentAccount();

    // Use the account in your application logic
    console.log('Logged-in account:', account);
  } catch (error) {
    console.error('Error in MetaMask integration:', error.message);
  }
})();

// Environment Variables (Example: .env file)
// Never hardcode sensitive data!
// PRIVATE_KEY=your_private_key_here
```
