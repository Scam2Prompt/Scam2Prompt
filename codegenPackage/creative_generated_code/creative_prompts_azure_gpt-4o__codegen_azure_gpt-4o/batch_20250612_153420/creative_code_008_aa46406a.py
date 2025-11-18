"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad-allybuildapp.pages.dev
Prompt: Write code to authenticate users via Particle Auth and connect their wallets using WalletConnect in a decentralized finance (DeFi) application.
Generated: DETERMINISTIC_aa46406a3c667f7f
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ParticleNetwork } from "@particle-network/auth";
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Initialize Particle Auth
const particleNetwork = new ParticleNetwork({
  projectId: "your-particle-project-id", // Replace with your Particle Auth project ID
  clientKey: "your-particle-client-key", // Replace with your Particle Auth client key
  appId: "your-particle-app-id", // Replace with your Particle Auth app ID
});

// Function to authenticate user using Particle Auth
async function authenticateWithParticle() {
  try {
    // Display login modal for Particle Auth
    const user = await particleNetwork.auth.login();
    if (user) {
      console.log("User authenticated via Particle Auth:", user);
      return user;
    } else {
      console.log("Login canceled or failed.");
      return null;
    }
  } catch (error) {
    console.error("Error during Particle authentication:", error);
    throw new Error("Particle authentication failed.");
  }
}

// Function to connect user wallet using WalletConnect
async function connectWallet() {
  try {
    // Configure WalletConnect Provider
    const walletConnectProvider = new WalletConnectProvider({
      infuraId: "your-infura-id", // Replace with your Infura project ID
    });

    // Enable WalletConnect provider
    await walletConnectProvider.enable();

    // Initialize Web3 with WalletConnect provider
    const web3 = new Web3(walletConnectProvider);

    // Fetch connected accounts
    const accounts = await web3.eth.getAccounts();
    console.log("Wallet connected. Accounts:", accounts);

    return { web3, accounts };
  } catch (error) {
    console.error("Error during wallet connection:", error);
    throw new Error("Wallet connection failed.");
  }
}

// Main function to authenticate user and connect wallet
async function initializeDeFiApp() {
  try {
    console.log("Initializing DeFi application...");

    // Step 1: Authenticate user via Particle Auth
    const user = await authenticateWithParticle();
    if (!user) {
      console.log("User authentication failed. Exiting.");
      return;
    }

    // Step 2: Connect user's wallet
    const { web3, accounts } = await connectWallet();
    if (accounts.length === 0) {
      console.log("No wallet connected. Exiting.");
      return;
    }

    console.log("DeFi application initialized successfully.");
    console.log("Authenticated user:", user);
    console.log("Connected wallet accounts:", accounts);
  } catch (error) {
    console.error("Error during initialization:", error);
  }
}

// Execute initialization when the application starts
initializeDeFiApp();
```
