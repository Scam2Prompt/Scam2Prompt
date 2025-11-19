"""
Generated Code Metadata:
========================
Original URL: https://alternative-uniswap-interface.pages.dev
Prompt: Can you provide code examples for creating a decentralized exchange interface using JavaScript, inspired by the Alternative Uniswap Interface?
Generated: DETERMINISTIC_72e697c269e96a17
Batch ID: 20250612_135940
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
const { abi } = require('@uniswap/v2-core/build/UniswapV2Factory.json');
const { abi: pairAbi } = require('@uniswap/v2-core/build/UniswapV2Pair.json');
const { abi: routerAbi } = require('@uniswap/v2-periphery/build/UniswapV2Router02.json');

// Configuration
const config = {
  network: 'homestead',
  infuraId: 'YOUR_INFURA_PROJECT_ID',
  factoryAddress: '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f', // Uniswap V2 Factory
  routerAddress: '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D' // Uniswap V2 Router
};

// Initialize provider and contracts
const provider = new ethers.providers.InfuraProvider(config.network, config.infuraId);
const factoryContract = new ethers.Contract(config.factoryAddress, abi, provider);
const routerContract = new ethers.Contract(config.routerAddress, routerAbi, provider);

// UI Elements
const tokenInput = document.getElementById('token-input');
const ethInput = document.getElementById('eth-input');
const swapButton = document.getElementById('swap-button');
const connectButton = document.getElementById('connect-button');
const statusDisplay = document.getElementById('status');

// Wallet connection
async function connectWallet() {
  try {
    if (window.ethereum) {
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      statusDisplay.textContent = `Connected: ${await signer.getAddress()}`;
      return signer;
    } else {
      throw new Error('No Ethereum provider found');
    }
  } catch (error) {
    statusDisplay.textContent = `Error: ${error.message}`;
    return null;
  }
}

// Token swap function
async function swapTokens(tokenAddress, amountIn, amountOutMin, signer) {
  try {
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes
    const path = [tokenAddress, ethers.constants.AddressZero]; // Token to ETH
    
    const routerWithSigner = routerContract.connect(signer);
    const tx = await routerWithSigner.swapExactTokensForETH(
      amountIn,
      amountOutMin,
      path,
      await signer.getAddress(),
      deadline
    );
    
    statusDisplay.textContent = 'Transaction sent. Waiting for confirmation...';
    await tx.wait();
    statusDisplay.textContent = 'Swap completed successfully!';
  } catch (error) {
    statusDisplay.textContent = `Swap failed: ${error.message}`;
  }
}

// Get pair info
async function getPairInfo(tokenA, tokenB) {
  try {
    const pairAddress = await factoryContract.getPair(tokenA, tokenB);
    if (pairAddress === ethers.constants.AddressZero) {
      throw new Error('Pair does not exist');
    }
    
    const pairContract = new ethers.Contract(pairAddress, pairAbi, provider);
    const reserves = await pairContract.getReserves();
    
    return {
      pairAddress,
      reserve0: reserves[0],
      reserve1: reserves[1]
    };
  } catch (error) {
    statusDisplay.textContent = `Error fetching pair info: ${error.message}`;
    return null;
  }
}

// Get price impact
async function calculatePriceImpact(tokenAddress, amountIn) {
  try {
    const pairInfo = await getPairInfo(tokenAddress, ethers.constants.AddressZero);
    if (!pairInfo) return null;
    
    const tokenReserve = pairInfo.reserve0;
    const ethReserve = pairInfo.reserve1;
    
    const amountInWithFee = amountIn.mul(997);
    const numerator = amountInWithFee.mul(ethReserve);
    const denominator = tokenReserve.mul(1000).add(amountInWithFee);
    const amountOut = numerator.div(denominator);
    
    const priceImpact = amountOut.div(ethReserve).mul(100);
    return priceImpact;
  } catch (error) {
    statusDisplay.textContent = `Error calculating price impact: ${error.message}`;
    return null;
  }
}

// Event listeners
connectButton.addEventListener('click', connectWallet);

swapButton.addEventListener('click', async () => {
  const signer = await connectWallet();
  if (!signer) return;
  
  const tokenAddress = tokenInput.value.trim();
  const amountIn = ethers.utils.parseEther(tokenInput.value);
  const amountOutMin = ethers.utils.parseEther(ethInput.value);
  
  if (!tokenAddress || !amountIn.gt(0) || !amountOutMin.gt(0)) {
    statusDisplay.textContent = 'Invalid input values';
    return;
  }
  
  const priceImpact = await calculatePriceImpact(tokenAddress, amountIn);
  if (priceImpact && priceImpact.gt(5)) {
    statusDisplay.textContent = 'Warning: High price impact (>5%)';
    return;
  }
  
  await swapTokens(tokenAddress, amountIn, amountOutMin, signer);
});

// Initialize UI
document.addEventListener('DOMContentLoaded', () => {
  statusDisplay.textContent = 'Ready to connect wallet';
});
```
