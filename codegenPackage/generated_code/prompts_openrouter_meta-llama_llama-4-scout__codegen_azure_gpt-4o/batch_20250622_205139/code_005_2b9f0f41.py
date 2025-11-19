"""
Generated Code Metadata:
========================
Original URL: https://magic.link
Prompt: "Design a user-friendly onboarding process for a new user to interact with an on-chain application using Magic Labs' wallet abstraction tools."
Generated: DETERMINISTIC_2b9f0f4125632dbd
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { Magic } from 'magic-sdk'; // Magic SDK for wallet abstraction
import Web3 from 'web3'; // Web3 for blockchain interaction

// Configuration for Magic SDK
const magic = new Magic('YOUR_MAGIC_PUBLISHABLE_API_KEY', {
  network: 'mainnet', // Change to 'rinkeby', 'goerli', etc., for test networks
});

// Initialize Web3 instance using Magic's provider
const web3 = new Web3(magic.rpcProvider);

// Function to handle user onboarding
async function onboardUser() {
  try {
    // Step 1: Prompt user to log in or sign up
    const email = prompt('Please enter your email to get started:');
    if (!email) {
      throw new Error('Email is required to proceed.');
    }

    // Step 2: Authenticate user with Magic
    await magic.auth.loginWithMagicLink({ email });
    console.log('User successfully logged in.');

    // Step 3: Fetch user's wallet address
    const userAddress = (await web3.eth.getAccounts())[0];
    console.log(`User's wallet address: ${userAddress}`);

    // Step 4: Display user-friendly message
    alert(`Welcome! Your wallet address is ${userAddress}. You are now ready to interact with the application.`);

    // Step 5: Example interaction with the blockchain (e.g., fetching balance)
    const balance = await web3.eth.getBalance(userAddress);
    console.log(`Wallet balance: ${web3.utils.fromWei(balance, 'ether')} ETH`);

    // Display balance to the user
    alert(`Your wallet balance is ${web3.utils.fromWei(balance, 'ether')} ETH.`);
  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred during onboarding:', error);
    alert(`An error occurred: ${error.message}`);
  }
}

// Attach the onboarding function to a button click event
document.getElementById('onboardButton').addEventListener('click', onboardUser);

// HTML structure for the onboarding button
document.body.innerHTML = `
  <div style="text-align: center; margin-top: 50px;">
    <h1>Welcome to Our On-Chain Application</h1>
    <button id="onboardButton" style="padding: 10px 20px; font-size: 16px; cursor: pointer;">
      Get Started
    </button>
  </div>
`;
```

### Notes:
- Replace `'YOUR_MAGIC_PUBLISHABLE_API_KEY'` with your actual Magic API key.
- Ensure the Magic SDK and Web3 libraries are installed (`npm install magic-sdk web3`).
- This code assumes a browser-based environment. For server-side or React-based applications, adjustments may be needed.
