"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica14.vercel.app
Prompt: Write a code snippet to connect a web app to the Solana network for user authentication.
Generated: DETERMINISTIC_378abb013b36c968
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import { Connection, clusterApiUrl, PublicKey } from '@solana/web3.js';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';

// Function to connect to the Solana network and authenticate a user
async function connectToSolana() {
  try {
    // Step 1: Setup Solana connection
    const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');
    console.log('Connected to the Solana network.');

    // Step 2: Initialize the Phantom wallet adapter
    const wallet = new PhantomWalletAdapter();

    // Ensure that the wallet is ready to use
    if (!wallet.connected) {
      await wallet.connect(); // Request connection to the wallet
    }
    console.log('Phantom wallet connected.');

    // Step 3: Get and display the public key of the user
    const publicKey = wallet.publicKey;
    if (!publicKey) {
      throw new Error('Failed to retrieve the public key from the wallet.');
    }
    console.log(`User's Wallet Address: ${publicKey.toBase58()}`);

    // Step 4: Verify connection by checking user balance (optional authentication step)
    const balance = await connection.getBalance(new PublicKey(publicKey));
    console.log(`User's Wallet Balance: ${balance / Math.pow(10, 9)} SOL`);
    
    // Return user wallet information
    return {
      publicKey: publicKey.toBase58(),
      balance: balance / Math.pow(10, 9), // Balance in SOL
    };
  } catch (error) {
    // Proper error handling
    console.error('Error connecting to Solana:', error.message);
    throw error; // Re-throw the error for upstream handling
  }
}

// Example usage: Connect and authenticate the user
connectToSolana()
  .then(userInfo => {
    console.log('User authenticated successfully:', userInfo);
  })
  .catch(error => {
    console.error('Authentication failed:', error.message);
  });
```

### Notes:
- Ensure `@solana/web3.js` and `@solana/wallet-adapter-phantom` are installed in your project via npm or yarn.
- You may need to configure the web app to allow interaction with the Phantom Wallet.
- This code assumes the user has already installed and set up the Phantom Wallet extension in their browser.
