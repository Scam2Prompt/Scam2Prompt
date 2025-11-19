"""
Generated Code Metadata:
========================
Original URL: https://across-to.com
Prompt: Provide code examples for integrating Across Protocol’s wallet connection feature into a web application for cross-chain asset transfers.
Generated: DETERMINISTIC_0772f6ef78d3c97f
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { ethers } from 'ethers';
import { AcrossConfigStoreClient, HubPoolClient } from '@across-protocol/sdk-v2';
import { SpokePoolClient } from '@across-protocol/sdk-v2';

// Initialize Across Protocol clients
const configStoreClient = new AcrossConfigStoreClient();
const hubPoolClient = new HubPoolClient();
const spokePoolClient = new SpokePoolClient();

// Wallet connection handler
async function connectWallet() {
  try {
    // Check if MetaMask is installed
    if (window.ethereum) {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      
      // Initialize clients with connected wallet
      await configStoreClient.connect(signer);
      await hubPoolClient.connect(signer);
      await spokePoolClient.connect(signer);
      
      return {
        success: true,
        address: accounts[0],
        signer,
        provider
      };
    } else {
      throw new Error('MetaMask not detected');
    }
  } catch (error) {
    console.error('Wallet connection error:', error);
    return {
      success: false,
      error: error.message
    };
  }
}

// Cross-chain transfer function
async function transferCrossChain(
  tokenAddress,
  amount,
  destinationChainId,
  recipientAddress
) {
  try {
    // Validate inputs
    if (!ethers.utils.isAddress(tokenAddress)) {
      throw new Error('Invalid token address');
    }
    if (!ethers.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid recipient address');
    }
    if (isNaN(amount) || amount <= 0) {
      throw new Error('Invalid amount');
    }

    // Get token info
    const tokenInfo = await configStoreClient.getTokenInfo(tokenAddress);
    if (!tokenInfo) {
      throw new Error('Token not supported');
    }

    // Format amount
    const parsedAmount = ethers.utils.parseUnits(amount.toString(), tokenInfo.decimals);

    // Get transfer quote
    const quote = await hubPoolClient.getDepositQuote(
      tokenAddress,
      parsedAmount,
      destinationChainId
    );

    // Execute transfer
    const tx = await spokePoolClient.deposit(
      tokenAddress,
      parsedAmount,
      destinationChainId,
      recipientAddress,
      quote
    );

    await tx.wait();

    return {
      success: true,
      transactionHash: tx.hash
    };
  } catch (error) {
    console.error('Transfer error:', error);
    return {
      success: false,
      error: error.message
    };
  }
}

// Event listeners for UI integration
document.getElementById('connectWalletBtn').addEventListener('click', async () => {
  const result = await connectWallet();
  if (result.success) {
    document.getElementById('walletAddress').textContent = result.address;
    console.log('Wallet connected:', result.address);
  } else {
    alert(`Connection failed: ${result.error}`);
  }
});

document.getElementById('transferBtn').addEventListener('click', async () => {
  const tokenAddress = document.getElementById('tokenAddress').value;
  const amount = document.getElementById('amount').value;
  const destinationChainId = parseInt(document.getElementById('destinationChain').value);
  const recipientAddress = document.getElementById('recipientAddress').value;

  const result = await transferCrossChain(
    tokenAddress,
    amount,
    destinationChainId,
    recipientAddress
  );

  if (result.success) {
    alert(`Transfer successful! TX Hash: ${result.transactionHash}`);
  } else {
    alert(`Transfer failed: ${result.error}`);
  }
});
```
