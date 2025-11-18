"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interface-git-fork-chenxsan-bugfix-fix-scroll-top-uniswap.vercel.app
Prompt: Write a script to enable JavaScript functionality for a decentralized exchange interface, similar to the Uniswap Interface.
Generated: DETERMINISTIC_227824a74792629e
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import { Contract } from 'ethers';
import { abi as UniswapV2RouterAbi } from './UniswapV2Router.json'; // Adjust the path according to your project structure
import { abi as ERC20Abi } from './ERC20.json'; // Adjust the path according to your project structure

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Define constants for the Ethereum network and the Uniswap Router
const UNISWAP_V2_ROUTER_ADDRESS = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6'; // Uniswap V2 Router address
const TOKEN_CONTRACT_ADDRESS = '0xYourTokenAddress'; // Replace with your token address

// Initialize contract instances
const uniswapRouter = new web3.eth.Contract(UniswapV2RouterAbi, UNISWAP_V2_ROUTER_ADDRESS);
const tokenContract = new web3.eth.Contract(ERC20Abi, TOKEN_CONTRACT_ADDRESS);

// Enable user to connect their wallet
async function connectWallet() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];
        console.log(`Wallet connected: ${userAddress}`);
        return userAddress;
    } catch (error) {
        console.error('Failed to connect wallet:', error);
        alert('Failed to connect wallet. Please check your browser console for details.');
    }
}

// Fetch ETH and token balances for the connected wallet
async function fetchBalances(address) {
    try {
        const ethBalance = await web3.eth.getBalance(address);
        const tokenBalance = await tokenContract.methods.balanceOf(address).call();
        
        return {
            ethBalance: web3.utils.fromWei(ethBalance, 'ether'),
            tokenBalance: web3.utils.fromWei(tokenBalance, 'ether')
        };
    } catch (error) {
        console.error('Failed to fetch balances:', error);
    }
}

// Perform token swap using Uniswap
async function swapTokens(tokenAmount, slippage = 1) {
    const userAddress = await connectWallet();
    
    // Calculate the amount out with slippage
    const amountIn = web3.utils.toWei(tokenAmount.toString(), 'ether');
    const slippageAmount = (amountIn * slippage) / 100;
    const amountOutMin = (parseFloat(amountIn) - slippageAmount).toString();
    
    try {
        // Approve the token transfer to the Uniswap router
        await tokenContract.methods.approve(UNISWAP_V2_ROUTER_ADDRESS, amountIn).send({ from: userAddress });

        // Perform the swap
        const path = [TOKEN_CONTRACT_ADDRESS, '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE']; // Token to ETH
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now

        const swapTransaction = await uniswapRouter.methods.swapExactTokensForETH(
            amountIn,
            amountOutMin,
            path,
            userAddress,
            deadline
        ).send({ from: userAddress });

        console.log('Swap successful:', swapTransaction);
    } catch (error) {
        console.error('Swap transaction failed:', error);
        alert('Swap transaction failed. Please check your browser console for details.');
    }
}

// Event listener for swap button
document.getElementById('swapButton').addEventListener('click', async () => {
    const tokenAmount = document.getElementById('tokenAmountInput').value;
    await swapTokens(tokenAmount);
});

// Initialize the application
(async function init() {
    const userAddress = await connectWallet();
    if (userAddress) {
        const balances = await fetchBalances(userAddress);
        console.log('User Balances:', balances);
        // Update UI with balances if necessary
    }
})();
```
