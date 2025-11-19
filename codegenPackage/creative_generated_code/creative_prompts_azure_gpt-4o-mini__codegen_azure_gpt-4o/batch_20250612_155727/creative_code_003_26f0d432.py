"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-extra.fi
Prompt: How do I connect my Web3 wallet to Extra Finance for yield optimization, and what are the steps involved?
Generated: DETERMINISTIC_26f0d4329ff2652f
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider'; // WalletConnect for wallet integration
import ExtraFinanceSDK from 'extra-finance-sdk'; // Example SDK for accessing Extra Finance

// Configuration constants
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura Project ID
const EXTRA_FINANCE_API_KEY = 'your-extra-finance-api-key'; // Replace with your Extra Finance API Key

// Initialize WalletConnect provider
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: INFURA_PROJECT_ID, // Infura ID for WalletConnect
    },
  },
};

// Initialize Extra Finance SDK
const extraFinance = new ExtraFinanceSDK({
  apiKey: EXTRA_FINANCE_API_KEY, // Pass your API key for authentication
});

// Function to connect Web3 wallet
async function connectWallet() {
  try {
    // Initialize Web3 provider with WalletConnect
    const web3Provider = new WalletConnectProvider(providerOptions.walletconnect.options);

    // Enable the provider (opens the wallet modal)
    await web3Provider.enable();

    // Create a Web3 instance
    const web3 = new Web3(web3Provider);

    // Get the connected wallet accounts
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
      throw new Error('No accounts found. Please connect your wallet.');
    }

    const connectedAccount = accounts[0];
    console.log('Connected Wallet Address:', connectedAccount);

    // Fetch the current network ID
    const networkId = await web3.eth.net.getId();
    console.log('Connected Network ID:', networkId);

    // (Optional) Switch network if necessary
    if (networkId !== extraFinance.supportedNetworkId) {
      console.error('Unsupported network. Please switch to the supported network.');
      return;
    }

    // Authenticate wallet on Extra Finance platform
    const authResult = await extraFinance.authenticateWallet(connectedAccount);
    if (authResult.success) {
      console.log('Wallet successfully authenticated with Extra Finance.');
    } else {
      throw new Error('Authentication failed. Please try again.');
    }

    // Proceed with yield optimization
    await optimizeYield(web3, connectedAccount);
  } catch (error) {
    console.error('Error connecting wallet:', error.message || error);
  }
}

// Function to optimize yield via Extra Finance
async function optimizeYield(web3, walletAddress) {
  try {
    // Fetch the optimal strategy from Extra Finance
    const strategy = await extraFinance.getOptimalStrategy(walletAddress);
    console.log('Optimal Strategy:', strategy);

    // Approve the contract to spend tokens
    const tokenContract = new web3.eth.Contract(strategy.tokenABI, strategy.tokenAddress);
    const approvalTx = await tokenContract.methods
      .approve(strategy.contractAddress, strategy.requiredAmount)
      .send({ from: walletAddress });

    console.log('Approval Transaction:', approvalTx);

    // Execute the yield optimization strategy
    const optimizationTx = await extraFinance.executeStrategy(walletAddress, strategy);
    console.log('Optimization Transaction:', optimizationTx);

    console.log('Yield optimization completed successfully.');
  } catch (error) {
    console.error('Error during yield optimization:', error.message || error);
  }
}

// Entry point for connecting the wallet and optimizing yield
(async function main() {
  await connectWallet();
})();
```

### Note:
1. Replace `your-infura-project-id` and `your-extra-finance-api-key` with actual values obtained from Infura and Extra Finance.
2. Ensure Extra Finance SDK and WalletConnect provider packages are installed via npm (`npm install extra-finance-sdk @walletconnect/web3-provider web3`).
3. The code assumes `ExtraFinanceSDK` has appropriate methods (`authenticateWallet`, `getOptimalStrategy`, and `executeStrategy`). Modify according to the actual SDK documentation.
