"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pioneerparticle-sigma.vercel.app
Prompt: How can I implement Wallet Abstraction in my dApp using Particle Network's Modular L1?
Generated: DETERMINISTIC_86c7d0ccb8da2fda
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules from Particle Network SDK
import { ParticleNetwork, ParticleProvider } from '@particle-network/connect';
import Web3 from 'web3';

// Initialize Particle Network
const particleNetwork = new ParticleNetwork({
  chainName: 'Ethereum', // Replace with the name of the chain you want to use (e.g., 'Ethereum', 'BSC', etc.)
  chainId: 1, // Replace with the chain ID for your selected network
  projectId: 'your_project_id', // Replace with your Particle Network project ID
  clientKey: 'your_client_key', // Replace with your Particle Network client key
  appId: 'your_app_id', // Replace with your Particle Network app ID
});

// Create a Web3 provider using Particle Network
const particleProvider = new ParticleProvider(particleNetwork);
const web3 = new Web3(particleProvider);

// Function to connect wallet
async function connectWallet() {
  try {
    // Trigger Particle Network login
    await particleNetwork.authService.login();
    console.log('Wallet connected successfully');
  } catch (error) {
    console.error('Error connecting wallet:', error);
  }
}

// Function to get wallet address
async function getWalletAddress() {
  try {
    const accounts = await web3.eth.getAccounts();
    if (accounts.length > 0) {
      console.log('Wallet Address:', accounts[0]);
      return accounts[0];
    } else {
      console.log('No wallet connected');
      return null;
    }
  } catch (error) {
    console.error('Error fetching wallet address:', error);
    return null;
  }
}

// Function to send transaction
async function sendTransaction(to, valueInEther) {
  try {
    const from = await getWalletAddress();
    if (!from) {
      throw new Error('Wallet not connected');
    }

    const transaction = {
      from: from,
      to: to,
      value: web3.utils.toWei(valueInEther, 'ether'),
    };

    const txHash = await web3.eth.sendTransaction(transaction);
    console.log('Transaction successful:', txHash);
    return txHash;
  } catch (error) {
    console.error('Error sending transaction:', error);
    throw error;
  }
}

// Example usage
async function main() {
  await connectWallet(); // Connect wallet
  const walletAddress = await getWalletAddress(); // Fetch wallet address
  if (walletAddress) {
    await sendTransaction('recipient_wallet_address_here', '0.01'); // Replace with recipient address and amount in Ether
  }
}

// Execute the example
main().catch((error) => {
  console.error('Error in main function:', error);
});
```

> Ensure you replace placeholders like `your_project_id`, `your_client_key`, `your_app_id`, and `recipient_wallet_address_here` with your actual Particle Network credentials and recipient details.
