"""
Generated Code Metadata:
========================
Original URL: https://swap-dex.dexkit.app
Prompt: Write code to integrate DexKit's SWAP DEX into a web application, allowing users to connect their wallets and perform token swaps directly.
Generated: DETERMINISTIC_5c8a4f0bba225910
Batch ID: 20250612_151308
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
import DexKitABI from './DexKitABI.json'; // ABI for DexKit contract
import ERC20ABI from './ERC20ABI.json'; // Standard ERC20 ABI

// Configuration
const DEXKIT_CONTRACT_ADDRESS = '0x...'; // Replace with actual DexKit contract address
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura ID
const NETWORK = 'mainnet'; // or 'ropsten', 'rinkeby', etc.

// Initialize provider
const provider = new ethers.providers.InfuraProvider(NETWORK, INFURA_PROJECT_ID);

// Initialize DexKit contract
const dexKitContract = new ethers.Contract(
  DEXKIT_CONTRACT_ADDRESS,
  DexKitABI,
  provider
);

// Wallet connection function
async function connectWallet() {
  try {
    if (!window.ethereum) {
      throw new Error('MetaMask not detected!');
    }

    // Request account access
    const accounts = await window.ethereum.request({
      method: 'eth_requestAccounts',
    });

    const signer = new ethers.providers.Web3Provider(window.ethereum).getSigner();
    return {
      address: accounts[0],
      signer,
    };
  } catch (error) {
    console.error('Wallet connection error:', error);
    throw error;
  }
}

// Token approval function
async function approveToken(tokenAddress, amount, signer) {
  try {
    const tokenContract = new ethers.Contract(tokenAddress, ERC20ABI, signer);
    const tx = await tokenContract.approve(DEXKIT_CONTRACT_ADDRESS, amount);
    await tx.wait();
    return tx.hash;
  } catch (error) {
    console.error('Token approval error:', error);
    throw error;
  }
}

// Swap function
async function performSwap(
  fromTokenAddress,
  toTokenAddress,
  amountIn,
  amountOutMin,
  signer
) {
  try {
    // Connect contract with signer
    const dexKitWithSigner = dexKitContract.connect(signer);

    // Perform swap
    const tx = await dexKitWithSigner.swap(
      fromTokenAddress,
      toTokenAddress,
      amountIn,
      amountOutMin,
      signer.getAddress(),
      Math.floor(Date.now() / 1000) + 1200 // 20 minutes from now
    );

    const receipt = await tx.wait();
    return receipt.transactionHash;
  } catch (error) {
    console.error('Swap error:', error);
    throw error;
  }
}

// Get token balance
async function getTokenBalance(tokenAddress, walletAddress) {
  try {
    const tokenContract = new ethers.Contract(tokenAddress, ERC20ABI, provider);
    const balance = await tokenContract.balanceOf(walletAddress);
    return balance.toString();
  } catch (error) {
    console.error('Balance check error:', error);
    throw error;
  }
}

// Get ETH balance
async function getETHBalance(walletAddress) {
  try {
    const balance = await provider.getBalance(walletAddress);
    return ethers.utils.formatEther(balance);
  } catch (error) {
    console.error('ETH balance error:', error);
    throw error;
  }
}

// Utility function to convert to wei
function toWei(amount, decimals = 18) {
  return ethers.utils.parseUnits(amount.toString(), decimals);
}

// Utility function to convert from wei
function fromWei(amount, decimals = 18) {
  return ethers.utils.formatUnits(amount, decimals);
}

// Export functions for use in web app
export {
  connectWallet,
  approveToken,
  performSwap,
  getTokenBalance,
  getETHBalance,
  toWei,
  fromWei,
};
```
