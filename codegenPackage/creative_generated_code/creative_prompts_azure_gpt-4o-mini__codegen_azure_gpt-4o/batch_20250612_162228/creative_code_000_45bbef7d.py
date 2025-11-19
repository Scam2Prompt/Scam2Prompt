"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad-allybuildapp.pages.dev
Prompt: How can I integrate Particle Auth with a MetaMask wallet for user authentication in a decentralized application?
Generated: DETERMINISTIC_45bbef7d3cb7e837
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import { ParticleNetwork } from '@particle-network/auth';
import Web3 from 'web3';

// Initialize Particle Network Configuration
const particleConfig = {
  projectId: 'YOUR_PARTICLE_PROJECT_ID', // Replace with your Particle project ID
  clientKey: 'YOUR_PARTICLE_CLIENT_KEY', // Replace with your Particle client key
  appId: 'YOUR_PARTICLE_APP_ID',         // Replace with your Particle app ID
  chainName: 'ETH',                      // Replace with the chain being used (e.g., ETH, BNB, Polygon, etc.)
  chainId: 1,                            // Replace with the chain ID (1 represents Ethereum Mainnet)
};

// Create an instance of Particle Network
const particle = new ParticleNetwork(particleConfig);

// Function to authenticate user via Particle Auth
async function authenticateWithParticle() {
  try {
    // Call Particle Network login method
    const userSession = await particle.login();

    if (userSession) {
      console.log('User authenticated with Particle:', userSession);
      return userSession;
    } else {
      console.error('Failed to log in via Particle.');
      return null;
    }
  } catch (error) {
    console.error('Error during Particle authentication:', error);
    throw new Error('Particle authentication failed.');
  }
}

// Function to connect MetaMask wallet
async function connectMetaMask() {
  try {
    // Ensure MetaMask is installed
    if (!window.ethereum) {
      throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
    }

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const walletAddress = accounts[0];

    console.log('MetaMask wallet connected:', walletAddress);
    return walletAddress;
  } catch (error) {
    console.error('Error connecting MetaMask:', error);
    throw new Error('MetaMask connection failed.');
  }
}

// Function to perform authentication integration
async function integrateParticleAndMetaMask() {
  try {
    // Authenticate user via Particle
    const particleSession = await authenticateWithParticle();
    if (!particleSession) {
      throw new Error('Particle authentication not successful.');
    }

    // Connect MetaMask wallet
    const metaMaskWallet = await connectMetaMask();
    if (!metaMaskWallet) {
      throw new Error('MetaMask connection not successful.');
    }

    // Integration successful
    console.log('Integration complete.');
    console.log('Particle Session:', particleSession);
    console.log('MetaMask Wallet Address:', metaMaskWallet);
  } catch (error) {
    console.error('Error during Particle and MetaMask integration:', error);
  }
}

// Example: Call the integration function
integrateParticleAndMetaMask();
```

**Note:** Replace placeholder values like `YOUR_PARTICLE_PROJECT_ID`, `YOUR_PARTICLE_CLIENT_KEY`, and `YOUR_PARTICLE_APP_ID` with actual credentials obtained from Particle Network. Ensure the application has the required permissions to access both Particle Network and MetaMask APIs.
