"""
Generated Code Metadata:
========================
Original URL: https://zkswapfinance.gitbook.io
Prompt: Create a step-by-step guide in JavaScript for using zkSwap Finance's Aggregator to bridge tokens between Ethereum Layer 2 and other supported chains.
Generated: DETERMINISTIC_205c0e087874c163
Batch ID: 20250612_154728
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.zkswap.finance/tx-status/${txHash}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://zksync2-mainnet.zksync.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers');
const axios = require('axios');

// Configuration
const config = {
  zkSwapAggregatorAddress: '0x...', // Replace with actual zkSwap Aggregator contract address
  ethereumRpcUrl: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
  layer2RpcUrl: 'https://zksync2-mainnet.zksync.io', // Example for zkSync Era
  supportedChains: {
    1: 'Ethereum',
    324: 'zkSync Era',
    10: 'Optimism',
    42161: 'Arbitrum'
  },
  abi: [
    // ABI for zkSwap Aggregator contract
    'function getBridgeFee(uint256 chainId) view returns (uint256)',
    'function bridgeTokens(address token, uint256 amount, uint256 destChainId, address recipient) payable'
  ]
};

// Initialize providers
const ethProvider = new ethers.providers.JsonRpcProvider(config.ethereumRpcUrl);
const layer2Provider = new ethers.providers.JsonRpcProvider(config.layer2RpcUrl);

// Initialize wallet (replace with your private key or use a secure method)
const privateKey = 'YOUR_PRIVATE_KEY';
const wallet = new ethers.Wallet(privateKey, ethProvider);

// Step 1: Check supported chains
function getSupportedChains() {
  return config.supportedChains;
}

// Step 2: Get bridge fee estimate
async function getBridgeFee(destChainId) {
  try {
    const contract = new ethers.Contract(config.zkSwapAggregatorAddress, config.abi, wallet);
    const fee = await contract.getBridgeFee(destChainId);
    return ethers.utils.formatEther(fee);
  } catch (error) {
    console.error('Error getting bridge fee:', error);
    throw error;
  }
}

// Step 3: Get token approval (if needed)
async function approveToken(tokenAddress, amount, spender) {
  try {
    const tokenAbi = ['function approve(address spender, uint256 amount)'];
    const tokenContract = new ethers.Contract(tokenAddress, tokenAbi, wallet);
    
    const tx = await tokenContract.approve(spender, amount);
    await tx.wait();
    return tx.hash;
  } catch (error) {
    console.error('Error approving token:', error);
    throw error;
  }
}

// Step 4: Execute token bridge
async function bridgeTokens(tokenAddress, amount, destChainId, recipient) {
  try {
    // Check if chain is supported
    if (!config.supportedChains[destChainId]) {
      throw new Error('Destination chain not supported');
    }

    const contract = new ethers.Contract(config.zkSwapAggregatorAddress, config.abi, wallet);
    
    // Get fee and add to value
    const fee = await contract.getBridgeFee(destChainId);
    const value = fee.add(amount);

    // Execute bridge
    const tx = await contract.bridgeTokens(
      tokenAddress,
      amount,
      destChainId,
      recipient,
      { value: value }
    );

    await tx.wait();
    return tx.hash;
  } catch (error) {
    console.error('Error bridging tokens:', error);
    throw error;
  }
}

// Step 5: Check transaction status
async function checkTransactionStatus(txHash) {
  try {
    const response = await axios.get(`https://api.zkswap.finance/tx-status/${txHash}`);
    return response.data;
  } catch (error) {
    console.error('Error checking transaction status:', error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // 1. Check supported chains
    const chains = getSupportedChains();
    console.log('Supported chains:', chains);

    // 2. Get fee estimate (e.g., bridging to zkSync Era)
    const fee = await getBridgeFee(324);
    console.log('Bridge fee estimate:', fee, 'ETH');

    // 3. Approve token (if needed)
    const tokenAddress = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'; // USDC
    const amount = ethers.utils.parseUnits('100', 6); // 100 USDC
    const approvalTx = await approveToken(tokenAddress, amount, config.zkSwapAggregatorAddress);
    console.log('Approval transaction hash:', approvalTx);

    // 4. Bridge tokens
    const recipient = wallet.address; // Send to same address
    const bridgeTx = await bridgeTokens(tokenAddress, amount, 324, recipient);
    console.log('Bridge transaction hash:', bridgeTx);

    // 5. Check status
    const status = await checkTransactionStatus(bridgeTx);
    console.log('Transaction status:', status);
  } catch (error) {
    console.error('Error in example usage:', error);
  }
})();
```
