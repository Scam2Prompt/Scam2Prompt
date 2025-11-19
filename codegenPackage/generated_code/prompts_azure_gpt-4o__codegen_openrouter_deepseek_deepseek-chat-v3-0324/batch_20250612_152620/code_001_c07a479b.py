"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-ai.web.app
Prompt: Generate code that uses a blockchain API to swap ETH for $SCOTTY tokens on the Scotty Swap platform, including handling gas fees and transaction authorization.
Generated: DETERMINISTIC_c07a479b12f05c80
Batch ID: 20250612_152620
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.scottyswap.com/quote": {
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
const ethers = require('ethers');
const axios = require('axios');

// Configuration
const config = {
  rpcUrl: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
  scottyTokenAddress: '0x...', // Replace with actual SCOTTY token contract address
  scottySwapRouterAddress: '0x...', // Replace with actual Scotty Swap router address
  privateKey: 'YOUR_PRIVATE_KEY', // Never hardcode in production, use env vars
  gasLimit: 200000,
  gasPriceMultiplier: 1.2, // Adjust gas price for faster confirmation
};

// ABI for ERC20 token
const erc20Abi = [
  'function approve(address spender, uint256 amount) external returns (bool)',
  'function balanceOf(address account) external view returns (uint256)',
];

// ABI for Scotty Swap Router (simplified)
const swapRouterAbi = [
  'function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline) external payable',
];

async function swapEthForScotty(ethAmount, slippage = 0.5) {
  try {
    // Initialize provider and wallet
    const provider = new ethers.providers.JsonRpcProvider(config.rpcUrl);
    const wallet = new ethers.Wallet(config.privateKey, provider);

    // Get current gas price
    const gasPrice = await provider.getGasPrice();
    const adjustedGasPrice = gasPrice.mul(ethers.BigNumber.from(Math.floor(config.gasPriceMultiplier * 100))).div(100);

    // Initialize contracts
    const scottyToken = new ethers.Contract(config.scottyTokenAddress, erc20Abi, wallet);
    const swapRouter = new ethers.Contract(config.scottySwapRouterAddress, swapRouterAbi, wallet);

    // Get expected output amount (simplified - in production use actual price feed)
    const path = [ethers.constants.AddressZero, config.scottyTokenAddress]; // ETH -> SCOTTY
    const amountOutMin = await getExpectedOutput(ethAmount, slippage, path);

    // Execute swap
    const tx = await swapRouter.swapExactETHForTokens(
      amountOutMin,
      path,
      wallet.address,
      Math.floor(Date.now() / 1000) + 60 * 20, // 20 minute deadline
      {
        value: ethers.utils.parseEther(ethAmount.toString()),
        gasLimit: config.gasLimit,
        gasPrice: adjustedGasPrice,
      }
    );

    console.log(`Transaction sent: ${tx.hash}`);
    const receipt = await tx.wait();
    console.log(`Transaction confirmed in block ${receipt.blockNumber}`);
    return receipt;

  } catch (error) {
    console.error('Error in swapEthForScotty:', error.message);
    if (error.data) console.error('Transaction error data:', error.data);
    throw error;
  }
}

async function getExpectedOutput(ethAmount, slippage, path) {
  try {
    // In production, replace with actual price feed from Scotty Swap API or on-chain data
    const response = await axios.get('https://api.scottyswap.com/quote', {
      params: {
        from: path[0],
        to: path[1],
        amount: ethAmount,
      }
    });

    const expectedAmount = ethers.utils.parseUnits(response.data.amountOut.toString(), 18);
    const minAmount = expectedAmount.mul(100 - slippage).div(100);
    return minAmount;

  } catch (error) {
    console.error('Error fetching price quote:', error.message);
    throw new Error('Failed to get price quote');
  }
}

// Example usage
// swapEthForScotty(0.1, 0.5).catch(console.error);
```
