"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoppyc0inerc20.pages.dev
Prompt: Generate a step-by-step guide for integrating MetaMask with a decentralized application (dApp) to allow users to swap ETH for HOPPY tokens using the Uniswap API.
Generated: DETERMINISTIC_eda048d69e3f9ae0
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Integration of MetaMask with a decentralized application (dApp) 
 * to allow users to swap ETH for HOPPY tokens using the Uniswap API.
 */

// Import required dependencies
const ethers = require('ethers');

// Define constants for the Uniswap Router contract and HOPPY token
const UNISWAP_ROUTER_ADDRESS = '0xE592427A0AEce92De3Edee1F18E0157C05861564'; // Example: Uniswap V3 Router address
const HOPPY_TOKEN_ADDRESS = '0xYourHoppyTokenAddressHere'; // Replace with actual HOPPY token address

// ABI for the Uniswap Router (simplified for swapping)
const UNISWAP_ROUTER_ABI = [
  'function exactInputSingle((address,address,uint24,address,uint256,uint256,uint256,uint160) struct) external payable returns (uint256)'
];

// Step-by-step guide starts here

async function connectMetaMask() {
  // Check if MetaMask is installed
  if (!window.ethereum) {
    throw new Error('MetaMask is not installed. Please install MetaMask to use this dApp.');
  }

  // Request connection to MetaMask
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
  return accounts[0]; // Return the connected account
}

async function createSigner() {
  // Connect to Ethereum provider
  const provider = new ethers.providers.Web3Provider(window.ethereum);

  // Create a signer for transaction signing
  const signer = provider.getSigner();
  return signer;
}

async function swapETHForHOPPY(signer, amountInETH) {
  // Validate input
  if (!signer || !amountInETH || amountInETH <= 0) {
    throw new Error('Invalid inputs for swapping.');
  }

  // Create a contract instance for the Uniswap Router
  const uniswapRouter = new ethers.Contract(UNISWAP_ROUTER_ADDRESS, UNISWAP_ROUTER_ABI, signer);

  // Define swap parameters
  const params = {
    tokenIn: ethers.constants.AddressZero, // ETH (native token)
    tokenOut: HOPPY_TOKEN_ADDRESS,        // HOPPY token
    fee: 3000,                            // Pool fee (example: 0.3%)
    recipient: await signer.getAddress(), // Recipient address (current user)
    deadline: Math.floor(Date.now() / 1000) + 60 * 10, // 10-minute transaction deadline
    amountIn: ethers.utils.parseEther(amountInETH.toString()), // Input ETH amount
    amountOutMinimum: 0,                  // Minimum output (no slippage protection for simplicity)
    sqrtPriceLimitX96: 0                  // Price limit (no restriction)
  };

  // Execute the swap
  const tx = await uniswapRouter.exactInputSingle(params, { value: params.amountIn });
  await tx.wait(); // Wait for transaction to be mined

  console.log(`Swap successful! Transaction hash: ${tx.hash}`);
}

async function main() {
  try {
    // Step 1: Connect MetaMask
    console.log('Connecting to MetaMask...');
    const userAddress = await connectMetaMask();
    console.log(`Connected with address: ${userAddress}`);

    // Step 2: Create signer
    const signer = await createSigner();

    // Step 3: Swap ETH for HOPPY tokens
    const ethAmount = 0.1; // Example: Swap 0.1 ETH
    console.log(`Swapping ${ethAmount} ETH for HOPPY tokens...`);
    await swapETHForHOPPY(signer, ethAmount);

    console.log('Swap complete!');
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

// Execute the main function
main();

```

This code integrates MetaMask with your dApp to allow users to swap ETH for HOPPY tokens using the Uniswap API. Ensure you replace placeholders (like `HOPPY_TOKEN_ADDRESS`) with actual values for your dApp configuration.
