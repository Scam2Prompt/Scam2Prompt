"""
Generated Code Metadata:
========================
Original URL: https://asud8uas8da.pages.dev
Prompt: Generate a step-by-step guide on how to buy $PEEPO using Metamask and Uniswap, including wallet setup and ETH swapping.
Generated: DETERMINISTIC_3f53e8df04f24d3b
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Step 1: Install MetaMask Extension
// This is a manual step - user needs to install MetaMask from the Chrome Web Store or Firefox Add-ons

// Step 2: Create or Import Wallet
// This is handled by MetaMask UI - no code needed

// Step 3: Connect MetaMask to Ethereum Network
async function connectToEthereum() {
  try {
    if (window.ethereum) {
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      console.log('Connected to Ethereum network');
    } else {
      throw new Error('MetaMask not detected');
    }
  } catch (error) {
    console.error('Error connecting to Ethereum:', error);
  }
}

// Step 4: Add ETH to Wallet (Manual process - user needs to buy ETH from exchange)

// Step 5: Connect to Uniswap
async function connectToUniswap() {
  try {
    if (!window.ethereum) throw new Error('MetaMask not detected');
    
    // This would be triggered by a "Connect Wallet" button in UI
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected to Uniswap with account:', accounts[0]);
  } catch (error) {
    console.error('Error connecting to Uniswap:', error);
  }
}

// Step 6: Swap ETH for $PEEPO
async function swapEthForPeepo(ethAmount, peepoContractAddress) {
  try {
    if (!window.ethereum) throw new Error('MetaMask not detected');
    
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    
    // Uniswap Router V2 address
    const uniswapRouterAddress = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D';
    const uniswapRouterABI = [
      'function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline) external payable returns (uint[] memory amounts)'
    ];
    
    const uniswapRouter = new ethers.Contract(uniswapRouterAddress, uniswapRouterABI, signer);
    
    // Transaction parameters
    const amountOutMin = 0; // Accept any amount (front-running risk, better to calculate)
    const path = [
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', // WETH
      peepoContractAddress // PEEPO
    ];
    const to = await signer.getAddress(); // Recipient
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes
    
    // Execute swap
    const tx = await uniswapRouter.swapExactETHForTokens(
      amountOutMin,
      path,
      to,
      deadline,
      { value: ethers.utils.parseEther(ethAmount.toString()) }
    );
    
    console.log('Transaction hash:', tx.hash);
    return tx;
  } catch (error) {
    console.error('Error swapping ETH for PEEPO:', error);
    throw error;
  }
}

// Step 7: Add $PEEPO token to MetaMask
async function addTokenToMetaMask(tokenAddress, tokenSymbol, decimals) {
  try {
    if (!window.ethereum) throw new Error('MetaMask not detected');
    
    const wasAdded = await window.ethereum.request({
      method: 'wallet_watchAsset',
      params: {
        type: 'ERC20',
        options: {
          address: tokenAddress,
          symbol: tokenSymbol,
          decimals: decimals,
        },
      },
    });
    
    if (wasAdded) {
      console.log('Token added to MetaMask');
    } else {
      console.log('Token was not added');
    }
  } catch (error) {
    console.error('Error adding token to MetaMask:', error);
  }
}

// Example usage:
// connectToEthereum();
// connectToUniswap();
// swapEthForPeepo(0.1, '0x...PEEPO_CONTRACT_ADDRESS');
// addTokenToMetaMask('0x...PEEPO_CONTRACT_ADDRESS', 'PEEPO', 18);
```
