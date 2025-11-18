"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Provide a step-by-step guide for integrating the EarthMeta Wallet with popular Web3 libraries like MetaMask and Trust Wallet for seamless user login.
Generated: DETERMINISTIC_70e4d267b47abd1b
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3'; // Web3.js library to interact with Ethereum blockchain
import detectEthereumProvider from '@metamask/detect-provider'; // Detects MetaMask provider

/**
 * Step 1: Initialize Web3 and provider
 */
async function initializeWeb3() {
  try {
    // Detect Ethereum provider (MetaMask or similar)
    const provider = await detectEthereumProvider();

    if (!provider) {
      throw new Error('Ethereum provider not found. Please install MetaMask or a compatible wallet.');
    }

    // Initialize Web3 instance
    const web3 = new Web3(provider);
    console.log('Web3 initialized successfully:', web3);

    return web3;
  } catch (error) {
    console.error('Error initializing Web3:', error.message);
    throw error;
  }
}

/**
 * Step 2: Connect to Wallet
 */
async function connectWallet(web3) {
  try {
    // Request accounts from wallet
    const accounts = await web3.eth.requestAccounts();

    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure your wallet is unlocked.');
    }

    console.log('Connected account:', accounts[0]);
    return accounts[0]; // Return the connected account
  } catch (error) {
    console.error('Error connecting wallet:', error.message);
    throw error;
  }
}

/**
 * Step 3: Authenticate User (Example: Message Signing)
 */
async function authenticateUser(web3, account) {
  try {
    const message = 'Welcome to EarthMeta Wallet! Please sign this message to authenticate.';
    const signature = await web3.eth.personal.sign(message, account, '');

    console.log('Signed message:', signature);
    return signature; // Return signed message for backend verification
  } catch (error) {
    console.error('Error signing message:', error.message);
    throw error;
  }
}

/**
 * Step 4: Integrate with Trust Wallet
 * Trust Wallet uses WalletConnect protocol, which requires additional setup.
 */
import WalletConnectProvider from '@walletconnect/web3-provider'; // WalletConnect provider library

async function connectWithTrustWallet() {
  try {
    // Initialize WalletConnect provider
    const walletConnectProvider = new WalletConnectProvider({
      infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura Project ID
    });

    await walletConnectProvider.enable(); // Open WalletConnect QR code modal for user connection

    // Initialize Web3 instance with WalletConnect provider
    const web3 = new Web3(walletConnectProvider);
    console.log('Connected with Trust Wallet:', web3);

    // Retrieve account
    const accounts = await web3.eth.getAccounts();

    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure your wallet is unlocked.');
    }

    console.log('Trust Wallet connected account:', accounts[0]);
    return { web3, account: accounts[0] }; // Return Web3 instance and connected account
  } catch (error) {
    console.error('Error connecting with Trust Wallet:', error.message);
    throw error;
  }
}

/**
 * Example Usage
 */
(async () => {
  try {
    console.log('Initializing EarthMeta Wallet integration...');

    // MetaMask Integration
    const web3 = await initializeWeb3();
    const account = await connectWallet(web3);
    const signedMessage = await authenticateUser(web3, account);
    console.log('User successfully authenticated with MetaMask:', signedMessage);

    // Trust Wallet Integration
    const trustWalletConnection = await connectWithTrustWallet();
    console.log('User connected successfully with Trust Wallet:', trustWalletConnection);

  } catch (error) {
    console.error('An error occurred during wallet integration:', error.message);
  }
})();
```

This code integrates EarthMeta Wallet with MetaMask and Trust Wallet, following Web3 best practices. Replace the placeholder `YOUR_INFURA_PROJECT_ID` with a valid Infura project ID for WalletConnect functionality.
