"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Provide an example of integrating Arcana Network for Google, Twitter, and Discord login functionality in MultiversX apps.
Generated: DETERMINISTIC_0860da27908eea95
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import { AuthProvider } from '@arcana/auth'; // Arcana Network Auth SDK
import { MultiversX } from '@multiversx/sdk'; // MultiversX SDK

// Configuration object for Arcana Auth
const arcanaConfig = {
  appID: '<YOUR_ARCANA_APP_ID>', // Replace with your Arcana App ID
  theme: 'light', // Theme for the login widget ('light' or 'dark')
  position: 'right', // Position of the login widget ('right' or 'left')
};

// Initialize Arcana AuthProvider
const authProvider = new AuthProvider(arcanaConfig);

// Supported social login types
const socialLogins = {
  google: 'google',
  twitter: 'twitter',
  discord: 'discord',
};

// Function to log in using Arcana and integrate with MultiversX
async function loginWithArcana(socialLoginType) {
  try {
    // Validate the input login type
    if (!socialLogins[socialLoginType]) {
      throw new Error('Unsupported social login type.');
    }

    // Authenticate the user via Arcana
    const user = await authProvider.loginWithSocial(socialLogins[socialLoginType]);

    // Access user's wallet details
    const walletAddress = user.wallet.address;
    const publicKey = user.wallet.publicKey;

    console.log(`Logged in successfully! Wallet Address: ${walletAddress}`);

    // Initialize MultiversX SDK with user's wallet address
    const multiversxConfig = {
      network: 'mainnet', // Replace with desired network ('mainnet', 'testnet', etc.)
      walletAddress: walletAddress,
    };

    const multiversx = new MultiversX(multiversxConfig);

    // Example: Fetch user's MultiversX balance
    const balance = await multiversx.getBalance();
    console.log(`User's MultiversX balance: ${balance}`);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error during login or MultiversX integration:', error.message);
  }
}

// Example usage: Login with Google
loginWithArcana('google');

// Example usage: Login with Twitter
// loginWithArcana('twitter');

// Example usage: Login with Discord
// loginWithArcana('discord');
```

Before running the code, make sure to replace `<YOUR_ARCANA_APP_ID>` with your Arcana App ID and configure the `multiversxConfig` appropriately for the desired network. Ensure that the required SDKs (`@arcana/auth` and `@multiversx/sdk`) are installed in your project.
