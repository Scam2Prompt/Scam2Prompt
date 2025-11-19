"""
Generated Code Metadata:
========================
Original URL: https://ethphb.com
Prompt: Generate code to enable JavaScript-based interaction with an Ethereum pledge platform, ensuring proper wallet integration and transaction validation.
Generated: DETERMINISTIC_7e43467fdc127920
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers');
const Web3Modal = require('web3modal');

// Configuration
const config = {
  network: 'mainnet', // or 'ropsten', 'rinkeby', etc.
  contractAddress: '0xYourContractAddressHere',
  contractABI: [/* Your Contract ABI here */],
  infuraId: 'your-infura-project-id' // Optional, for Infura provider
};

// Initialize Web3Modal
const web3Modal = new Web3Modal({
  network: config.network,
  cacheProvider: true,
  providerOptions: {} // Add wallet providers here if needed
});

// Global variables
let provider;
let signer;
let contract;

// Connect Wallet Function
async function connectWallet() {
  try {
    const instance = await web3Modal.connect();
    provider = new ethers.providers.Web3Provider(instance);
    signer = provider.getSigner();
    contract = new ethers.Contract(config.contractAddress, config.contractABI, signer);
    
    const address = await signer.getAddress();
    console.log('Connected with address:', address);
    return address;
  } catch (error) {
    console.error('Error connecting wallet:', error);
    throw error;
  }
}

// Check if Wallet is Connected
async function checkWalletConnection() {
  try {
    if (!provider) {
      throw new Error('Wallet not connected');
    }
    const address = await signer.getAddress();
    return address;
  } catch (error) {
    console.error('Wallet connection check failed:', error);
    throw error;
  }
}

// Make Pledge Function
async function makePledge(amount) {
  try {
    // Validate amount
    if (!amount || isNaN(amount) || amount <= 0) {
      throw new Error('Invalid pledge amount');
    }

    // Check wallet connection
    await checkWalletConnection();

    // Convert amount to wei
    const weiAmount = ethers.utils.parseEther(amount.toString());

    // Estimate gas
    const gasEstimate = await contract.estimateGas.pledge(weiAmount);
    const gasPrice = await provider.getGasPrice();

    // Send transaction
    const tx = await contract.pledge(weiAmount, {
      gasLimit: gasEstimate.mul(2), // Add buffer
      gasPrice: gasPrice.mul(2) // Add buffer
    });

    console.log('Transaction sent:', tx.hash);
    
    // Wait for confirmation
    const receipt = await tx.wait();
    console.log('Transaction confirmed:', receipt.transactionHash);
    
    return receipt;
  } catch (error) {
    console.error('Error making pledge:', error);
    throw error;
  }
}

// Get Pledge Amount Function
async function getPledgeAmount(address) {
  try {
    if (!provider) {
      await connectWallet();
    }

    const pledgeAmount = await contract.getPledgeAmount(address);
    return ethers.utils.formatEther(pledgeAmount);
  } catch (error) {
    console.error('Error getting pledge amount:', error);
    throw error;
  }
}

// Event Listeners
function setupEventListeners() {
  if (!contract) return;

  contract.on('PledgeMade', (pledger, amount, event) => {
    console.log(`New pledge from ${pledger}: ${ethers.utils.formatEther(amount)} ETH`);
    // Update UI or trigger callback
  });

  contract.on('PledgeWithdrawn', (pledger, amount, event) => {
    console.log(`Pledge withdrawn by ${pledger}: ${ethers.utils.formatEther(amount)} ETH`);
    // Update UI or trigger callback
  });
}

// Initialize
async function init() {
  try {
    await connectWallet();
    setupEventListeners();
  } catch (error) {
    console.error('Initialization error:', error);
  }
}

// Export functions for use in your application
module.exports = {
  connectWallet,
  checkWalletConnection,
  makePledge,
  getPledgeAmount,
  init
};
```
